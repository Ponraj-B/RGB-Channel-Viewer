import streamlit as st
import numpy as np
from PIL import Image

st.title("Color Channel Splitter")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert('RGB')  # Ensure it's in RGB
    img_array = np.array(img)

    st.image(img, caption="Original Image", use_column_width=True)

    # Split the channels
    red_channel = img_array.copy()
    red_channel[:, :, 1] = 0  # Remove Green
    red_channel[:, :, 2] = 0  # Remove Blue

    green_channel = img_array.copy()
    green_channel[:, :, 0] = 0  # Remove Red
    green_channel[:, :, 2] = 0  # Remove Blue

    blue_channel = img_array.copy()
    blue_channel[:, :, 0] = 0  # Remove Red
    blue_channel[:, :, 1] = 0  # Remove Green

    st.subheader("Red Channel")
    st.image(red_channel, use_column_width=True)

    st.subheader("Green Channel")
    st.image(green_channel, use_column_width=True)

    st.subheader("Blue Channel")
    st.image(blue_channel, use_column_width=True)
