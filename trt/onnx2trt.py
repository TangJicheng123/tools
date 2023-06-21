import tensorrt as trt

trt.init_libnvinfer_plugins(None, "")

engine_file = "./controlnet_sim_script.trt"
onnx_file = "./controlnet_sim.onnx"

TRT_LOGGER = trt.Logger(trt.Logger.INFO)

builder = trt.Builder(TRT_LOGGER)
network = builder.create_network(1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH))
parser = trt.OnnxParser(network, TRT_LOGGER)
success = parser.parse_from_file(onnx_file)

for idx in range(parser.num_errors):
    print(parser.get_error(idx))

if not success:
    pass # Error handling code here

config = builder.create_builder_config()
config.set_memory_pool_limit(trt.MemoryPoolType.WORKSPACE, 1 << 30) # 1 GiB
serialized_engine = builder.build_serialized_network(network, config)
with open(engine_file, "wb") as f:
    f.write(serialized_engine)

# with open(engine_file, 'rb') as f:
#     engine_data = f.read()
# engine = runtime.deserialize_cuda_engine(engine_data)

runtime = trt.Runtime(TRT_LOGGER)
engine = runtime.deserialize_cuda_engine(serialized_engine)
