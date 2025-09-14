import os
import gdown
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

# Download model from Google Drive (replace with your file ID)
file_id="17X_Z5NKE_7avFX9l_qlHeSupeGWw4Hk1"
output = "crop_disease_model.h5"
gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)

# Load model
model = load_model(output)

# Labels (change as per your dataset)
class_labels = ["Tomato Healthy", "Tomato Early Blight", "Tomato Late Blight"]

st.title("🌱 Crop Disease Detector")
st.write("Upload a leaf image and check if it's healthy or diseased.")

# Upload file
uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Leaf", use_column_width=True)

    # Preprocess image
    img = img.resize((128, 128))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)

    st.success(f"Prediction: {class_labels[class_idx]}")
