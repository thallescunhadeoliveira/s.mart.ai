# 🛒 s.mart.ai - Chatbot Inteligente para Análise de Compras 📈

## 📌 Sobre o Projeto

🤖 s.mart.ai é uma aplicação web interativa que permite aos usuários registrarem e consultarem seus hábitos de consumo a partir de notas fiscais (imagem ou QR Code NFe-C).<br>
Com essa ferramenta, você pode:<br>
- Extrair automaticamente os dados de compras, itens e estabelecimentos;<br>
- Salvar esse histórico de forma estruturada e anônima;<br>
- Conversar com uma IA (LLM) que responde perguntas sobre suas compras e oferece análises personalizadas.<br>

🤔 Exemplos de perguntas que o agente responde:
- “Quanto gastei em bebidas no último mês?”<br>
- “Qual foi a última vez que comprei sabonete?”<br>

---
## 📋 Teste o Projeto!
Você pode testar o projeto diretamente pelo Streamlit, sem necessidade de instalação local.<br>

⚠️ Atenção: Este é um ambiente público e demonstrativo, com os seguintes pontos a considerar:<br>
- Os dados de exemplo já registrados são utilizados por padrão no chat.<br>
- É possível subir suas próprias imagens de notas fiscais. A imagem não será armazenada, mas os dados extraídos (de forma anonimizada) serão salvos em um banco de dados acessível por outros usuários.<br>
- Não há login ou controle por usuário, por se tratar de uma versão de demonstração.<br>
- As conversas com o chat são registradas apenas para fins de melhoria da aplicação e monitoramento de uso (tokens).<br>

👉 Acesse o projeto clicando
  <a href="https://smartai-chat.streamlit.app/" target="_blank">
    <button style="padding: 10px 20px; font-size: 16px; background-color: #FF4B4B; color: white; border: none; border-radius: 5px; cursor: pointer;">
      aqui
    </button>
  </a>.

---
## ⚙️ Funcionalidades Principais

### 📷 Inserção de registros por foto ou QR Code NFE-C

- É possível fazer o upload de foto de Nota Fiscal para que o agente leia e registre os dados
- Também é possível ler QR Code da nota para acessar os dados da receita federal, sem identificar o comprador.
- Para maior assertividade e padronização nos nomes do produto, a LLM lê e raciocina sobre cada item para ajustar os nomes.
- Ex: PAO HB PULLMAN -> Pão de Hambúrguer Pullman

### 💬 Conversa com Histórico Contextualizado

- O chatbot mantém um histórico das interações com o usuário para fornecer respostas mais relevantes e coerentes.
- A análise e a comunicação dos dados são realizadas por agentes especializados, garantindo respostas precisas e contextualizadas.
- Ao ser questionado sobre alguma informação acerca dos dados, o Agente Buscador ajuda a transformar a dúvida em uma consulta ao banco de dados.

### 📄 Dados de Exemplo

- O projeto inclui um arquivo de dados de exemplo (`samples.json`) com diversas compras simuladas para facilitar testes e desenvolvimento.
- Estes exemplos podem ser importados diretamente na coleção MongoDB para rápida inicialização.

---
## 🚀 Instruções de Configuração

### ✅ Requisitos

- Python 3.8+
- MongoDB (Atlas ou local)
- API do Google Gemini
- Pacotes listados em `requirements.txt`

### 👣 Passos para rodar o projeto

1. **Clone o repositório**

2. **Instale as dependências**

- Insira sua API do Google Gemini nos arquivos de configuração (.env - caso queira rodar apenas localmente e secrets.toml - caso queira rodar com streamlit cloud)

4. **Configure o MongoDB:**

- Crie um cluster no MongoDB Atlas ou utilize um servidor local.
- Crie uma base de dados chamada "smartai" e uma coleção chamada "historico_compras".
- Atualize o arquivo de configuração do projeto (.env e secrets.toml) com a string de conexão MongoDB
- (Opcional) Importe os dados de exemplo com o arquivo data/samples/mongo.py

4. **Rode o Streamlit:**
- Mude para o diretório do app
- $ cd app
- streamlit run main.py --server.runOnSave true

---
## 📁 Estrutura do projeto
s.mart.ai/<br>
├── app/<br>
│ ├── main.py    # Arquivo principal, executa o streamlit<br>
│ ├── db.py    # Conexão com o banco de dados<br>
│ └── config.py    # Variáveis de ambiente e chaves de API<br>
│<br>
├── models/<br>
│ ├── agents.py    # Definição dos agentes<br>
│ └── prompts.py    # Definição dos prompts de sistema para os agentes<br>
│<br>
├── utils/<br>
│ └── utils.py    # Funções a serem usadas no código<br>
│<br>
├── samples/<br>
│ ├── mongo.py    # Popula banco de dados com dados de exemplo<br>
│ └── samples.json    # Dados de exemplos salvo em formato .json<br>
│<br>
├── requirements.txt    # Dependências do projeto<br>
├── secrets.toml    # Chave API e String de conexão ao MongoDB<br>
├── .env    # Variáveis de ambiente (não versionado)<br>
├── README.md    # Este arquivo<br>
└── .gitignore<br>

---
## 👨‍💻 Desenvolvedor

**Thalles Oliveira**  [![GitHub](https://img.shields.io/badge/-000000?style=flat-square&logo=github)](https://github.com/thallescunhadeoliveira) [![LinkedIn](https://img.shields.io/badge/-in-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thalles-cunha-de-oliveira/)
