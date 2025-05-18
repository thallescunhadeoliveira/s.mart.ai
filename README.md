s.mart.at - Chatbot Inteligente para Análise de Compras 🛒🤖
Sobre o Projeto
Este projeto implementa um chatbot inteligente que permite a interação via texto e análise de imagens de notas fiscais para extração de dados de compras. O sistema utiliza inteligência artificial para processar o histórico de compras armazenado em um banco de dados MongoDB e responder perguntas contextualizadas com base nesses dados.

Funcionalidades Principais
Conversa com Histórico Contextualizado 💬
O chatbot mantém um histórico das interações com o usuário para fornecer respostas mais relevantes e coerentes.

É possível enviar imagens contendo notas fiscais para que o chatbot extraia automaticamente os dados e os armazene no banco.

A análise e a comunicação dos dados são realizadas por agentes especializados, garantindo respostas precisas e contextualizadas.

Dados de Exemplo 📄
O projeto inclui um arquivo de dados de exemplo (samples.json) com diversas compras simuladas para facilitar testes e desenvolvimento.

Estes exemplos podem ser importados diretamente na coleção MongoDB para rápida inicialização.

Instruções de Configuração 🚀
Requisitos
Python 3.8+

MongoDB (Atlas ou local)

Pacotes listados em requirements.txt

Passos para rodar o projeto
Clone o repositório:

bash
Copy
Edit
git clone <URL_DO_REPOSITORIO>
cd s.mart.at
Instale as dependências:

bash
Copy
Edit
pip install -r requirements.txt
Configure o MongoDB:

Crie um cluster no MongoDB Atlas ou utilize um servidor local.

Crie uma base de dados e uma coleção chamada historico_compras.

Atualize o arquivo de configuração do projeto (app/config.py ou variável de ambiente) com a string de conexão MongoDB.

(Opcional) Importe os dados de exemplo:

python
Copy
Edit
import json
from db import historico_compras

with open('samples.json', 'r') as f:
    data = json.load(f)

historico_compras.insert_many(data)
Execute a aplicação Streamlit:

bash
Copy
Edit
streamlit run app/main.py
Uso
A interface web apresenta o histórico da conversa.

Digite sua mensagem na barra ao final da página.

Para enviar, clique no botão Enviar ou pressione Enter.

Você pode enviar imagens de notas fiscais para que o chatbot analise e atualize o histórico automaticamente.

As respostas são geradas com base no histórico e nas informações extraídas.

Considerações Finais
Este projeto busca unir automação, análise inteligente e interação natural para facilitar o acompanhamento e entendimento do histórico de compras. É ideal para quem deseja um assistente inteligente integrado a dados reais de compras.

Se precisar de ajuda ou tiver sugestões, sinta-se à vontade para abrir uma issue ou enviar um pull request!

✨ Obrigado por usar o s.mart.at! ✨