# app_streamlit.py
import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Iris Classifier", page_icon="🌸")

st.title("🌸 Iris Flower Classifier")
st.write("Enter the flower features below and click **Predict** to see its species.")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width  = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width  = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

if st.button("🔍 Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    pred = model.predict(features)[0]
    st.success(f"Predicted class: **{pred}**")

st.markdown("---")
st.caption("Built with Streamlit + scikit-learn • demo mode")
