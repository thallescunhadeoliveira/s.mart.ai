import streamlit as st
from PIL import Image
import io
from models.agents import Agents
from db import historico_compras
from utils.utils import construir_historico

# # Função simples para responder ao usuário (exemplo)
# def chatbot_response(user_input):
#     # Aqui você pode colocar lógica real ou conectar com um modelo de IA
#     return f"s.mart.at diz: Você disse '{user_input}'"

agents = Agents()

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
        st.session_state.chat_history.append(("s.mart.at", resposta))
        st.experimental_rerun()  # Atualiza a página para mostrar nova mensagem

        historico = construir_historico(st.session_state.chat_history, user_input)

        try:
            agente = agents.agente_orquestrador(user_input)
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



    # Upload de imagem
    uploaded_file = st.file_uploader("Envie uma imagem para o chatbot:", type=["png", "jpg", "jpeg"])
    if uploaded_file:

        try:
            st.image(uploaded_file, caption="Imagem enviada", use_column_width=True)
            st.write("s.mart.at recebeu sua imagem! Processando...")

            # Carregar imagem a partir do arquivo enviado
            image_bytes = uploaded_file.getvalue()
            image = Image.open(io.BytesIO(image_bytes))

            st.image(image, caption="Imagem carregada", use_column_width=True)

            # Extrair dados da imagem
            extracao = agents.agente_leitor(image)

            # Formatar a extração para lista de dicionários
            itens = agents.agente_formatacao(extracao)

            if not itens or not isinstance(itens, list):
                st.warning("Nenhum dado válido foi extraído da imagem.")
                return

            # Inserir itens no MongoDB (coleção historico_compras)
            # Use insert_many para inserir múltiplos documentos
            result = historico_compras.insert_many(itens)
            st.success(f"{len(result.inserted_ids)} itens inseridos no histórico de compras.")

        except Exception as e:
            st.error("Ocorreu um erro ao processar a imagem.")
            print("Erro no processamento da imagem:", e)


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
