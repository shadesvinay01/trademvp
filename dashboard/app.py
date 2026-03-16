import streamlit as st
from models.sentiment import SentimentAnalyzer

st.title("Sharp Trading AI")

text = st.text_area("Enter tweet")

model = SentimentAnalyzer()

if st.button("Analyze"):

    result = model.ensemble(text)

    st.write("Sentiment:", result)
