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

    # Criar um container para mostrar a conversa
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Input do usuário
    user_input = st.text_input("Digite sua mensagem:", "")

    # Botão para enviar mensagem
    if st.button("Enviar") and user_input.strip() != "":

        st.session_state.chat_history.append(("Você", user_input))
        #st.rerun()  # Atualiza a página para mostrar nova mensagem

        historico = construir_historico(st.session_state.chat_history, user_input)
        resposta = None

        try:
            agente = agents.agente_orquestrador(user_input)
            agente = str(agente).strip()
            print(agente)
            if agente not in ("agente_conversador", "agente_buscador"):
                print("Erro no agente_orquestrador")
                agente = "agente_conversador"  # fallback para garantir que o chat continue
        except Exception as e:
            print("Erro no agente_orquestrador:", e)
            agente = "agente_conversador"  # fallback para garantir que o chat continue
        if agente == "agente_conversador":
            try:
                resposta = agents.agente_conversador(historico)
            except Exception as e:
                st.error("Não consegui conversar agora. Tente de novo mais tarde.")
                print("Erro no agente_conversador:", e)

        elif agente == "agente_buscador":
            try:
                query = agents.agente_buscador(historico)
            except Exception as e:
                st.error("Não consegui entender sua pergunta sobre compras.")
                print("Erro ao gerar query com agente_buscador:", e)
                query = None

            if query:
                try:
                    resultados = list(historico_compras.find(query))
                except Exception as e:
                    st.error("Houve um problema ao buscar no histórico de compras.")
                    print("Erro no acesso ao MongoDB:", e)
                    resultados = []

                try:
                    analise = agents.agente_analista(resultados, historico)
                    resposta = agents.agente_comunicador(analise, historico)
                except Exception as e:
                    st.error("Não consegui analisar ou comunicar os dados.")
                    print("Erro no agente_analista ou agente_comunicador:", e)

        st.session_state.chat_history.append(("s.mart.at", resposta))
        st.rerun()  # Atualiza a página para mostrar nova mensagem



    # Upload de imagem
    uploaded_file = st.file_uploader("Envie uma imagem para o chatbot:", type=["png", "jpg", "jpeg"])
    if uploaded_file:

        # Cria a pasta 'uploads' caso não exista
        upload_dir = "uploads"
        resposta = "Desculpe, não consegui carregar os dados."
        os.makedirs(upload_dir, exist_ok=True)

        # Define o caminho do arquivo para salvar
        file_path = os.path.join(upload_dir, uploaded_file.name)

        try:
            # Salva o arquivo no disco
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Arquivo salvo em {file_path}")
            st.image(file_path, caption="Imagem carregada do arquivo salvo", use_container_width=True)
        except Exception as e:
            st.error("Falha ao salvar o arquivo.")
            print("Erro ao salvar arquivo:", e)
            resposta = "Não consegui salvar o arquivo enviado. Por favor, tente novamente."
            st.session_state.chat_history.append(("s.mart.at", resposta))
            return

        try:
            st.write("s.mart.at recebeu sua imagem! Processando...")

            # Carregar bytes da imagem
            try:
                image_bytes = uploaded_file.getvalue()
            except Exception as e:
                st.error("Falha ao ler os bytes da imagem.")
                print("Erro ao obter bytes da imagem:", e)
                resposta = "Não consegui ler os dados da imagem."
                st.session_state.chat_history.append(("s.mart.at", resposta))
                return

            # Abrir a imagem com PIL
            try:
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption="Imagem carregada", use_container_width=True)
            except Exception as e:
                st.error("Falha ao abrir a imagem.")
                print("Erro ao abrir a imagem:", e)
                resposta = "A imagem enviada está corrompida ou no formato inválido."
                st.session_state.chat_history.append(("s.mart.at", resposta))
                return

            # Extrair dados da imagem
            try:
                extracao = agents.agente_leitor(file_path)
            except Exception as e:
                st.error("Falha na extração dos dados da imagem.")
                print("Erro no agente_leitor:", e)
                resposta = "Não consegui extrair informações da imagem."
                st.session_state.chat_history.append(("s.mart.at", resposta))
                return

            # Formatar extração
            try:
                itens = agents.agente_formatacao(extracao)
                if not itens or not isinstance(itens, list):
                    st.warning("Nenhum dado válido foi extraído da imagem.")
                    resposta = "Não encontrei dados válidos na imagem para processar."
                    st.session_state.chat_history.append(("s.mart.at", resposta))
                    return
            except Exception as e:
                st.error("Falha na formatação dos dados extraídos.")
                print("Erro no agente_formatacao:", e)
                resposta = "Houve um problema ao formatar os dados extraídos."
                st.session_state.chat_history.append(("s.mart.at", resposta))
                return

            # Inserir no MongoDB
            try:
                result = historico_compras.insert_many(itens)
                st.success(f"{len(result.inserted_ids)} itens inseridos no histórico de compras.")
                resposta = f"{len(result.inserted_ids)} itens foram adicionados ao seu histórico de compras."
                st.session_state.chat_history.append(("s.mart.at", resposta))
            except Exception as e:
                st.error("Falha ao inserir dados no banco.")
                print("Erro no insert_many do MongoDB:", e)
                resposta = "Não consegui salvar os dados no banco de dados."
                st.session_state.chat_history.append(("s.mart.at", resposta))
                return

        except Exception as e:
            st.error("Erro inesperado ao processar a imagem.")
            print("Erro geral no processamento da imagem:", e)
            resposta = "Ocorreu um erro inesperado durante o processamento."
            st.session_state.chat_history.append(("s.mart.at", resposta))
            return




    # Mostrar o histórico da conversa
    st.markdown("---")
    st.subheader("Histórico da conversa:")
    for speaker, message in st.session_state.chat_history:
        if speaker == "Você":
            st.markdown(f"**Você:** {message}")
        else:
            st.markdown(f"**{speaker}:** {message}")

if __name__ == "__main__":
    main()
