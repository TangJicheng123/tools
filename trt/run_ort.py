import onnxruntime as ort
import numpy as np

ort_session = ort.InferenceSession("alexnet.onnx", providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])

outputs = ort_session.run(
    None,
    {"actual_input_1": np.ones([10, 3, 224, 224]).astype(np.float32)},
)
print(outputs[0])
np.savetxt("ort_output.txt", outputs[0], fmt="%.5f")