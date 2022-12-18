import streamlit as st
import numpy as np
import pickle
import pandas as pd

pickle_in = open("Classifier.pk1", "rb")
Classifier = pickle.load(pickle_in)
def predict_flower(sep_len, sep_wid, pet_len, pet_wid):
    prediction = Classifier.predict([[sep_len, sep_wid, pet_len, pet_wid]])
    return prediction
def main():
    st.title("Iris flower species predictor")
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-color : pink
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    pet_len = st.number_input("Petal length", min_value= 1.0, max_value= 6.9, step= 0.1, label_visibility="visible")
    pet_wid = st.number_input("Petal width", min_value= 0.1, max_value= 2.5, step= 0.1, label_visibility="visible")
    sep_len = st.number_input("Sepal length", min_value= 4.3, max_value= 7.9, step= 0.1, label_visibility="visible")
    sep_wid = st.number_input("Sepal width", min_value= 2.0, max_value= 4.4, step= 0.1, label_visibility="visible")

    result = ""
    if st.button("Predict"):
        result= predict_flower(sep_len, sep_wid, pet_len, pet_wid)
    st.success('This flower is {}'.format(str(result)))
if __name__ == '__main__':
    main()