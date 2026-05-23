import streamlit as st
import google.generativeai as genai

# 1. Nayi API Key yahan dalein
API_KEY = "AIzaSyAwufb1rEiQCW5kykhOa3SpHQbicLvw2SI"

# 2. Setup
genai.configure(api_key=API_KEY, transport='rest')

st.set_page_config(page_title="Magic Teddy", page_icon="🧸")
st.title("🧸 Magic Teddy")

# Model ko button se bahar define kar diya taake 'NameError' na aaye
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input("Teddy se baat karein:", placeholder="Hi Teddy!")

if st.button("Poocho ✨"):
    if user_input:
        with st.spinner("Teddy soch raha hai..."):
            try:
                # Seedha response generate karein
                response = model.generate_content(user_input)
                st.success(f"Teddy: {response.text}")
            except Exception as e:
                st.error(f"Oho! Masla hai: {e}")
    else:
        st.warning("Kuch likhen!")
