import onnxruntime as ort 
import numpy as np
import torch
import time
import timeit

providers = ["CUDAExecutionProvider"]

# 创建 SessionOptions 对象
session_options = ort.SessionOptions()

# session_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
# session_options.enable_profiling = True
# session_options.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
# session_options.optimized_model_filepath = 'optimized_model.onnx'

path = "/host-local/tools/trt/"
model_file = "controlnet_dy2_inner_no_einsum3_webui.onnx"
ort_sess = ort.InferenceSession(model_file, sess_options=session_options, providers=providers)

device = torch.device("cuda")
dtype = torch.float32
x = torch.randn((2, 4, 64, 64), dtype=dtype, device=device).cpu().numpy()
hint = torch.randn((1, 3, 512, 512), dtype=dtype, device=device).cpu().numpy()
timesteps = torch.randn((2), dtype=dtype, device=device).cpu().numpy()
context = torch.randn((2, 77, 768), dtype=dtype, device=device).cpu().numpy()

output_names = [output.name for output in ort_sess.get_outputs()]

# warmup
for i in range(5):
    output = ort_sess.run(output_names, {"x": x, "hint":hint, "timesteps":timesteps, "context":context})


torch.cuda.synchronize()
start_time = timeit.default_timer() * 1000
for i in range(20):
    output = ort_sess.run(output_names, {"x": x, "hint":hint, "timesteps":timesteps, "context":context})
torch.cuda.synchronize()
end_time = timeit.default_timer() * 1000

print(f"ok, {end_time - start_time}")