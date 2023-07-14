import grpc
import grpc_service_pb2
import grpc_service_pb2_grpc
import numpy as np

# 创建 gRPC 通道
channel = grpc.insecure_channel('127.0.0.1:8001')

# 创建 Triton Server 的推断服务客户端
client = grpc_service_pb2_grpc.GRPCInferenceServiceStub(channel)

# 创建推断请求
request = grpc_service_pb2.ModelInferRequest()

# 设置模型名称
request.model_name = 'stage-1'

# 创建输入张量
input_tensor = request.inputs.add()
input_tensor.name = 'input_str'
input_tensor.shape.extend([1])  # 设置输入形状为 [1]
input_tensor.datatype = "BYTES"

# 设置输入数据
input_tensor_contents = [b'EC2_TritonServer']
input_tensor.contents.bytes_contents.extend(input_tensor_contents)

# 发送推断请求
response = client.ModelInfer(request)

# 处理响应
if response:
    # 提取输出张量
    output = (response.raw_output_contents[0]).decode("utf-8")
    print(output)
else:
    print("Inference request failed")


