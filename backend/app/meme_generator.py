#!/usr/bin/env python3
"""
Gerador de Memes usando PIL
-------------------------------------
Este script permite gerar memes adicionando texto diretamente à imagem usando PIL.
Implementa princípios de código limpo para melhor manutenibilidade.
"""

import logging
import os
from typing import List, Tuple

from PIL import Image, ImageDraw, ImageFont

# Configurações globais
DEFAULT_OUTPUT_FILENAME = "meme_output.png"
TEXT_MARGIN_PERCENT = 0.9  # Texto usa 90% da largura da imagem
TOP_MARGIN_PERCENT = 0.05  # Margem superior de 5% da altura da imagem
LINE_SPACING_FACTOR = 1.2  # Espaçamento entre linhas é 1.2x o tamanho da fonte
FONT_SIZE_DIVISOR = 12  # Tamanho da fonte é largura da imagem / 12
OUTLINE_WIDTH_DIVISOR = 15  # Espessura do contorno é tamanho da fonte / 15
TEXT_COLOR = "white"
OUTLINE_COLOR = "black"
PREFERRED_FONTS = ["Impact", "Arial Bold", "Helvetica Bold"]

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MemeGenerator:
    """Classe responsável por gerar memes com texto sobreposto em imagens."""
    
    def __init__(self) -> None:
        """Inicializa o gerador de memes."""
        logger.info("Inicializando gerador de memes com PIL")
    
    def generate_meme(self, image: Image.Image, text: str) -> Image.Image:
        """
        Gera um meme adicionando texto à imagem fornecida.
        
        Args:
            image: Objeto Image da PIL
            text: Texto a ser adicionado ao meme
            
        Returns:
            Image: Objeto Image da PIL com o meme gerado
            
        Raises:
            ValueError: Se os parâmetros forem inválidos
        """
        if not text.strip():
            raise ValueError("O texto não pode estar vazio")
        
        try:
            # Criar uma cópia da imagem para não modificar a original
            meme = image.copy()
            draw = ImageDraw.Draw(meme)
            
            # Configurar fonte e texto
            font = self._get_appropriate_font(meme.width)
            text_lines = self._wrap_text(draw, text.upper(), font, meme.width)
            
            # Adicionar texto à imagem
            self._add_text_to_image(draw, text_lines, font, meme.width, meme.height)
            
            return meme
                
        except Exception as e:
            logger.error(f"Erro inesperado ao gerar meme: {e}")
            raise
    
    def _get_appropriate_font(self, image_width: int) -> ImageFont.FreeTypeFont:
        """
        Obtém uma fonte apropriada para o meme baseada na largura da imagem.
        
        Args:
            image_width: Largura da imagem em pixels
            
        Returns:
            Objeto de fonte para desenhar o texto
        """
        font_size = int(image_width / FONT_SIZE_DIVISOR)
        
        # Tenta carregar uma das fontes preferidas
        for font_name in PREFERRED_FONTS:
            try:
                return ImageFont.truetype(font_name, font_size)
            except IOError:
                continue
        
        # Se nenhuma fonte preferida estiver disponível, usa a padrão
        logger.warning("Nenhuma fonte preferida encontrada, usando fonte padrão")
        return ImageFont.load_default()
    
    def _get_text_width(self, draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> float:
        """
        Obtém a largura do texto com a fonte especificada.
        
        Args:
            draw: Objeto ImageDraw
            text: Texto a ser medido
            font: Fonte a ser usada
            
        Returns:
            Largura do texto em pixels
        """
        try:
            return draw.textlength(text, font=font)
        except AttributeError:
            # Para versões mais antigas do PIL
            return font.getlength(text)
    
    def _wrap_text(self, draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, 
                  max_width: int) -> List[str]:
        """
        Quebra o texto em múltiplas linhas para caber na largura da imagem.
        
        Args:
            draw: Objeto ImageDraw
            text: Texto a ser quebrado
            font: Fonte a ser usada
            max_width: Largura máxima disponível
            
        Returns:
            Lista de linhas de texto
        """
        words = text.split()
        if not words:
            return []
            
        lines = []
        current_line = []
        max_text_width = max_width * TEXT_MARGIN_PERCENT
        
        for word in words:
            # Adicionar palavra à linha atual
            current_line.append(word)
            
            # Verificar a largura da linha atual
            line_text = " ".join(current_line)
            line_width = self._get_text_width(draw, line_text, font)
            
            # Se a linha for muito larga, remover a última palavra e começar uma nova linha
            if line_width > max_text_width:
                current_line.pop()  # Remover a última palavra
                
                if current_line:  # Se ainda houver palavras na linha atual
                    lines.append(" ".join(current_line))
                
                current_line = [word]  # Começar nova linha com a palavra atual
        
        # Adicionar a última linha
        if current_line:
            lines.append(" ".join(current_line))
        
        return lines
    
    def _draw_text_with_outline(self, draw: ImageDraw.ImageDraw, text: str, position: Tuple[float, float], 
                               font: ImageFont.FreeTypeFont, font_size: int) -> None:
        """
        Desenha texto com contorno para melhor visibilidade.
        
        Args:
            draw: Objeto ImageDraw
            text: Texto a ser desenhado
            position: Posição (x, y) para desenhar o texto
            font: Fonte a ser usada
            font_size: Tamanho da fonte para calcular a espessura do contorno
        """
        outline_width = max(1, int(font_size / OUTLINE_WIDTH_DIVISOR))
        
        # Desenhar o contorno (deslocando o texto em várias direções)
        for dx, dy in [(j, i) for i in range(-outline_width, outline_width + 1) 
                      for j in range(-outline_width, outline_width + 1)
                      if (i != 0 or j != 0)]:
            draw.text((position[0] + dx, position[1] + dy), text, font=font, fill=OUTLINE_COLOR)
        
        # Desenhar o texto principal
        draw.text(position, text, font=font, fill=TEXT_COLOR)
    
    def _add_text_to_image(self, draw: ImageDraw.ImageDraw, text_lines: List[str], 
                          font: ImageFont.FreeTypeFont, image_width: int, image_height: int) -> None:
        """
        Adiciona linhas de texto à imagem.
        
        Args:
            draw: Objeto ImageDraw
            text_lines: Lista de linhas de texto
            font: Fonte a ser usada
            image_width: Largura da imagem
            image_height: Altura da imagem
        """
        if not text_lines:
            return
            
        # Calcular parâmetros de posicionamento
        font_size = int(image_width / FONT_SIZE_DIVISOR)
        line_height = font_size * LINE_SPACING_FACTOR
        y_position = image_height * TOP_MARGIN_PERCENT
        
        # Adicionar cada linha de texto
        for line in text_lines:
            line_width = self._get_text_width(draw, line, font)
            x_position = (image_width - line_width) / 2  # Centralizar horizontalmente
            
            self._draw_text_with_outline(draw, line, (x_position, y_position), font, font_size)
            y_position += line_height  # Mover para a próxima linha
