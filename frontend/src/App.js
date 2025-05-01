import React, { useState } from 'react';
import './App.css';
import { generateMeme } from './api';

function App() {
  const [imageUrl, setImageUrl] = useState('');
  const [memeText, setMemeText] = useState('');
  const [generatedMeme, setGeneratedMeme] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [previewImage, setPreviewImage] = useState(null);

  // Função para validar URL
  const isValidUrl = (string) => {
    try {
      new URL(string);
      return true;
    } catch (_) {
      return false;
    }
  };

  // Função para visualizar a imagem antes de gerar o meme
  const handlePreview = () => {
    if (!imageUrl) {
      setError('Por favor, insira uma URL de imagem');
      setPreviewImage(null);
      return;
    }

    if (!isValidUrl(imageUrl)) {
      setError('URL inválida. Por favor, insira uma URL completa (começando com http:// ou https://)');
      setPreviewImage(null);
      return;
    }

    setError(null);
    setPreviewImage(imageUrl);
  };

  // Função para gerar o meme
  const handleGenerateMeme = async () => {
    if (!imageUrl || !memeText) {
      setError('Por favor, preencha todos os campos');
      return;
    }

    if (!isValidUrl(imageUrl)) {
      setError('URL inválida. Por favor, insira uma URL completa (começando com http:// ou https://)');
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const result = await generateMeme(imageUrl, memeText);
      
      if (result.success) {
        setGeneratedMeme({
          url: imageUrl,
          text: memeText,
          generatedImageUrl: result.memeUrl
        });
      } else {
        setError(result.error);
      }
    } catch (err) {
      setError('Erro ao gerar o meme. Por favor, tente novamente.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Gerador de Memes</h1>
        <p>Crie memes a partir de qualquer imagem da web</p>
      </header>

      <main className="App-main">
        <div className="input-section">
          <div className="form-group">
            <label htmlFor="imageUrl">URL da Imagem:</label>
            <input
              type="text"
              id="imageUrl"
              value={imageUrl}
              onChange={(e) => setImageUrl(e.target.value)}
              placeholder="https://exemplo.com/imagem.jpg"
            />
            <button onClick={handlePreview} className="preview-button">
              Visualizar Imagem
            </button>
          </div>

          <div className="form-group">
            <label htmlFor="memeText">Texto do Meme:</label>
            <input
              type="text"
              id="memeText"
              value={memeText}
              onChange={(e) => setMemeText(e.target.value)}
              placeholder="DIGITE SEU TEXTO AQUI"
            />
          </div>

          <button 
            onClick={handleGenerateMeme} 
            disabled={isLoading}
            className="generate-button"
          >
            {isLoading ? 'Gerando...' : 'Gerar Meme'}
          </button>

          {error && <div className="error-message">{error}</div>}
        </div>

        <div className="preview-section">
          <div className="image-container">
            <h3>Imagem Original</h3>
            {previewImage ? (
              <img src={previewImage} alt="Preview" className="preview-img" />
            ) : (
              <div className="placeholder">
                <p>Visualização da imagem aparecerá aqui</p>
              </div>
            )}
          </div>

          <div className="image-container">
            <h3>Meme Gerado</h3>
            {generatedMeme ? (
              <div className="generated-meme">
                <img src={generatedMeme.generatedImageUrl} alt="Meme gerado" className="meme-img" />
                <a 
                  href={generatedMeme.generatedImageUrl} 
                  download="meme.png"
                  className="download-button"
                >
                  Baixar Meme
                </a>
              </div>
            ) : (
              <div className="placeholder">
                <p>Seu meme aparecerá aqui</p>
              </div>
            )}
          </div>
        </div>
      </main>

      <footer className="App-footer">
        <p>Criado com ❤️ usando React, Python e Amazon Q Developer CLI</p>
        <p>AWS User Group Campinas, AWS User Group Circuito das Águas Paulistas e AWS User Group Interior de São Paulo</p>
      </footer>
    </div>
  );
}

export default App;
