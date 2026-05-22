import streamlit as st
import google.generativeai as genai

# 1. NAYI API KEY YAHAN DALEIN
API_KEY = "AIzaSyD7sOKbKkDyMt2AF58c_vFwieylBE0b2Sw"

# 2. Setup (Force Latest)
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Magic Teddy", page_icon="🧸")
st.title("🧸 Magic Teddy Talks")

user_input = st.text_input("Teddy se baat karein:", placeholder="Kuch likhen...")

if st.button("Poocho ✨"):
    if user_input:
        with st.spinner("Teddy soch raha hai..."):
            try:
                # Hum model ka naam bilkul simple rakhenge
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(user_input)
                st.success(f"Teddy 🧸: {response.text}")
            except Exception as e:
                # Agar error aaye to hum 'gemini-1.5-pro' try karenge
                try:
                    model = genai.GenerativeModel('gemini-1.5-pro')
                    response = model.generate_content(user_input)
                    st.success(f"Teddy 🧸: {response.text}")
                except Exception as e2:
                    st.error(f"Abhi bhi masla hai: {e2}")
    else:
        st.warning("Pehle kuch likhen!")
