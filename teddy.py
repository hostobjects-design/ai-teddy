import streamlit as st
import google.generativeai as genai

# 🔥 1. APNI KEY YAHAN DALEIN
API_KEY = "AIzaSyCQXGzVOl5TcM7uYkdq2WCEOUV2gCbF_SM"

# 2. Setup
try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error(f"Configuration Error: {e}")

# 3. Website Design
st.set_page_config(page_title="Magic Teddy", page_icon="🧸")
st.title("🧸 Magic Teddy Talks")
st.write("Main ek jaaduai Teddy hoon! Mujhse Urdu mein baatein karo.")

# 4. Input
user_input = st.text_input("Teddy se kuch poocho:", placeholder="Yahan likhein...")

if st.button("Teddy se Poocho ✨"):
    if user_input:
        with st.spinner("Teddy soch raha hai..."):
            try:
                # 🛑 HUMNE YAHAN 'gemini-1.5-flash-latest' ISTEMAL KIYA HAI
                model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
                response = model.generate_content(f"Talk like a cute teddy bear in Urdu/Roman Urdu: {user_input}")
                st.success(f"Teddy: {response.text}")
            except Exception as e:
                # Agar phir bhi masla aaye to ye error dikhayega
                st.error(f"Teddy thak gaya hai. Masla: {e}")
    else:
        st.warning("Pehle kuch likho to sahi!")
