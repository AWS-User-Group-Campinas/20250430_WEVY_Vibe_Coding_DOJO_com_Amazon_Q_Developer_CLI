# Gerador de Memes

Este projeto é um gerador de memes simples que permite adicionar texto no estilo clássico de memes a qualquer imagem.

Ele foi criado colaborativamente (Randori) durante um VIDE CODING DOJO em um meetup dos grupos AWS User Group Campinas, AWS User Group Circuito das águas e AWS User Group Interior de São Paulo em 30/04/2025.

![Exemplo de Meme](/images/meme_4bcad1c2-a575-4872-8e84-90aadb4893d6.png)

## Estrutura do Projeto

```
.
├── README.md                # Este arquivo
├── AmazonQ.md               # Informações sobre Amazon Q e IA Generativa
├── backend/                 # Backend em Python/Flask
│   ├── app/                 # Pacote principal da aplicação
│   │   ├── __init__.py      # Inicialização do pacote
│   │   ├── meme_generator.py # Lógica de geração de memes
│   │   └── server.py        # Servidor Flask com endpoints da API
│   ├── images/              # Diretório para armazenar imagens
│   │   ├── memes/           # Memes gerados
│   │   ├── source/          # Imagens originais
│   │   └── temp/            # Arquivos temporários
│   ├── run.py               # Script para iniciar o servidor
│   └── requirements.txt     # Dependências do backend
└── frontend/                # Frontend em React
    ├── public/              # Arquivos públicos
    ├── src/                 # Código fonte
    │   ├── App.js           # Componente principal
    │   ├── App.css          # Estilos do componente principal
    │   ├── api.js           # Funções para comunicação com a API
    │   ├── index.js         # Ponto de entrada da aplicação
    │   └── ...              # Outros arquivos
    ├── package.json         # Dependências e scripts
    └── README.md            # Documentação do frontend
```

## Pré-requisitos

- Python 3.8 ou superior
- Node.js 14 ou superior
- Biblioteca Python: Pillow, Flask, Flask-CORS, requests
- Bibliotecas JavaScript: React, Axios

## Instalação

### Backend (Python)

1. Crie um ambiente virtual dentro do diretório backend e instale as dependências:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend (React)

1. Instale as dependências do frontend:
```bash
cd frontend
npm install
```

## Execução

1. Inicie o servidor backend:
```bash
cd backend
source venv/bin/activate  # Se ainda não estiver ativado
python run.py
```

2. Em outro terminal, inicie o frontend:
```bash
cd frontend
npm start
```

3. Acesse a aplicação em seu navegador: http://localhost:3000

## Como usar

1. Cole a URL de uma imagem da web no campo "URL da Imagem"
2. Clique em "Visualizar Imagem" para ver a imagem original
3. Digite o texto do meme no campo "Texto do Meme"
4. Clique em "Gerar Meme" para criar o meme
5. Use o botão "Baixar Meme" para salvar o meme gerado

## Características

- **Interface web amigável**: Fácil de usar e intuitiva
- **Texto com contorno**: Texto branco com contorno preto para garantir legibilidade
- **Quebra automática de texto**: Textos longos são divididos em múltiplas linhas
- **Centralização automática**: O texto é centralizado na imagem
- **Organização de arquivos**: Imagens de origem e memes são armazenados em pastas separadas

## Princípios de Código Limpo

Este projeto foi desenvolvido seguindo princípios de código limpo:

- **Responsabilidade Única**: Cada componente tem uma única responsabilidade
- **DRY (Don't Repeat Yourself)**: Evita duplicação de código
- **Nomes Significativos**: Variáveis e funções com nomes descritivos
- **Tratamento de Erros**: Tratamento adequado de exceções
- **Configuração Externa**: Valores configuráveis definidos como constantes
- **Documentação**: Docstrings e comentários detalhados

## Próximos passos

- Adicionar suporte para upload de imagens locais
- Implementar templates de memes populares
- Adicionar opções de personalização de fonte e posicionamento do texto
- Suporte para adicionar texto na parte inferior da imagem
- Implementar autenticação de usuários
