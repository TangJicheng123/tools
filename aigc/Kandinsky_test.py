import torch
from transformers import CLIPVisionModelWithProjection
from diffusers import KandinskyV22Pipeline, KandinskyV22PriorPipeline
from diffusers.models import UNet2DConditionModel

DEVICE = torch.device('cuda')
image_encoder = CLIPVisionModelWithProjection.from_pretrained(
    'kandinsky-community/kandinsky-2-2-prior',
    subfolder='image_encoder'
).half().to(DEVICE)

unet = UNet2DConditionModel.from_pretrained(
    'kandinsky-community/kandinsky-2-2-decoder', 
    subfolder='unet'
).half().to(DEVICE)

prior = KandinskyV22PriorPipeline.from_pretrained(
    'kandinsky-community/kandinsky-2-2-prior',
    image_encoder=image_encoder, 
    torch_dtype=torch.float16
).to(DEVICE)

decoder = KandinskyV22Pipeline.from_pretrained(
    'kandinsky-community/kandinsky-2-2-decoder',
    unet=unet, 
    torch_dtype=torch.float16,
    safety_checker=None
).to(DEVICE)

negative_prior_prompt ='bad quality'
img_emb = prior(
    prompt='a nude girl',
    num_inference_steps=2, 
    num_images_per_prompt=1
)

negative_emb = prior(
    prompt=negative_prior_prompt,
    num_inference_steps=2,
    num_images_per_prompt=1
)

images = decoder(image_embeds=img_emb.image_embeds, 
                 negative_image_embeds=negative_emb.image_embeds, 
                 num_inference_steps=100, 
                 height=512, 
                 width=512)

img = images.images[0]
img.save("test.jpg")