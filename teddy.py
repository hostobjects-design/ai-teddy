import streamlit as st
import google.generativeai as genai
import os

# 1. API KEY
API_KEY = "AIzaSyAYOyor9kZgffny4hKahYqn1S9lQyTLJ_I"

# 🔥 YE LINE VERSION KA MASLA KHATAM KAR DEGI
os.environ["GOOGLE_API_USE_MTLS"] = "never" 

genai.configure(api_key=API_KEY)

st.title("🧸 Teddy is Online!")

user_input = st.text_input("Kuch bhi likho:")

if st.button("Talk to Teddy"):
    if user_input:
        try:
            # Hum model ka pura naam likhenge version ke saath
            model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
            response = model.generate_content(user_input)
            st.success(f"Teddy: {response.text}")
        except Exception as e:
            st.error(f"Abhi bhi masla hai: {e}")
