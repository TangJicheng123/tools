export WORKDIR=~/webui
mkdir -p $WORKDIR
cd $WORKDIR && git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git 
cd $WORKDIR/stable-diffusion-webui/extensions && git clone https://github.com/Bing-su/adetailer.git
cd $WORKDIR/stable-diffusion-webui/extensions && git clone https://github.com/Mikubill/sd-webui-controlnet.git
cd $WORKDIR/stable-diffusion-webui/extensions && git clone https://github.com/toriato/stable-diffusion-webui-wd14-tagger.git
cd $WORKDIR/stable-diffusion-webui/extensions && git clone https://github.com/s0md3v/sd-webui-roop.git

cd $WORKDIR && git clone https://huggingface.co/lllyasviel/ControlNet-v1-1
