import streamlit as st
import tensorflow as tf
import numpy as np
import cv2

IMG_SIZE = 64

# Load model
model = tf.keras.models.load_model("eye_open_close_cnn.h5")

st.title("👁️ Eye Open / Closed Detection")
st.write("Upload an eye image to classify whether the eye is OPEN or CLOSED.")

uploaded = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded:
    file_bytes = np.frombuffer(uploaded.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Preprocess
    img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE)) / 255.0
    img_input = np.expand_dims(img_resized, axis=0)

    pred = model.predict(img_input)[0][0]
    label = "OPEN 👁️" if pred > 0.5 else "CLOSED 😴"

    st.image(img, channels="BGR")
    st.subheader(f"Prediction: **{label}**")
