import streamlit as st
from PIL import Image
from model import load_captioning_model, generate_caption

# Load model, processor, and tokenizer
@st.cache_resource
def load_model():
    return load_captioning_model()

model, processor, tokenizer = load_model()

# Streamlit App
st.title("AI Image Caption Generator")
st.write("Upload an image, and let the AI describe it for you!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Generate caption
    with st.spinner("Generating caption..."):
        caption = generate_caption(image, model, processor, tokenizer)
    st.success("Caption Generated!")
    st.write(f"**Caption:** {caption}")
