trtexec --fp16 --verbose --onnx=controlnet_final.onnx --saveEngine=./controlnet_final2.trt

trtexec --fp16 --verbose --onnx=controlnet_final.onnx --minShapes=x:2x4x32x32,hint:1x3x256x256 --optShapes=x:2x4x64x64,hint:1x3x512x512 --maxShapes=x:2x4x512x512,hint:1x3x2048x2048 --saveEngine=./controlnet_final2.trt
trtexec --onnx=controlnet_sim.onnx --shapes=x:2x4x64x64,hint:1x3x512x512 