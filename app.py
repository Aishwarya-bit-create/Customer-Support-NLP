import streamlit as st
from predict import predict_query

st.title("Customer Support AI Bot")

query = st.text_area("Enter Customer Query")

if st.button("Submit"):
    if query:
        category, response, confidence = predict_query(query)

        st.write("Category:", category)
        st.write("Response:", response)
        st.write("Confidence:", round(confidence*100,2), "%")