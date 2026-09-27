import streamlit as st
import numpy as np
import cv2
import tempfile
import os

from image_processing import process_image
from segmentation import segment_colors
from analysis import analyze_plant_health

st.set_page_config(page_title="Plant Doctor 🌱", layout="wide")
st.title("🌱 Plant Doctor — Leaf Health Analyzer")
st.write("Upload a leaf image, or try one of the sample leaves, to check for signs of stress (yellowing/browning).")

# --- Image source selection ---
SAMPLE_IMAGES = {
    "None": None,
    "Healthy Leaf": "images/healthy_leaf.jpg",
    "Yellow Leaf": "images/yellow_leaf.jpg",
    "Brown Leaf": "images/brown_leaf.jpg",
}

col_a, col_b = st.columns(2)

with col_a:
    sample_choice = st.selectbox("Try a sample image", list(SAMPLE_IMAGES.keys()))

with col_b:
    uploaded_file = st.file_uploader("...or upload your own", type=["jpg", "jpeg", "png"])

# --- Decide which image path to use ---
image_path = None
cleanup_needed = False

if uploaded_file is not None:
    # Uploaded file takes priority over sample selection
    suffix = os.path.splitext(uploaded_file.name)[1]
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    tmp_file.write(uploaded_file.read())
    tmp_file.close()
    image_path = tmp_file.name
    cleanup_needed = True
elif SAMPLE_IMAGES[sample_choice] is not None:
    image_path = SAMPLE_IMAGES[sample_choice]

# --- Run the pipeline ---
if image_path is not None:
    try:
        # 1. Debasmita's module: image -> RGB + HSV
        processed = process_image(image_path)
        rgb_img = processed["rgb"]
        hsv_img = processed["hsv"]

        # 2. Adrija's module: HSV -> masks
        green_mask, yellow_mask, brown_mask = segment_colors(hsv_img)

        # 3. Rishika's module: masks -> analysis
        results = analyze_plant_health(rgb_img, green_mask, yellow_mask, brown_mask)

        # --- Display ---
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Leaf")
            st.image(rgb_img, use_container_width=True)
        with col2:
            st.subheader("Detected Problem Areas")
            st.image(results["highlighted_image"], use_container_width=True)

        st.subheader("📊 Color Breakdown")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("🟢 Green", f"{results['green_percentage']}%")
        c2.metric("🟡 Yellow", f"{results['yellow_percentage']}%")
        c3.metric("🟤 Brown", f"{results['brown_percentage']}%")
        c4.metric("⚠️ Affected", f"{results['affected_percentage']}%")

        st.subheader("🩺 Diagnosis")
        st.info(results["observation"])

    finally:
        if cleanup_needed:
            os.remove(image_path)  # clean up temp file from upload
else:
    st.info("👆 Pick a sample image or upload your own to get started.")