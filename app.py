import streamlit as st
import os
from dotenv import load_dotenv
from agent import run_research

# Load environment variables
load_dotenv()

# Configure the Streamlit page
st.set_page_config(page_title="Research Agent", page_icon="🔍", layout="centered")

st.title("🔍 Research Agent")
st.markdown("Powered by LangChain, Groq (Llama 3.1 8b), and Tavily Search")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    st.write("Enter your API keys below to start using the research agent.")
    
    groq_api_key = st.text_input("Groq API Key", type="password", value=os.getenv("GROQ_API_KEY", ""))
    tavily_api_key = st.text_input("Tavily API Key", type="password", value=os.getenv("TAVILY_API_KEY", ""))
    
    # Set the keys in the environment so the agent can pick them up
    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key
    if tavily_api_key:
        os.environ["TAVILY_API_KEY"] = tavily_api_key

    st.markdown("---")
    st.markdown("[Get a Groq API Key](https://console.groq.com/keys)")
    st.markdown("[Get a Tavily API Key](https://app.tavily.com/home)")

# Main chat interface
if not os.getenv("GROQ_API_KEY") or not os.getenv("TAVILY_API_KEY"):
    st.warning("⚠️ Please provide both Groq and Tavily API keys in the sidebar to continue.")
else:
    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What would you like to research?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            with st.spinner("Researching..."):
                try:
                    response = run_research(prompt)
                    st.markdown(response)
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
