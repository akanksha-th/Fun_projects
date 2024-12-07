from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import torch

# Load the pretrained image captioning model
def load_captioning_model():
    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    return model, processor, tokenizer

# Generate captions for the uploaded image
def generate_caption(image, model, processor, tokenizer, max_length=16):
    # Preprocess the image
    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    # Generate captions
    with torch.no_grad():
        output_ids = model.generate(pixel_values, max_length=max_length, num_return_sequences=1)

    # Decode the output to a caption
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()
    return caption
