from diffusers import DiffusionPipeline

model_path = "/home/ec2-user/models/urpm"

pipeline = DiffusionPipeline.from_pretrained(model_path)
pipeline.to("cuda")
neg = "lowres, mediumres, low quality, medium quality, old, unrealistic, writing, logo, text, worst quality, high pass filter, airbrush, cell shading, fake, bad photo, unrealistic, multipanel, collage, comic, censored, clothes, covered, clothed, dressed, clad, prudent, modest, shy, timid, sheepish, reluctant, disinclined, reserved, chaste, monogamous, restrained, cartoon, illustration, painting, art, drawing, sketch, blurry, bokeh, dof, grainy, gaussian, monochrome, ringing, mutation, mutated, bad face, deformed face, smooth skin, bad drawing, dead eyes, ugly, lifeless, bad hands, out of frame, missing limb, extra limb, missing hand, missing finger, extra finger, fused bodies, fused limb, attired, fused finger, missing genitals, fused genitals, group,"
image = pipeline("woman licking another woman's pussy, (((cunnilingus))), ((detailed genitals)), ((detailed faces)), 2girls", negative_prompt=neg,
                 num_inference_steps=20).images[0]

image.save("test1.png")
