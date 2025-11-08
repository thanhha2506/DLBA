import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="🍋 FruitVision Detector", layout="centered")
st.title("🍋 FruitVision – Fruit Defect & Ripeness Detection")

st.write("Upload an image of a fruit, and let our models do the magic!")

uploaded_file = st.file_uploader("📸 Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Hiển thị ảnh preview
    img = Image.open(uploaded_file)
    st.image(img, caption="Your uploaded image", use_column_width=True)

    if st.button("🔍 Run Prediction"):
        # Gửi ảnh tới FastAPI backend
        backend_url = "http://127.0.0.1:8080/predict"
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}

        with st.spinner("Detecting... please wait ⏳"):
            response = requests.post(backend_url, files=files)

        if response.status_code == 200:
            result = response.json()["result"]
            st.success("Detection completed!")
            st.json(result)
        else:
            st.error(f"Error {response.status_code}: {response.text}")
