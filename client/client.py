import base64
import requests
from PIL import Image
from io import BytesIO
import os

API_URL = "http://localhost:8000/predict"  # adjust if running remotely

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as f:
        image_bytes = f.read()
        return base64.b64encode(image_bytes).decode("utf-8")

def send_prediction_request(image_base64):
    payload = {"image_base64": image_base64}
    response = requests.post(API_URL, json=payload)
    return response.json()

def main():
    image_folder = "test_images"  # a folder with .png or .jpg files
    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            path = os.path.join(image_folder, filename)
            print(f"🔍 Predicting for: {filename}")
            image_b64 = encode_image_to_base64(path)
            result = send_prediction_request(image_b64)
            print(f"✅ Prediction: {result['prediction']}\n")

if __name__ == "__main__":
    main()
