import safetensors.torch

path = "/Users/ctw/stable-diffusion-webui/models/Stable-diffusion/"
file = path + "Lyriel.safetensors"
file = path + "Aniflatmix.safetensors"
file = path + "Counterfeit-V3.0.safetensors"
pl_sd = safetensors.torch.load_file(file)

# print(type(pl_sd))
sum = 0
for k, v in pl_sd.items():
    print(k, ": ", v.size(), " num: ", v.numel())
    sum += v.numel()
print("sum: ", sum)
