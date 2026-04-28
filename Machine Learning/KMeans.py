import streamlit as st
import numpy as np
from sklearn.cluster import KMeans

st.set_page_config(page_title="Revathy ML App", layout="centered")

st.write("KMeans Clustering Demo")

st.subheader("Enter Values")

x = st.number_input("Enter value X")
y = st.number_input("Enter value Y")

if st.button("Predict Cluster"):
   
    data = np.array([[1,2],[2,3],[3,4],[8,9],[9,10],[10,11]])
    
    model = KMeans(n_clusters=2, random_state=0)
    model.fit(data)
    
    result = model.predict([[x, y]])
    
    st.success(f"Cluster: {result[0]}")

st.write("---")
st.write("Made with ❤️ using Streamlit")