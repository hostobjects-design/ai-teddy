import streamlit as st
import google.generativeai as genai

# 1. API KEY (Yahan apni nayi key paste karein)
API_KEY = "AIzaSyAytevRvUsIDOKu379dTGggr3ebm4tiygc"

# 2. Setup (Latest 2026 Configuration)
genai.configure(api_key=API_KEY)

# Design
st.set_page_config(page_title="Teddy Talk", page_icon="🧸")
st.markdown("<h1 style='color: #FF69B4;'>🧸 Magic Teddy</h1>", unsafe_allow_html=True)

user_msg = st.text_input("Teddy se baat karein...", placeholder="Hi Teddy!")

if st.button("Poocho ✨"):
    if user_msg:
        try:
            # 2026 model call
            model_name="gemini-1.5-flash"
            response = model.generate_content(f"Talk like a cute teddy bear in Urdu: {user_msg}")
            
            st.info(f"Teddy: {response.text}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Kuch likhen to sahi!")
