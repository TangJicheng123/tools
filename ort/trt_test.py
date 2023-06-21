import tensorrt as trt
import numpy as np

# 加载 TensorRT 引擎
engine_filename = "./controlnet_final2.trt"
with open(engine_filename, 'rb') as f:
    engine_data = f.read()

runtime = trt.Runtime(trt.Logger(trt.Logger.WARNING))
engine = runtime.deserialize_cuda_engine(engine_data)

# 创建执行上下文
context = engine.create_execution_context()

# 准备输入数据
input_data = ...  # 替换为你的输入数据

# 在 GPU 上为输入和输出分配内存
input_binding = engine.get_binding_index('input')
output_binding = engine.get_binding_index('output')
device_input = cuda.mem_alloc(input_data.nbytes)
device_output = cuda.mem_alloc(output_size)

# 将输入数据复制到 GPU 内存
cuda.memcpy_htod(device_input, input_data)

# 设置输入和输出绑定
bindings = [int(device_input), int(device_output)]
context.set_binding_shape(input_binding, input_data.shape)
context.set_binding_shape(output_binding, output_shape)

# 执行推理
context.execute_v2(bindings)

# 获取输出结果
output_data = np.empty(output_shape, dtype=np.float32)
cuda.memcpy_dtoh(output_data, device_output)

# 处理输出结果
print(output_data)
