import streamlit as st
import numpy as np
from PIL import Image

# Title
st.title("🔍 RGB Peek: Visualize Image Color Layers")
st.write("Upload an image and explore its individual Red, Green, and Blue channels.")

# File uploader
uploaded_file = st.file_uploader("📁 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open image and convert to RGB
    img = Image.open(uploaded_file).convert('RGB')
    img_array = np.array(img)

    # Show original image
    st.image(img, caption="🖼️ Original Image", use_column_width=True)

    # Create red channel
    red_channel = img_array.copy()
    red_channel[:, :, 1] = 0  # Remove Green
    red_channel[:, :, 2] = 0  # Remove Blue

    # Create green channel
    green_channel = img_array.copy()
    green_channel[:, :, 0] = 0  # Remove Red
    green_channel[:, :, 2] = 0  # Remove Blue

    # Create blue channel
    blue_channel = img_array.copy()
    blue_channel[:, :, 0] = 0  # Remove Red
    blue_channel[:, :, 1] = 0  # Remove Green

    # Show the three channels
    st.subheader("🔴 Red Channel")
    st.image(red_channel, use_column_width=True)

    st.subheader("🟢 Green Channel")
    st.image(green_channel, use_column_width=True)

    st.subheader("🔵 Blue Channel")
    st.image(blue_channel, use_column_width=True)

# Contact section
st.markdown("---")
st.markdown("### 📬 Contact")
st.markdown(
    """
    **Name:** Your Name  
    **Email:** [ponraj322002@gmail.com](mailto:your.email@example.com)  
    **GitHub:** [https://github.com/Ponraj-B](https://github.com/yourusername)  
    **LinkedIn:** [https://in.linkedin.com/in/ponraj-b-96a917264](https://linkedin.com/in/yourprofile)
    """
)
