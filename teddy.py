import streamlit as st
import google.generativeai as genai

# 1. APNI KEY YAHAN DALEIN
API_KEY = "AIzaSyB8mG9_5XVEyGmSVvP8UR15WEXoGRdGLk8"

# 2. Setup
genai.configure(api_key=API_KEY)

# 3. Website Design
st.set_page_config(page_title="Magic Teddy", page_icon="🧸")
st.title("🧸 Magic Teddy Talks")
st.write("Main ek jaaduai Teddy hoon! Mujhse baatein karo.")

# 4. Input
user_input = st.text_input("Teddy se kuch poocho:", placeholder="Yahan likhein...")

if st.button("Teddy se Poocho ✨"):
    if user_input:
        with st.spinner("Teddy soch raha hai..."):
            try:
                # Is baar hum simple 'gemini-1.5-flash' use karenge bina kisi extra path ke
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(user_input)
                st.success(f"Teddy: {response.text}")
            except Exception as e:
                # Agar phir bhi masla ho, to hum doosra model try karenge automatically
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(user_input)
                    st.success(f"Teddy (Backup): {response.text}")
                except Exception as e2:
                    st.error(f"Oho! Dono models nahi chale. Error: {e2}")
    else:
        st.warning("Pehle kuch likho to sahi!")
