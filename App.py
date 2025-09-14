import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

st.title("🌱 Agri AI App")

# Load your model (ensure the model file is in your repo)
try:
    model = load_model("your_model.h5")
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Could not load model: {e}")

# Upload an image for prediction
uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image for model
    img_array = image.resize((224, 224))  # adjust size based on your model
    img_array = np.array(img_array) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    try:
        prediction = model.predict(img_array)
        st.write(f"Prediction: {prediction}")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")