from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 加载GPT模型和标记器
model_name = 'gpt2'  # 模型名称
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 输入文本
input_text = "Hello, how are you?"

# 将文本编码为模型可接受的输入
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# 生成文本
output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# 解码生成的文本
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

# 打印生成的文本
print("Generated Text:")
print(generated_text)
