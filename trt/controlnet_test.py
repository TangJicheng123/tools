import onnxruntime as ort 
import numpy as np
import torch
import time
import timeit

providers = ["CUDAExecutionProvider"]

# 创建 SessionOptions 对象
session_options = ort.SessionOptions()


session_options.intra_op_num_threads = 8
session_options.execution_mode = ort.ExecutionMode.ORT_PARALLEL
session_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL

path = "/host-local/tools/trt/"
model_file = "controlnet_dy2_inner_no_einsum3_webui.onnx"
ort_sess = ort.InferenceSession(model_file, sess_options=session_options, providers=providers)

device = torch.device("cuda")
dtype = torch.float32
x = torch.randn((2, 4, 128, 128), dtype=dtype, device=device).cpu().numpy()
hint = torch.randn((1, 3, 1024, 1024), dtype=dtype, device=device).cpu().numpy()
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

print(f"ok, {end_time - start_time}ms")