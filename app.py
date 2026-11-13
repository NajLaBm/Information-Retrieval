
import streamlit as st
from src.helper import (
    get_pdf_text,
    get_text_chunks,
    get_vector_store,
    get_conversational_chain,
)


def user_input(user_question):
    conversation = st.session_state.get("conversation")

    if conversation is None:
        st.warning("Veuillez d'abord importer et traiter vos fichiers PDF dans le menu.")
        return

    response = conversation.invoke({"question": user_question})
    st.session_state.chatHistory = response["chat_history"]

    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write("User:", message.content)
        else:
            st.write("Reply:", message.content)


def main():
    st.set_page_config(page_title="Information Retrieval")
    st.header("Information Retrieval System 💁")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader(
            "Upload your PDF Files and Click on the Submit & Process Button",
            type=["pdf"],
            accept_multiple_files=True,
        )

        if st.button("Submit & Process"):
            if not pdf_docs:
                st.warning("Veuillez importer au moins un fichier PDF.")
            else:
                try:
                    with st.spinner("Processing..."):
                        raw_text = get_pdf_text(pdf_docs)
                        if not raw_text.strip():
                            st.error("Aucun texte n'a été extrait des PDF.")
                        else:
                            text_chunks = get_text_chunks(raw_text)
                            vector_store = get_vector_store(text_chunks)
                            st.session_state.conversation = (
                                get_conversational_chain(vector_store)
                            )
                            st.session_state.chatHistory = None
                            st.success("PDF traités avec succès ! Vous pouvez poser vos questions.")
                except Exception as e:
                    st.error(f"Erreur pendant le traitement : {e}")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)


if __name__ == "__main__":
    main()
