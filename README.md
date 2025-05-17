# s.mart.ai
Chat bot de IA onde podemos interagir sobre nosso histórico de compras

s-mart-ai/
│
├── app/                       # Código principal do app Streamlit
│   ├── __init__.py
│   ├── main.py                # Ponto de entrada do app
│   ├── chatbot.py             # Lógica do chatbot
│   ├── upload.py              # Upload de imagem e OCR
│   ├── auth.py                # Autenticação de usuários
│   ├── db.py                  # Conexão e funções de banco de dados
│   └── utils.py               # Funções auxiliares
│
├── data/                      # Dados locais (apenas para testes)
│   └── samples/               # Imagens de exemplo
│
├── models/                    # Agentes ou modelos NLP usados no chatbot
│   └── agent.py               # Interpretação e resposta de perguntas
│
├── requirements.txt           # Bibliotecas usadas no projeto
├── .streamlit/                # Configurações do Streamlit
│   └── config.toml
├── .env                       # Variáveis de ambiente (credenciais)
├── .gitignore                 # Arquivos a serem ignorados pelo Git
└── README.md                  # Explicação e instruções do projeto
