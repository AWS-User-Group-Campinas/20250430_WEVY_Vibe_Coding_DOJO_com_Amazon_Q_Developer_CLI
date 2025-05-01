# Backend do Gerador de Memes

Este é o backend do aplicativo Gerador de Memes, responsável por processar imagens e adicionar texto no estilo de memes.

## Estrutura do Projeto

```
backend/
├── app/                    # Pacote principal da aplicação
│   ├── __init__.py         # Inicialização do pacote
│   ├── meme_generator.py   # Lógica de geração de memes
│   └── server.py           # Servidor Flask com endpoints da API
├── images/                 # Diretório para armazenar imagens
│   ├── memes/              # Memes gerados
│   ├── source/             # Imagens originais
│   └── temp/               # Arquivos temporários
├── run.py                  # Script para iniciar o servidor
└── requirements.txt        # Dependências do projeto
```

## Instalação

1. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução

Para iniciar o servidor:

```bash
python run.py
```

O servidor estará disponível em http://localhost:5000.

## API Endpoints

### Gerar Meme
- **URL**: `/api/generate-meme`
- **Método**: POST
- **Corpo da Requisição**:
  ```json
  {
    "imageUrl": "https://exemplo.com/imagem.jpg",
    "text": "TEXTO DO MEME"
  }
  ```
- **Resposta de Sucesso**:
  ```json
  {
    "success": true,
    "message": "Meme gerado com sucesso",
    "memeUrl": "/api/memes/meme_uuid.png"
  }
  ```

### Obter Meme
- **URL**: `/api/memes/<filename>`
- **Método**: GET
- **Resposta**: Arquivo de imagem (PNG)
