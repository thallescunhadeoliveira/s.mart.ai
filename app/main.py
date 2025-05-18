import os
import sys
import io
from PIL import Image
import streamlit as st

# Adiciona o diretório raiz ao sys.path para permitir imports relativos entre pastas
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# Imports do projeto
from models.agents import Agents
from db import historico_compras
from utils.utils import construir_historico
from app.config import client, MODEL_ID



agents = Agents(client, MODEL_ID)

def main():
    st.set_page_config(page_title="s.mart.ai - Chatbot", page_icon="🤖")

    st.title("s.mart.at - Chatbot")
    st.write("Converse com o chatbot e envie imagens para ele analisar.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Mostrar o histórico da conversa
    st.markdown("---")
    st.subheader("Histórico da conversa:")
    for speaker, message in st.session_state.chat_history:
        if speaker == "Você":
            st.markdown(f"**Você:** {message}")
        else:
            st.markdown(f"**{speaker}:** {message}")

    # Input do usuário com key fixa e botão que envia também no Enter
    def enviar_mensagem():
        user_input = st.session_state.user_input.strip()
        if user_input != "":
            st.session_state.chat_history.append(("Você", user_input))
            
            historico = construir_historico(st.session_state.chat_history, user_input)
            resposta = None

            try:
                agente = agents.agente_orquestrador(user_input)
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

            st.session_state.chat_history.append(("s.mart.at", resposta))
            # Limpar input após enviar
            st.session_state.user_input = ""

    # Campo de texto com callback para enviar no Enter
    st.text_input("Digite sua mensagem:", key="user_input", on_change=enviar_mensagem)
    
    # Botão enviar para quem preferir clicar
    if st.button("Enviar"):
        enviar_mensagem()

if __name__ == "__main__":
    main()
