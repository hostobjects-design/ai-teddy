import streamlit as st
import google.generativeai as genai

# 1. API Key Yahan Dalein
API_KEY = "AIzaSyA_aap_ki_asli_key_yahan"

# 2. Setup
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. Website Design
st.set_page_config(page_title="Magic Teddy", page_icon="🧸")
st.title("🧸 Magic Teddy Talks")
st.write("Main ek jaaduai Teddy hoon! Mujhse kuch bhi poocho.")

# 4. Input aur Output
user_input = st.text_input("Aapka Sawal:", placeholder="Yahan likhein...")

if st.button("Teddy se Poocho ✨"):
    if user_input:
        with st.spinner("Teddy soch raha hai..."):
            try:
                response = model.generate_content(f"Talk like a cute teddy bear in Urdu/Roman Urdu: {user_input}")
                st.success(f"Teddy: {response.text}")
            except Exception as e:
                st.error("Oho! Teddy thak gaya hai. Shayad API Key ka masla hai.")
    else:
        st.warning("Pehle kuch likho to sahi!")
