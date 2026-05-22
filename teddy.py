import streamlit as st
import google.generativeai as genai

# 🔥 1. BILKUL NAYI KEY YAHAN DALEIN
API_KEY = "AIzaSyD4uxYA_UC9apPycCTdgPMZGXYkxVsgGWc"

# 🔥 2. ZABARDASTI VERSION SET KARNA
genai.configure(api_key=API_KEY)

st.title("🧸 Teddy is BACK!")

user_input = st.text_input("Kuch likhen:")

if st.button("Talk"):
    try:
        # Hum sirf 'gemini-1.5-flash' likhenge, Google khud version sambhal lega
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(f"Error detail: {e}")
