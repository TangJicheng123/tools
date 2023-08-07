from transformers import AutoTokenizer, AutoModel

cache = "~/.cache"

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b",
                                          trust_remote_code=True,
                                          cache_dir=cache)
model = AutoModel.from_pretrained("THUDM/chatglm2-6b",
                                  trust_remote_code=True,
                                  cache_dir=cache).half().cuda()
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)
response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
print(response)
