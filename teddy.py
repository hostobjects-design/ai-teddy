import streamlit as st
import requests

# 1. Nayi API Key yahan dalein
API_KEY = "AIzaSyCWudDDz96djZViqkTj8skhdeMNYLyITVc"

st.set_page_config(page_title="Magic Teddy", page_icon="🧸")
st.title("🧸 Magic Teddy")

user_input = st.text_input("Teddy se baat karein:", placeholder="Hi Teddy!")

if st.button("Poocho ✨"):
    if user_input:
        with st.spinner("Teddy soch raha hai..."):
            # Direct API URL (Force Version v1)
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
            
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{"parts": [{"text": f"Talk like a cute teddy bear in Urdu: {user_input}"}]}]
            }
            
            try:
                response = requests.post(url, headers=headers, json=data)
                result = response.json()
                
                # Jawab nikaalna
                answer = result['candidates'][0]['content']['parts'][0]['text']
                st.success(f"Teddy: {answer}")
            except Exception as e:
                st.error("Oho! Teddy ko signal nahi mil raha. Key check karein!")
    else:
        st.warning("Kuch likhen!")
