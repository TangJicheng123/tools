import onnx
from onnxconverter_common import float16

path = "/Users/ctw/Desktop/contorlnet_model/"
model = onnx.load(path + "controlnet_dy.onnx")
model_fp16 = float16.convert_float_to_float16(model)
onnx.save(model_fp16, path + "controlnet_dy_my_fp16.onnx")