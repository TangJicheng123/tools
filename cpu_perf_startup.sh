sudo yum install git gcc g++ htop mesa-libGL.x86_64
git clone https://github.com/TangJicheng123/cpu_test.git
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2022.05-Linux-x86_64.sh

chmod a+x ./Anaconda3-2022.05-Linux-x86_64.sh
./Anaconda3-2022.05-Linux-x86_64.sh

source ~/.bashrc
conda create python=3.10 -n cpu_test -y
conda activate cpu_test

cd cpu_test
pip install -r requirements.txt