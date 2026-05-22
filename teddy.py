import streamlit as st
import google.generativeai as genai

# 🔥 1. APNI KEY YAHAN DALEIN
API_KEY = "AIzaSyD8xqVMekksePqJXciCXsXe0L91bn6HvP0"

# 2. Setup
genai.configure(api_key=API_KEY)

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
                # Model setup aur response
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Talk like a cute teddy bear in Urdu/Roman Urdu: {user_input}")
                st.success(f"Teddy: {response.text}")
            except Exception as e:
                st.error(f"Oho! Masla agaya hai: {e}")
    else:
        st.warning("Pehle kuch likho to sahi!")
