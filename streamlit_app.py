# Lenny the LaborBot - Streamlit-Ready Sarcastic AI Using Groq
# Requirements: pip install streamlit requests

import streamlit as st
import requests

# Streamlit App Config
st.set_page_config(page_title="Lenny the LaborBot 🤠", page_icon="🛠️", layout="centered")

# Custom UI Theme
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #1E1E1E;
        color: #F2F2F2;
        font-family: 'Courier New', monospace;
    }
    .stButton>button {
        background-color: #F29F05;
        color: black;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stTextArea textarea {
        background-color: #2B2B2B;
        color: #F2F2F2;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# App Title & Intro
st.title("🛠️ Lenny the LaborBot")
st.subheader("Your sarcastic AI pal who's had one too many coffees and zero patience for nonsense.")
st.markdown("""
Lenny's the kinda guy who'll tell you the engine's busted *and* that it's your fault. Ask him anything — just don’t expect him to sugarcoat the answers.
""")

# User Prompt
prompt = st.text_area("💬 What's on your mind, hotshot?", "Why is the sky blue?")

# Submit Button
if st.button("🗣️ Ask Lenny"):
    if not st.secrets.get("GROQ_API_KEY"):
        st.error("❌ GROQ API key not found. Add it to your Streamlit secrets.")
    else:
        headers = {
            "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": "You're Lenny the LaborBot, a sarcastic, blue-collar jokester AI who sounds like a grumpy truck mechanic. Give direct, witty, blunt responses with some dry humor."},
                {"role": "user", "content": prompt}
            ]
        }
        try:
            response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
            response.raise_for_status()
            reply = response.json()["choices"][0]["message"]["content"]
            st.markdown(f"**🧰 Lenny:** {reply}")
        except requests.exceptions.RequestException as e:
            st.error(f"🤖 API error: {e}")
