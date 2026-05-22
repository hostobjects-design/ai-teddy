import streamlit as st
from google import genai

# 🔥 APNI GOOGLE API KEY YAHAN PASTE KARO 🔥
GOOGLE_API_KEY = "AIzaSyB8Dxuf1w9L_kQEYQSPe2cpyXIW_Da-iwQ"

client = genai.Client(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="Magic Teddy Talks", page_icon="🧸")

st.markdown("<h1 style='text-align: center; color: #FFCC00;'>🧸 MAGIC TEDDY TALKS 🧸</h1>", unsafe_allow_html=True)

sawaal = st.text_input("Teddy se baatein karo...", placeholder="Yahan kuch likho...")

if st.button("Teddy Ko Btao 🗣️"):
    if sawaal:
        with st.spinner("Teddy soch raha hai..."):
            try:
                prompt = f"You are a friendly Teddy Bear. Reply in Urdu/Roman Urdu: {sawaal}"
                response = client.models.generate_content(model='gemini-2.0-flash', contents=prompt)
                st.success(f"Teddy 🧸: {response.text}")
            except Exception as e:
                st.error("API Key ka masla hai!")
