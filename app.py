# app.py
import streamlit as st

st.title("🧠 Core Image Classifier (Demo)")
st.write("Upload a core image to test CNN classification.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.success("Pretend we're running a CNN here...")
