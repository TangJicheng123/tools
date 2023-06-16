import onnx

# 加载 ONNX 模型
model_path = 'controlnet_sim.onnx'
model = onnx.load(model_path)

# 遍历模型中的节点
for node in model.graph.node:
    node_type = node.op_type
    node_name = node.name
    print(f"node_type: {node_type}")
