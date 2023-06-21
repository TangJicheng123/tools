import tensorrt as trt
import torch
import numpy as np

trt.init_libnvinfer_plugins(None, "")

engine_file = "./controlnet_dy_sim.trt"

TRT_LOGGER = trt.Logger(trt.Logger.INFO)

with open(engine_file, "rb") as f:
    serialized_engine = f.read()

runtime = trt.Runtime(TRT_LOGGER)
engine = runtime.deserialize_cuda_engine(serialized_engine)

num_inputs = engine.num_bindings
for i in range(num_inputs):
    input_shape = engine.get_binding_shape(i)
    input_dtype = engine.get_binding_dtype(i)
    print(f"Input {i} - Shape: {input_shape}, Type: {input_dtype}")

context = engine.create_execution_context()

# set input
def get_input(input_name, shape):
    tensor = torch.ones(shape).to("cuda")
    trt_shape = trt.Dims(shape)
    return (input_name, tensor, trt_shape)

x_name, x_tensor, x_shape = get_input("x", [2, 4, 32, 64])

hint_name, hint_tensor, hint_shape = get_input("hint", [1, 3, 256, 512])

timesteps_name, timesteps_tensor, timesteps_shape = get_input("timesteps", [2,])

context_name, context_tensor, context_shape = get_input("context", [2,77,768])

def get_output(output_name, shape):
    tensor = torch.zeros(shape).to("cuda")
    return (output_name, tensor)

output0_name, output0_tensor = get_output("output0", [2,320,64,64])
output1_name, output1_tensor = get_output("output1", [2,320,64,64])
output2_name, output2_tensor = get_output("output2", [2,320,64,64])
output3_name, output3_tensor = get_output("output3", [2,320,32,32])
output4_name, output4_tensor = get_output("output4", [2,640,32,32])
output5_name, output5_tensor = get_output("output5", [2,640,32,32])
output6_name, output6_tensor = get_output("output6", [2,640,16,16])
output7_name, output7_tensor = get_output("output7", [2,1280,16,16])
output8_name, output8_tensor = get_output("output8", [2,1280,16,16])
output9_name, output9_tensor = get_output("output9", [2,1280,8,8])
output10_name, output10_tensor = get_output("output10", [2,1280,8,8])
output11_name, output11_tensor = get_output("output11", [2,1280,8,8])
output12_name, output12_tensor = get_output("output12", [2,1280,8,8])

context.set_input_shape(x_name, x_shape)
context.set_tensor_address(x_name, x_tensor.data_ptr())

context.set_input_shape(hint_name, hint_shape)
context.set_tensor_address(hint_name, hint_tensor.data_ptr())

context.set_input_shape(timesteps_name, timesteps_shape)
context.set_tensor_address(timesteps_name, timesteps_tensor.data_ptr())

context.set_input_shape(context_name, context_shape)
context.set_tensor_address(context_name, context_tensor.data_ptr())

context.set_tensor_address(output0_name, output0_tensor.data_ptr())
context.set_tensor_address(output1_name, output1_tensor.data_ptr())
context.set_tensor_address(output2_name, output2_tensor.data_ptr())
context.set_tensor_address(output3_name, output3_tensor.data_ptr())
context.set_tensor_address(output4_name, output4_tensor.data_ptr())
context.set_tensor_address(output5_name, output5_tensor.data_ptr())
context.set_tensor_address(output6_name, output6_tensor.data_ptr())
context.set_tensor_address(output7_name, output7_tensor.data_ptr())
context.set_tensor_address(output8_name, output8_tensor.data_ptr())
context.set_tensor_address(output9_name, output9_tensor.data_ptr())
context.set_tensor_address(output10_name, output10_tensor.data_ptr())
context.set_tensor_address(output11_name, output11_tensor.data_ptr())
context.set_tensor_address(output12_name, output12_tensor.data_ptr())

stream = torch.cuda.Stream()

context.execute_async_v3(stream.stream_id)

stream.synchronize()

# output_tensor_cpu = output_tensor.to("cpu")
# print(output_tensor_cpu)
# np.savetxt("trt_output.txt", output_tensor_cpu.numpy(), fmt="%.5f")
