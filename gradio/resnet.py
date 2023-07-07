import gradio as gr
import torch
from torchvision.models import resnet50
from torchvision.transforms import functional as F
import numpy as np

# Load the pre-trained ResNet model
model = resnet50(pretrained=True)
model.eval()

# Define the function to classify an image using ResNet


def classify_image(image):
    # Convert the image to a NumPy array
    image_np = np.array(image)

    # Preprocess the image
    image = F.to_pil_image(image_np)
    image = F.resize(image, (224, 224))
    image = F.to_tensor(image)
    image = F.normalize(image, mean=[0.485, 0.456, 0.406], std=[
                        0.229, 0.224, 0.225])
    image = image.unsqueeze(0)

    # Forward pass through the model
    with torch.no_grad():
        output = model(image)

    # Get the predicted class index
    _, predicted_idx = torch.max(output, 1)

    # Return the predicted class label
    return str(predicted_idx.item())


# Create the input and output interfaces
inputs = gr.inputs.Image()
outputs = gr.outputs.Textbox()

# Create the Gradio interface
iface = gr.Interface(fn=classify_image, inputs=inputs, outputs=outputs)

# Launch the Gradio app
iface.launch()
