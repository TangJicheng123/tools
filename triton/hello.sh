conda create -n triton -y python=3.10
pip install -r requirements.txt

docker pull nvcr.io/nvidia/tritonserver:23.01-py3
nvidia-docker run -itd -v /home/ec2-user/SageMaker:/local-host --name my_triton nvcr.io/nvidia/tritonserver:23.01-py3 /bin/bash

wget https://github.com/onnx/models/raw/main/vision/classification/resnet/model/resnet18-v1-7.onnx && mv resnet18-v1-7.onnx model.onnx

wget https://www.dropbox.com/s/r2ingd0l3zt8hxs/frozen_east_text_detection.tar.gz && tar -xvf frozen_east_text_detection.tar.gz

python -m tf2onnx.convert --input frozen_east_text_detection.pb --inputs "input_images:0" --outputs "feature_fusion/Conv_7/Sigmoid:0","feature_fusion/concat_3:0" --output detection.onnx

wget https://www.dropbox.com/sh/j3xmli4di1zuv3s/AABzCC1KGbIRe2wRwa3diWKwa/None-ResNet-None-CTC.pth
