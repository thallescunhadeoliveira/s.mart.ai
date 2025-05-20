# s.mart.ai - Chatbot Inteligente para Análise de Compras 🛒🤖

## Sobre o Projeto

s.mart.ai é uma aplicação web interativa que permite conversar com um chatbot inteligente baseado em dados reais de histórico de compras armazenados em MongoDB. Através de interações naturais, o usuário pode consultar, analisar e receber respostas contextualizadas a partir do seu histórico de compras.

---

## Funcionalidades Principais

### Conversa com Histórico Contextualizado 💬

- O chatbot mantém um histórico das interações com o usuário para fornecer respostas mais relevantes e coerentes.
- A análise e a comunicação dos dados são realizadas por agentes especializados, garantindo respostas precisas e contextualizadas.

### Dados de Exemplo 📄

- O projeto inclui um arquivo de dados de exemplo (`samples.json`) com diversas compras simuladas para facilitar testes e desenvolvimento.
- Estes exemplos podem ser importados diretamente na coleção MongoDB para rápida inicialização.

---

## Instruções de Configuração 🚀

### Requisitos

- Python 3.8+
- MongoDB (Atlas ou local)
- Pacotes listados em `requirements.txt`

### Passos para rodar o projeto

1. **Clone o repositório**

2. **Instale as dependências**

- Insira sua API do Google Gemini

4. **Configure o MongoDB:**

- Crie um cluster no MongoDB Atlas ou utilize um servidor local.
- Crie uma base de dados chamada "smartai" e uma coleção chamada "historico_compras".
- Atualize o arquivo de configuração do projeto (app/config.py ou variável de ambiente) com a string de conexão MongoDB
- (Opcional) Importe os dados de exemplo com o arquivo data/samples/mongo.py

4. **Rode o Streamlit:**
- Mude para o diretório do app
- $ cd app
- streamlit run main.py --server.runOnSave true


### **Considerações Finais**
O projeto tinha como uma das principais features a leitura e extração de dados de Notas Fiscais, porém não consegui terminar a tempo!
Parte do código se encontra no repositório pois planejo continuar o desenvolvimento do projeto.

Se precisar de ajuda ou tiver sugestões, sinta-se à vontade para abrir uma issue ou enviar um pull request!

✨ Obrigado por usar o s.mart.ai! ✨
