import os
import streamlit as st

from src.sidebar import get_llm_and_sidebar
from dotenv import load_dotenv

load_dotenv()

def main():
    # Initialize the LLM with sidebar configuration
    llm = get_llm_and_sidebar(ollama_url=os.getenv("OLLAMA_HOST", ""))

    # Title and session state initialization
    st.title("My Local GPT with Ollama")

    reset_chat_button = st.sidebar.button("Reset chat", key="reset_chat_button")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if reset_chat_button:
         st.session_state.messages = []

    # Display past messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input handling
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner(f"Thinking..."):
                # Stream the assistant's response
                stream = llm.stream(
                    input=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ]
                )
                response = st.write_stream(stream)

        # Store the assistant's response
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()