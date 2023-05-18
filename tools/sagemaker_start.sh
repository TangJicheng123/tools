wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
source ~/.bashrc
cd /home/ec2-user/SageMaker
conda create -n py310 python=3.10
conda activate py310
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui/models/Stable-diffusion
aws s3 cp s3://staging-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Old_SD/bg_generation_model/ . --recursive
cd /home/ec2-user/SageMaker/stable-diffusion-webui
./webui.sh --share