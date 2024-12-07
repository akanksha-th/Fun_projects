web-app: https://imagecaptioningproject.streamlit.app/

# Image Captioning System
A simple AI-powered app that generates captions for images.

## Features
- Upload an image to get an AI-generated caption.
- Pretrained Vision-Encoder-Decoder model for out-of-the-box functionality.
- Interactive web app built with Streamlit.

## How to Use

### Run Locally
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd image_captioning
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app/main.py
   ```
4. Open your browser at `http://localhost:8501` and upload your image.

### Run with Docker
1. Build the Docker image:
   ```bash
   docker build -t image_captioning_app .
   ```
2. Run the container:
   ```bash
   docker run -p 8501:8501 image_captioning_app
   ```
3. Open your browser at `http://localhost:8501`.

## Example
1. Upload an image (e.g., a dog photo).
2. The system generates a caption like:
   ```
   Caption: A dog sitting on a couch in a living room.
   ```
