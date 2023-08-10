from diffusers import StableDiffusionPipeline
from PIL import Image
import random

model_path = "/Users/ctw/models/vivid_paina"

pipe = StableDiffusionPipeline.from_pretrained(model_path)

prompt = "a nude girl"
steps = 50

image = pipe(prompt=prompt, num_inference_steps=steps).images[0]

pic_path = "picture/"
filename = prompt.replace(" ", "_") + "_" + str(random.randint(10**4,
                                                         10**5 - 1)) + ".jpg"
image.save(pic_path + filename)
print(filename, "is saved.")