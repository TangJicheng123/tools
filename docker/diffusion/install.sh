wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh -O Miniconda3.sh
chmod +x Miniconda3.sh
mkdir -p /opt
./Miniconda3.sh -b -p /opt/miniconda
PATH="/opt/miniconda/bin:${PATH}"
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui && git checkout v1.3.0


