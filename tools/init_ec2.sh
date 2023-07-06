sudo yum install -y gperftools gperftools-devel

sudo yum install -y amazon-linux-extras
sudo amazon-linux-extras install epel -y 
sudo yum-config-manager --enable epel
sudo yum install -y git-lfs

cd ~ && mkdir -p webui && cd webui && git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

cd ~ && wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh -O Miniconda3.sh && chmod +x Miniconda3.sh && ~/Miniconda3.sh -b -p ~/miniconda3
export PATH="~/miniconda3/bin:$PATH"
conda init bash
conda create -y -n webui python=3.10

# controlnet
