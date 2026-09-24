import streamlit as st
import google.generativeai as genai
 
# Configure Gemini API Key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
 
# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")
 
# App UI
st.header("🐦 Tweet Generator 🐦")
st.subheader("Generate tweets using Gemini AI")
 
topic = st.text_input("Topic")
 
number = st.number_input(
"Number of tweets",
min_value=1,
max_value=10,
value=1,
step=1
)
 
if st.button("Generate"):
prompt = f"Give me {number} engaging tweets about {topic}"
 
response = model.generate_content(prompt)
 
st.write(response.text)
