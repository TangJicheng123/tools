from diffusers import DiffusionPipeline
import torch

from diffusers import KandinskyV22Pipeline, KandinskyV22PriorPipeline


pipe_prior = KandinskyV22PriorPipeline.from_pretrained("kandinsky-community/kandinsky-2-2-prior", torch_dtype=torch.float16, use_safetensors=False)
pipe_prior.to("cuda")

# t2i_pipe = KandinskyV22Pipeline.from_pretrained("kandinsky-community/kandinsky-2-2-decoder", torch_dtype=torch.float16, use_safetensors=False)
t2i_pipe = KandinskyV22Pipeline.from_pretrained("/home/ec2-user/models/kandinsky-2-2-decoder", torch_dtype=torch.float16, use_safetensors=False)
t2i_pipe.to("cuda")

prompt = "portrait of a young women, blue eyes, cinematic"
negative_prompt = "low quality, bad quality"

image_embeds, negative_image_embeds = pipe_prior(prompt, negative_prompt, guidance_scale=1.0).to_tuple()

image = t2i_pipe(image_embeds=image_embeds, negative_image_embeds=negative_image_embeds, height=768, width=768).images[0]
image.save("portrait2.png")