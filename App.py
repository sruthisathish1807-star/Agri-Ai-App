import streamlit as st
import gdown

st.title("🌱 Agri AI App (Test)")

st.write("✅ Streamlit is working!")
st.write("✅ gdown is installed!")

# Try downloading a small test file from Google Drive
file_id = "1ZdR3L2y6hU7JhH7m1v3lF-ExampleID"  # replace later with your real model file ID
output = "test.txt"

try:
    gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)
    st.success("Google Drive connection successful! Test file downloaded.")
except Exception as e:
    st.error(f"gdown failed: {e}")