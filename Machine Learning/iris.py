import streamlit as st
import joblib
import numpy as np
from sklearn.datasets import load_iris

# Load saved model and scaler
model = joblib.load('svm_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load Iris dataset info
iris = load_iris()
class_names = iris.target_names

# Streamlit App UI
st.title("🌸 Iris Flower Prediction using SVM")
st.write("Enter the measurements below to predict the Iris flower species.")

# Sidebar info
st.sidebar.header("📘 About the Project")
st.sidebar.info(
    "This app uses a Support Vector Machine (SVM) model trained on the Iris dataset. "
    "It predicts whether the flower is Setosa, Versicolor, or Virginica."
)
st.sidebar.write("🌼 Make your prediction below!")

# User input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)

# Prediction
if st.button("🔍 Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    st.success(f"🌺 Predicted Iris Species: **{class_names[prediction].capitalize()}**")
