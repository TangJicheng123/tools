trtexec --fp16 --verbose --onnx=controlnet_dy_sim.onnx --minShapes=x:2x4x32x32,hint:1x3x256x256 --optShapes=x:2x4x64x64,hint:1x3x512x512 --maxShapes=x:2x4x128x128,hint:1x3x1024x1024 --saveEngine=./controlnet_dy_sim.trt

trtexec --fp16 --verbose --explicitBatch --onnx=controlnet_dy_sim.onnx --minShapes=x:2x4x32x32,hint:1x3x256x256 --optShapes=x:2x4x64x64,hint:1x3x512x512 --maxShapes=x:2x4x128x128,hint:1x3x1024x1024 --saveEngine=./controlnet_dy_sim.trt

trtexec --fp16 --verbose --onnx=controlnet_sim_dy2.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x128x128,hint:1x3x1024x1024 --maxShapes=x:2x4x256x256,hint:1x3x2048x2048 --saveEngine=./controlnet_sim_dy2.trt


trtexec --fp16 --verbose --preview=+fasterDynamicShapes0805 --builderOptimizationLevel=5 --onnx=controlnet_dy2.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x128x128,hint:1x3x1024x1024 --maxShapes=x:2x4x256x256,hint:1x3x2048x2048 --saveEngine=./controlnet_sim_dy2.trt


trtexec --fp16 --verbose --preview=+fasterDynamicShapes0805 --builderOptimizationLevel=5 --onnx=controlnet_dy2.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x64x64,hint:1x3x512x512 --maxShapes=x:2x4x128x128,hint:1x3x1024x1024 --saveEngine=./controlnet_sim_dy2.trt


trtexec --fp16 --verbose --preview=+fasterDynamicShapes0805 --builderOptimizationLevel=5 --onnx=controlnet_sim_dy2.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x64x64,hint:1x3x512x512 --maxShapes=x:2x4x128x128,hint:1x3x1024x1024 --saveEngine=./controlnet_sim_dy2.trt


trtexec --fp16 --verbose --preview=+fasterDynamicShapes0805 --builderOptimizationLevel=5 --onnx=controlnet_dy2_fp16.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x64x64,hint:1x3x512x512 --maxShapes=x:2x4x128x128,hint:1x3x1024x1024 --saveEngine=./controlnet_sim_dy2.trt

trtexec --fp16 --verbose --preview=+fasterDynamicShapes0805 --builderOptimizationLevel=5 --onnx=controlnet_dy2_fp16.onnx --minShapes=x:2x4x32x32,hint:1x3x256x256 --optShapes=x:2x4x64x64,hint:1x3x512x512 --maxShapes=x:2x4x128x128,hint:1x3x1024x1024 --saveEngine=./controlnet_sim_dy2.trt

trtexec --fp16 --builderOptimizationLevel=5 --onnx=controlnet_dy2_fp16.onnx --minShapes=x:2x4x32x32,hint:1x3x256x256 --optShapes=x:2x4x64x64,hint:1x3x512x512 --maxShapes=x:2x4x128x128,hint:1x3x1024x1024 --saveEngine=./controlnet_sim_dy2.trt

trtexec --fp16 --onnx=controlnet_dy2_fp16.onnx --minShapes=x:2x4x32x32,hint:1x3x256x256 --optShapes=x:2x4x64x64,hint:1x3x512x512 --maxShapes=x:2x4x128x128,hint:1x3x1024x1024 --saveEngine=./controlnet_sim_dy2.trt

trtexec --fp16 --onnx=controlnet_dy2_fp16.onnx --layerPrecisions=layernorm:fp32 --minShapes=x:2x4x32x32,hint:1x3x256x256 --optShapes=x:2x4x64x64,hint:1x3x512x512 --maxShapes=x:2x4x128x128,hint:1x3x1024x1024 --saveEngine=./controlnet_sim_dy2.trt

trtexec --fp16 --onnx=controlnet_dy2_inner_op16.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x256x256,hint:1x3x2048x2048 --maxShapes=x:2x4x256x256,hint:1x3x2048x2048 --saveEngine=./controlnet_sim_dy2_ok2.trt

trtexec --fp16 --builderOptimizationLevel=5 --onnx=controlnet_dy2_inner_op16.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x256x256,hint:1x3x2048x2048 --maxShapes=x:2x4x256x256,hint:1x3x2048x2048 --saveEngine=./controlnet_sim_dy2_ok2.trt

trtexec --fp16 --builderOptimizationLevel=5 --onnx=controlnet_dy2_inner_no_einsum.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x256x256,hint:1x3x2048x2048 --maxShapes=x:2x4x256x256,hint:1x3x2048x2048 --saveEngine=./controlnet_sim_dy2_ok2.trt

trtexec --fp16 --builderOptimizationLevel=5 --onnx=controlnet_dy2_inner_no_einsum3.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x256x256,hint:1x3x2048x2048 --maxShapes=x:2x4x256x256,hint:1x3x2048x2048 --saveEngine=./controlnet_sim_dy2_ok2.trt

trtexec --fp16 --builderOptimizationLevel=5 --onnx=controlnet_dy2_inner_no_einsum3_webui.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x256x256,hint:1x3x2048x2048 --maxShapes=x:2x4x256x256,hint:1x3x2048x2048 --saveEngine=./controlnet_sim_dy2_ok2.trt

trtexec --fp16 --builderOptimizationLevel=5 --onnx=controlnet_dy2_inner_no_einsum3_webui_steps32.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x256x256,hint:1x3x2048x2048 --maxShapes=x:2x4x256x256,hint:1x3x2048x2048 --saveEngine=./controlnet_sim_dy2_ok2.trt

trtexec --fp16 --onnx=controlnet_dy2_inner_no_einsum3_webui_steps32.onnx --minShapes=x:2x4x64x64,hint:1x3x512x512 --optShapes=x:2x4x256x256,hint:1x3x2048x2048 --maxShapes=x:2x4x256x256,hint:1x3x2048x2048 --saveEngine=./controlnet_sim_dy2_ok2.trt
