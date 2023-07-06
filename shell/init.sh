export DEBIAN_FRONTEND=noninteractive
apt-get update -y 
apt-get install -y libgl1 libglib2.0-0 wget git \
    unzip curl vim\
    git-lfs google-perftools libgoogle-perftools-dev\
    supervisor ffmpeg libsm6 libxext6 \
    clang \
    build-essential \
    libssl-dev \
    default-libmysqlclient-dev

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip -q awscliv2.zip && ./aws/install