"""
Servidor Flask para o gerador de memes.
Fornece endpoints para gerar memes a partir de imagens.
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import requests
from io import BytesIO
import uuid
import logging
from PIL import Image

from app.meme_generator import MemeGenerator

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configurações
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
TEMP_FOLDER = os.path.join(IMAGES_DIR, 'temp')
MEMES_FOLDER = os.path.join(IMAGES_DIR, 'memes')
SOURCE_FOLDER = os.path.join(IMAGES_DIR, 'source')

# Criar diretórios se não existirem
os.makedirs(TEMP_FOLDER, exist_ok=True)
os.makedirs(MEMES_FOLDER, exist_ok=True)
os.makedirs(SOURCE_FOLDER, exist_ok=True)

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas as rotas

# Inicializar o gerador de memes
meme_generator = MemeGenerator()

@app.route('/api/generate-meme', methods=['POST'])
def api_generate_meme():
    """API endpoint para gerar um meme a partir de uma URL de imagem e texto"""
    try:
        data = request.json
        
        if not data or 'imageUrl' not in data or 'text' not in data:
            return jsonify({'error': 'Dados incompletos. Forneça imageUrl e text'}), 400
        
        image_url = data['imageUrl']
        text = data['text']
        
        # Baixar a imagem da URL
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()  # Lança exceção para códigos de erro HTTP
            
            # Carregar a imagem usando PIL
            image = Image.open(BytesIO(response.content))
            
            # Gerar o meme
            meme_image = meme_generator.generate_meme(image, text)
            
            # Salvar o meme em um arquivo
            meme_filename = f"meme_{uuid.uuid4()}.png"
            meme_path = os.path.join(MEMES_FOLDER, meme_filename)
            meme_image.save(meme_path)
            
            # Retornar o caminho do arquivo
            return jsonify({
                'success': True,
                'message': 'Meme gerado com sucesso',
                'memeUrl': f"/api/memes/{meme_filename}"
            })
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao baixar a imagem: {e}")
            return jsonify({'error': f'Erro ao baixar a imagem: {str(e)}'}), 400
        except Exception as e:
            logger.error(f"Erro ao processar a imagem: {e}")
            return jsonify({'error': f'Erro ao processar a imagem: {str(e)}'}), 500
    
    except Exception as e:
        logger.error(f"Erro interno do servidor: {e}")
        return jsonify({'error': f'Erro interno do servidor: {str(e)}'}), 500

@app.route('/api/memes/<filename>', methods=['GET'])
def get_meme(filename):
    """Retorna um meme gerado pelo nome do arquivo"""
    try:
        return send_file(os.path.join(MEMES_FOLDER, filename), mimetype='image/png')
    except Exception as e:
        logger.error(f"Erro ao buscar o meme: {e}")
        return jsonify({'error': f'Meme não encontrado: {str(e)}'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
