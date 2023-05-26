#!/bin/bash

env=staging
# VAE
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/vae/kl-f8-anime2.vae.pt" "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/VAE/"

# Embeddings
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/embedding/EasyNegative.pt" "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/embeddings/"
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/embedding/bad_prompt.pt" "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/embeddings/"
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/embedding/bad_prompt_version2.pt" "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/embeddings/"

# BaseModel
# Character
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/dreambooth/paina_novel_caption_100.safetensors" "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/Stable-diffusion/"
# Icon
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/base_model/Lyriel-1.5.safetensors" "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/Stable-diffusion/"

# ControlNet
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Artifex_Controlnet/control_v11p_sd15_canny.yaml" "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/ControlNet/"
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Artifex_Controlnet/control_v11p_sd15_canny.pth" "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/ControlNet/"

# LoRA
# Character
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Lora/Style/Moxin_10.safetensors" "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/Lora/"
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Lora/Style/Moxin_Shukezouma11.safetensors"  "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/Lora/"
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Lora/Style/Colorwater_v4.safetensors"  "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/Lora/"
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Lora/Style/standingFullBodyWithBackgroundStyle_v10Offset.safetensors"  "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/Lora/"
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Lora/Style/style_mikazuki.safetensors"  "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/Lora/"
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Lora/Style/style_mementomori.safetensors"  "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/Lora/"
# Icon
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Lora/Style/okashi-gstyle.safetensors"  "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/Lora/"
aws s3 cp "s3://$env-g123-ai/sagemaker/model/diffusion_model/pretrained_model/Lora/Style/tsukisima-ystyle.safetensors"  "s3://$env-g123-ai/sagemaker/model/diffusion_model/deploy/Lora/"
