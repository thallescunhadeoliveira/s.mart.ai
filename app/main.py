import os
import sys
from PIL import Image
import streamlit as st
from pprint import pprint

# Adiciona o diretório raiz ao sys.path para permitir imports relativos entre pastas
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# Imports do projeto
from models.agents import Agents
from db import historico_compras
from utils.utils import construir_historico, formata_registro
from app.config import client, MODEL_ID


agents = Agents(client, MODEL_ID)

def main():

    # TO DO atualizar esse techo com o nome do ultimo arquivo e checar antes de ler
    if "imagem_processada" not in st.session_state:
        st.session_state.imagem_processada = False

    st.set_page_config(page_title="s.mart.ai - Chatbot", page_icon="🤖")

    st.title("s.mart.ai - Chatbot")
    st.write("Converse com o chatbot e envie imagens para ele analisar.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Mostrar o histórico da conversa
    st.markdown("---")
    st.subheader("Histórico da conversa:")
    # CSS para estilizar os balões
    st.markdown("""
    <style>
    .chat-message {
        padding: 0.5rem 1rem;
        margin: 0.25rem 0;
        border-radius: 0.75rem;
        max-width: 70%;
        display: inline-block;
        word-wrap: break-word;
    }
    .user-message {
        background-color: #DCF8C6;
        margin-left: auto;
        text-align: right;
    }
    .bot-message {
        background-color: #F1F0F0;
        margin-right: auto;
        text-align: left;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    </style>
    """, unsafe_allow_html=True)

    # Renderiza as mensagens com layout visual
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for speaker, message in st.session_state.chat_history:
        if speaker == "Você":
            st.markdown(f'<div class="chat-message user-message">{message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message bot-message"><strong>{speaker}:</strong> {message}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Input do usuário com key fixa e botão que envia também no Enter
    def enviar_mensagem():
        user_input = st.session_state.user_input.strip()
        if user_input != "":
            st.session_state.chat_history.append(("Você", user_input))
            
            historico = construir_historico(st.session_state.chat_history, user_input)
            resposta = None

            try:
                agente = agents.agente_orquestrador(user_input)
                print(f"Agente: {agente}")
                agente = str(agente).strip()
                if agente not in ("agente_conversador", "agente_buscador"):
                    agente = "agente_conversador"
            except Exception as e:
                print("Erro no agente_orquestrador:", e)
                agente = "agente_conversador"

            if agente == "agente_conversador":
                try:
                    resposta = agents.agente_conversador(historico)
                except Exception as e:
                    st.error("Não consegui conversar agora. Tente de novo mais tarde.")
                    print("Erro no agente_conversador:", e)

            elif agente == "agente_buscador":
                try:
                    resultados = list(historico_compras.find({}, {'_id': 0}))
                except Exception as e:
                    st.error("Houve um problema ao buscar no histórico de compras.")
                    print("Erro no acesso ao MongoDB:", e)
                    resultados = []

                try:
                    analise = agents.agente_analista(resultados, user_input)
                    resposta = agents.agente_comunicador(analise, user_input)
                except Exception as e:
                    st.error("Não consegui analisar ou comunicar os dados.")
                    print("Erro no agente_analista ou agente_comunicador:", e)

            st.session_state.chat_history.append(("s.mart.ai", resposta))
            # Limpar input após enviar
            st.session_state.user_input = ""

    # Campo de texto com callback para enviar no Enter
    st.text_input("Digite sua mensagem:", key="user_input", on_change=enviar_mensagem)
    
    # Botão enviar para quem preferir clicar
    if st.button("Enviar"):
        enviar_mensagem()


    # Upload de imagem
    uploaded_file = st.file_uploader("Envie uma imagem para o chatbot:", type=["png", "jpg", "jpeg"])
  
    if uploaded_file and st.session_state.imagem_processada != uploaded_file.name:
        st.session_state.imagem_processada = uploaded_file.name
        st.write("s.mart.ai recebeu sua imagem! Processando...")
        with st.spinner('👀 Lendo o arquivo...'):

            try:
                output_arquivo = Image.open(uploaded_file)
                extracao = agents.agente_leitor(output_arquivo)
            except Exception as e:
                st.error("Falha na extração dos dados da imagem.")
                print("Erro no agente_leitor:", e)
                resposta = "Não consegui extrair informações da imagem."
                st.session_state.chat_history.append(("s.mart.ai", resposta))
                return
        
        print(f"Extração: ")
        pprint(extracao)

        with st.spinner('🛠️ Ajustando o arquivo...'):
            try:
                registros_formatados = formata_registro(extracao)
            except Exception as e:
                st.error("Falha na formatacao dos dados.")
                print("Erro na função formata_registro:", e)
                resposta = "Não consegui tratar as informações lidas na imagem."
                st.session_state.chat_history.append(("s.mart.ai", resposta))
                return

        print(f"registros_formatados: ")
        pprint(registros_formatados)

        with st.spinner('💾 Salvando dados...'):
            # Inserir no MongoDB
            try:
                result = historico_compras.insert_many(registros_formatados)
                st.success(f"{len(result.inserted_ids)} itens inseridos no histórico de compras.")
                resposta = f"{len(result.inserted_ids)} itens foram adicionados ao seu histórico de compras."
                st.session_state.chat_history.append(("s.mart.ai", resposta))
            except Exception as e:
                st.error("Falha ao inserir dados no banco.")
                print("Erro no insert_many do MongoDB:", e)
                resposta = "Não consegui salvar os dados no banco de dados."
                st.session_state.chat_history.append(("s.mart.ai", resposta))
                return
        try:            
            feedback = agents.agente_feedback(registros_formatados)
            print(feedback)
            st.session_state.chat_history.append(("s.mart.ai", feedback))
            st.rerun()
        except Exception as e:
            st.error("Erro no agente Feedback.")
            print("Erro no agente Feedback.:", e)
            return

if __name__ == "__main__":
    main()
