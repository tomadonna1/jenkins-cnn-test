from fastapi import FastAPI
from pydantic import BaseModel
from io import BytesIO
from PIL import Image
import base64
import torch
import torchvision.transforms as transforms
from lenet import LeNet5

app = FastAPI()

# Load model
model = LeNet5(input_channels=1, input_height=28, input_width=28, num_classes=10)
model.load_state_dict(torch.load("models/model.pt", map_location=torch.device("cpu")))
model.eval()

# Transform for MNIST-style input
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

class PredictRequest(BaseModel):
    image_base64: str

@app.post("/predict")
async def predict(req: PredictRequest):
    image_data = base64.b64decode(req.image_base64)
    image = Image.open(BytesIO(image_data))
    x = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(x)
    prediction = torch.argmax(output, dim=1).item()
    return {"prediction": prediction}
