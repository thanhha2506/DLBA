import streamlit as st
from PIL import Image
from pathlib import Path

def render_header():
    logo_path = Path(__file__).parent / "images" / "fruits (1).png"

    if not logo_path.exists():
        st.error(f" Logo not found at: {logo_path}")
        return

    logo = Image.open(logo_path)

    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(logo, width=100)
    with col2:
        st.markdown(
            """
            <h1 style='font-size: 40px; color: #2E2E2E; text-align: left;'>
                FRUIT DETECTION & QUALITY CLASSIFICATION
            </h1>
            """,
            unsafe_allow_html=True
        )
    st.markdown("---")

def render_upload_images():
    return st.file_uploader("Choose an Image:", type=["jpg", "png"])

def render_footer():
    st.markdown(
        """
        <div class="footer">
            Developed by Group 3
        </div>
        """,
        unsafe_allow_html=True
    )
