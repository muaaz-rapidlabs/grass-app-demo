import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

def detect_grass(image):
    # Convert to OpenCV format
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image_hsv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2HSV)

    # Define green range
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    # Create mask for green areas
    mask = cv2.inRange(image_hsv, lower_green, upper_green)

    # Highlight green areas in original image
    highlighted = np.array(image).copy()
    highlighted[mask > 0] = [0, 255, 0]

    # Optional: Draw bounding boxes
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxed = highlighted.copy()
    for cnt in contours:
        if cv2.contourArea(cnt) > 50:  # filter noise
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(boxed, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Calculate green percentage
    green_pixels = np.sum(mask > 0)
    total_pixels = mask.shape[0] * mask.shape[1]
    green_percent = (green_pixels / total_pixels) * 100

    return boxed, green_percent

# Streamlit UI
st.title("Grass Detection in Beetroot Load")
st.write("Upload an image to detect grass patches and estimate green coverage.")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Original Image', use_container_width=True)

    result_img, percent = detect_grass(image)

    st.image(result_img, caption=f"Detected Grass: {percent:.2f}%", use_container_width=True)
    st.success(f"Grass Coverage: {percent:.2f}%")

    # Download button
    result_pil = Image.fromarray(result_img)
    buf = io.BytesIO()
    result_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download Highlighted Image",
        data=byte_im,
        file_name="highlighted_grass.png",
        mime="image/png"
    )
