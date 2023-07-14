# generate triton server proto&grpc code for python
pip install grpcio grpcio-tools
python -m grpc_tools.protoc -I ./triton_proto --python_out=. --grpc_python_out=. ./triton_proto/grpc_service.proto
python -m grpc_tools.protoc -I ./triton_proto --python_out=. --grpc_python_out=. ./triton_proto/model_config.proto
python -m grpc_tools.protoc -I ./triton_proto --python_out=. --grpc_python_out=. ./triton_proto/health.proto
