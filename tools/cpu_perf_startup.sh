sudo yum install -y git gcc g++ htop mesa-libGL.x86_64
git clone https://github.com/TangJicheng123/cpu_test.git
git clone https://gitlab.com/juliensimon/huggingface-demos.git
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2022.05-Linux-x86_64.sh

chmod a+x ./Anaconda3-2022.05-Linux-x86_64.sh
./Anaconda3-2022.05-Linux-x86_64.sh

source ~/.bashrc
conda create python=3.10 -n cpu_test -y
conda activate cpu_test

cd cpu_test
pip install -r requirements.txt

cd vino
python vino2.py

mo --input_model text_encoder.onnx --compress_to_fp16
mo --input_model vae_decoder.onnx --compress_to_fp16
mo --input_model vae_encoder.onnx --compress_to_fp16
mo --input_model unet/unet.onnx --compress_to_fp16

mo --input_model text_encoder.onnx --data_type half
mo --input_model vae_decoder.onnx --data_type half
mo --input_model vae_encoder.onnx --data_type half
mo --input_model unet/unet.onnx --data_type half

python vino3.py