import numpy as np
import tensorflow as tf
from PIL import Image
import streamlit as st

st.title("Age Prediction")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("age_prediction_model.keras")


model = load_model()

def predict(img):
    img = img.convert("RGB").resize((64, 64))
    x = np.array(img) / 255.0
    x = x.reshape(1, 64, 64, 3)
    return float(model.predict(x, verbose=0)[0][0])

tab1, tab2 = st.tabs(["Upload", "Webcam"])

with tab1:
    f = st.file_uploader("Upload a face image", type=["jpg", "jpeg", "png"],accept_multiple_files=False)
    if f:
        img = Image.open(f)
        st.image(img, width=250)
        if st.button("Predict", key="upload_predict"):
            st.success(f"Predicted age: {predict(img):.0f} years")

with tab2:
    use_cam = st.checkbox("Open camera")
    if use_cam:
        cam = st.camera_input("Take a photo")
        if cam:
            img = Image.open(cam)
            if st.button("Predict", key="cam_predict"):
                st.success(f"Predicted age: {predict(img):.0f} years")