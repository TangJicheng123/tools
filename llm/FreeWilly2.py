import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

cache = "~/.cache"

tokenizer = AutoTokenizer.from_pretrained("stabilityai/FreeWilly2", use_fast=False, cache_dir=cache)
model = AutoModelForCausalLM.from_pretrained("stabilityai/FreeWilly2", torch_dtype=torch.float16, low_cpu_mem_usage=True, device_map="auto", cache_dir=cache)
system_prompt = "### System:\nYou are Free Willy, an AI that follows instructions extremely well. Help as much as you can. Remember, be safe, and don't do anything illegal.\n\n"

message = "Write me a poem please"
prompt = f"{system_prompt}### User: {message}\n\n### Assistant:\n"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
output = model.generate(**inputs, do_sample=True, top_p=0.95, top_k=0, max_new_tokens=256)

print(tokenizer.decode(output[0], skip_special_tokens=True))
