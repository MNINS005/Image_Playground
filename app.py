import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="Image Playground ", layout="centered")

st.title(" Image Playground with OpenCV")
st.markdown("""
Upload an image and play around with classic OpenCV actions:
- Resize
- Convert to Grayscale
- Apply Blur
- Detect Edges
""")

uploaded_file = st.file_uploader("Upload your image here ", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)  # Read as BGR

    st.subheader("Original Image")
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), channels="RGB")

    # --- Resize ---
    st.subheader("Resize ")
    scale = st.slider("Scale %", 10, 200, 100)
    width = int(image.shape[1] * scale / 100)
    height = int(image.shape[0] * scale / 100)
    resized = cv2.resize(image, (width, height))
    st.image(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB), channels="RGB", caption=f"Resized to {scale}%")

    # --- Grayscale ---
    st.subheader("Grayscale ")
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    st.image(gray, channels="GRAY")

    # --- Blur ---
    st.subheader("Blur ")
    blur_strength = st.slider("Kernel size for blur", 1, 49, 9, step=2)
    blurred = cv2.GaussianBlur(resized, (blur_strength, blur_strength), 0)
    st.image(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB), channels="RGB")

    # --- Edge detection ---
    st.subheader("Edge Detection ")
    threshold1 = st.slider("Threshold 1", 0, 500, 100)
    threshold2 = st.slider("Threshold 2", 0, 500, 200)
    edges = cv2.Canny(resized, threshold1, threshold2)
    st.image(edges, channels="GRAY")
else:
    st.info(" Upload an image to start playing with OpenCV magic!")

