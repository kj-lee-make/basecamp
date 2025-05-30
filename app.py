import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("Gemini Chatbot")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def send_message():
    user_input = st.session_state.user_input.strip()
    if not user_input:
        return

    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(history=st.session_state.chat_history)

    with st.spinner("Generating response..."):
        response = chat.send_message(user_input)

    st.session_state.chat_history.extend([
        {"role": "user", "parts": [user_input]},
        {"role": "model", "parts": [response.text]}
    ])
    st.session_state.user_input = ""

st.text_input("You:", key="user_input", on_change=send_message)

for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['parts'][0]}")
    elif message["role"] == "model":
        st.markdown(f"**Gemini:** {message['parts'][0]}")
