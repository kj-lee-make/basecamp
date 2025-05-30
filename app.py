import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("Gemini Chatbot")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"author": "system", "content": "You are a helpful AI assistant."}
    ]

def send_message():
    user_input = st.session_state.user_input.strip()
    if not user_input:
        return
    st.session_state.messages.append({"author": "user", "content": user_input})
    with st.spinner("Generating response..."):
        response = genai.chat.completions.create(
            model="gemini-1.5-flash",
            messages=st.session_state.messages
        )
    assistant_message = response.choices[0].message.content
    st.session_state.messages.append({"author": "assistant", "content": assistant_message})
    st.session_state.user_input = ""

st.text_input("You:", key="user_input", on_change=send_message)

for msg in st.session_state.messages:
    if msg["author"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Gemini:** {msg['content']}")
