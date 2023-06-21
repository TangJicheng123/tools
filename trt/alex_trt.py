import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit

# 定义用于加载引擎的函数
def load_engine(engine_path):
    TRT_LOGGER = trt.Logger(trt.Logger.WARNING)
    runtime = trt.Runtime(TRT_LOGGER)

    with open(engine_path, 'rb') as f:
        engine_data = f.read()

    engine = runtime.deserialize_cuda_engine(engine_data)
    return engine

# 定义用于创建执行上下文的函数
def create_context(engine):
    context = engine.create_execution_context()
    return context

# 定义用于分配和传输数据的函数
def allocate_buffers(engine):
    inputs = []
    outputs = []
    bindings = []
    stream = cuda.Stream()

    for binding in engine:
        size = trt.volume(engine.get_binding_shape(binding)) * engine.max_batch_size
        dtype = trt.nptype(engine.get_binding_dtype(binding))
        
        # 分配GPU内存
        device_mem = cuda.mem_alloc(size * dtype.itemsize)
        
        # 将输入和输出绑定到分配的内存
        if engine.binding_is_input(binding):
            inputs.append({'name': binding, 'data': device_mem})
        else:
            outputs.append({'name': binding, 'data': device_mem})
        
        # 将绑定添加到列表中
        bindings.append(int(device_mem))

    return inputs, outputs, bindings, stream

# 定义运行推理的函数
def run_inference(context, bindings, inputs, outputs, stream):
    # 将数据传输到GPU
    for input in inputs:
        cuda.memcpy_htod_async(input['data'], input['host'], stream)
    
    # 执行推理
    context.execute_async_v2(bindings=bindings, stream_handle=stream.handle)
    
    # 将结果从GPU传输回主机内存
    for output in outputs:
        cuda.memcpy_dtoh_async(output['host'], output['data'], stream)
    
    # 等待推理完成
    stream.synchronize()

# 指定引擎文件路径
engine_path = './alex.trt'

# 加载引擎
engine = load_engine(engine_path)

# 创建执行上下文
context = create_context(engine)

# 分配和传输输入/输出数据
inputs, outputs, bindings, stream = allocate_buffers(engine)

# 准备输入数据（示例：假设输入数据为浮点32位张量）
input_data = prepare_input_data()

# 将输入数据复制到输入缓冲区
cuda.memcpy_htod(inputs[0]['data'], input_data)

# 运行推理
run_inference(context, bindings, inputs, outputs, stream)

# 获取输出结果（示例：假设输出为浮点32位张量）
output_data = np.empty(output_shape, dtype=np.float32)
cuda.memcpy_dtoh(output_data, outputs[0]['data'])

# 处理输出结果
process_output_data(output_data)

# 清理资源
del engine
del context
cuda.mem_free(bindings[0])
cuda.cuda.Device().reset()
