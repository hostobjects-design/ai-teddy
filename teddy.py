import streamlit as st
import google.generativeai as genai

# 🔥 APNI GOOGLE API KEY YAHAN PASTE KARO 🔥
GOOGLE_API_KEY = "AIzaSyBSjLKR0cjpxHvXQLBPLnaXJtGcIR9u_h4"

genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="Magic Teddy Talks", page_icon="🧸")

st.markdown("<h1 style='text-align: center; color: #FFCC00;'>🧸 MAGIC TEDDY TALKS 🧸</h1>", unsafe_allow_html=True)

sawaal = st.text_input("Teddy se baatein karo...", placeholder="Yahan kuch likho...")

if st.button("Teddy Ko Btao 🗣️"):
    if sawaal:
        with st.spinner("Teddy soch raha hai..."):
            try:
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(f"You are a friendly Teddy Bear. Reply in Urdu/Roman Urdu: {sawaal}")
                st.success(f"Teddy 🧸: {response.text}")
            except Exception as e:
                st.error("API Key ka masla hai ya internet slow hai!")
