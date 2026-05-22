import streamlit as st
import google.generativeai as genai

# 1. API Key (Inverted commas ke andar)
API_KEY = "AIzaSyDpmgwJPValy-amQ8q3vh1LcP91gueJUCY"

# 2. Setup (Force Version v1)
try:
    genai.configure(api_key=API_KEY)
    # Hum specific model name use kar rahe hain jo v1 par chalta hai
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
except Exception as e:
    st.error(f"Setup Error: {e}")

# 3. Design
st.set_page_config(page_title="Magic Teddy", page_icon="🧸")
st.title("🧸 Magic Teddy Talks")

user_input = st.text_input("Teddy se baat karein:", placeholder="Kuch likhen...")

if st.button("Poocho ✨"):
    if user_input:
        with st.spinner("Teddy soch raha hai..."):
            try:
                # Direct call
                response = model.generate_content(user_input)
                st.success(f"Teddy 🧸: {response.text}")
            except Exception as e:
                # Agar phir bhi 404 aaye, to ye last option try karega
                st.error(f"Error: {e}")
                st.info("Mashwara: Google AI Studio se aik NAYI API Key bana kar try karein.")
    else:
        st.warning("Pehle kuch likhen!")
