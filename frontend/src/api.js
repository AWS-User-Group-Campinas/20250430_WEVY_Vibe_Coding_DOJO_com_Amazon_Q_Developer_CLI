import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const generateMeme = async (imageUrl, text) => {
  try {
    const response = await axios.post(`${API_URL}/generate-meme`, {
      imageUrl,
      text
    });
    
    return {
      success: true,
      data: response.data,
      memeUrl: `http://localhost:5000${response.data.memeUrl}`
    };
  } catch (error) {
    console.error('Error generating meme:', error);
    return {
      success: false,
      error: error.response?.data?.error || 'Erro ao gerar o meme'
    };
  }
};
