#!/bin/bash

# 源S3目录，你需要将这里替换为你的实际S3桶和目录
SRC_S3_DIR="s3://staging-g123-ai/sagemaker/model/diffusion_model/deploy/Stable-diffusion/"

# 目标S3目录，你需要将这里替换为你的实际S3桶和目录
DEST_S3_DIR="s3://gc3a-stable-diffusion-deployment-0/Stable-diffusion/"

aws s3 sync "s3://staging-g123-ai/sagemaker/model/diffusion_model/deploy/Stable-diffusion/" "s3://gc3a-stable-diffusion-deployment-3/Stable-diffusion/"
