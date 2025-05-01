# Frontend do Gerador de Memes

Este é o frontend do aplicativo Gerador de Memes, desenvolvido com React.

## Estrutura do Projeto

```
frontend/
├── public/                 # Arquivos públicos
├── src/                    # Código fonte
│   ├── App.js              # Componente principal
│   ├── App.css             # Estilos do componente principal
│   ├── api.js              # Funções para comunicação com a API
│   ├── index.js            # Ponto de entrada da aplicação
│   └── ...                 # Outros arquivos
├── package.json            # Dependências e scripts
└── README.md               # Este arquivo
```

## Instalação

1. Instale as dependências:
```bash
npm install
```

## Execução

Para iniciar o servidor de desenvolvimento:

```bash
npm start
```

A aplicação estará disponível em http://localhost:3000.

## Build para Produção

Para criar uma versão otimizada para produção:

```bash
npm run build
```

Os arquivos serão gerados no diretório `build/`.

## Funcionalidades

- Inserção de URL de imagem
- Visualização prévia da imagem
- Adição de texto no estilo de meme
- Geração do meme
- Download do meme gerado
