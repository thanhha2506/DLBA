import streamlit as st
import asyncio
from components import render_header, render_upload_images, render_footer
from api import predict_image
from message import display_results

# --- Page Config ---
st.set_page_config(
    page_title="Fruit Detection",
    page_icon="🍎",
    layout="centered"
)

# --- Load CSS ---
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ CSS file not found. Using default Streamlit style.")

load_css("style.css")

# --- UI Layout ---
render_header()
image_file = render_upload_images()

if image_file:
    st.image(image_file, caption="Uploaded Image", use_container_width=True)

    # Nút dự đoán
    if st.button("🔍 Predict"):
        with st.spinner("🧠 Running model... Please wait."):
            try:
                result = asyncio.run(predict_image(image_file))
                display_results(result)
            except Exception as e:
                st.error(f" Error: {e}")

render_footer()
