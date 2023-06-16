import onnxruntime as ort 
import numpy as np


# 创建 SessionOptions 对象
session_options = ort.SessionOptions()

# 设置 CUDA 运行选项
session_options.enable_cuda = True

# 设置 FP16 选项
session_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
session_options.enable_profiling = True
session_options.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
session_options.optimized_model_filepath = 'optimized_model.onnx'
session_options.enable_fp16 = True

model_file = "./controlnet_sim.onnx"
ort_sess = ort.InferenceSession(model_file, sess_options=session_options)

x = np.random.rand(2, 4, 225, 64)
hint = np.random.rand(1, 3, 1800, 512)
timesteps = np.random.rand(2)
context = np.random.rand(2, 77, 768)

output_names = [output.name for output in ort_sess.get_outputs()]

output = ort_sess.run(output_names, {"x": x, "hint":hint, "timesteps":timesteps, "context":context})
