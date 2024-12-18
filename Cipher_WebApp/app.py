import streamlit as st
from PIL import Image
import os
import base64

# Set page layout
st.set_page_config(layout="wide")

# Function to set background
def set_background(image_file):
    with open(image_file, "rb") as file:
        img_data = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{img_data}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Set your background
set_background("Cipher_WebApp/violet-evergarden-violets-letter-to-major-gilbert.jpg")


st.title("Violet Evergarden Cipher Web App")
st.write("Convert your text into the alphabet used in the Violet Evergarden anime.")

# Load alphabet images
def load_alphabet_images(folder_path):
    alphabet_images = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        file_path = os.path.join(folder_path, f"{letter}.png")
        if os.path.exists(file_path):
            alphabet_images[letter] = Image.open(file_path)
        else:
            print(f"Warning: {letter}.png not found!")
    for letter in "abcdefghijklmnopqrstuvwxyz":
        file_path = os.path.join(folder_path, f"{letter*2}.png")
        if os.path.exists(file_path):
            alphabet_images[letter] = Image.open(file_path)
        else:
            print(f"Warning: {letter}.png not found!")
    for letter in " ":
        file_path = os.path.join(folder_path, "space.png")
        if os.path.exists(file_path):
            alphabet_images[letter] = Image.open(file_path)
        else:
            print(f"Warning: {letter}.png not found!")
    return alphabet_images

alphabet_images = load_alphabet_images("Cipher_WebApp/violet_alphabet/")


def text_to_cipher_image(input_text, alphabet_images, output_path="output.png"):
    #input_text = input_text.upper()  # Converting all letters to upper-case because of lack of complete knowledge of the lower-case alphabets
    images = [alphabet_images[letter] for letter in input_text if letter in alphabet_images]

    # Concatenate images horizontally
    total_width = sum(img.width for img in images)
    max_height = max(img.height for img in images)
    result_image = Image.new("RGBA", (total_width, max_height), (255, 255, 255, 0))

    x_offset = 0
    for img in images:
        result_image.paste(img, (x_offset, 0), img)
        x_offset += img.width

    result_image.save(output_path)
    print(f"Cipher saved as {output_path}")
    return result_image

# Text Input Section
st.header("Type Text to Cipher")
user_text = st.text_input("Enter your text here:")
if user_text:
    result_image = text_to_cipher_image(user_text, alphabet_images)
    st.image(result_image, caption="Cipher Output")


