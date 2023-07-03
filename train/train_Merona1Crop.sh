# download model
aws s3 sync s3://staging-g123-ai/sagemaker/model/diffusion_model/pretrained_model/artifex_pretrain_model/ .

accelerate launch --mixed_precision="fp16" train_dreambooth_diffusers.py \
        --pretrained_model_name_or_path="/home/ec2-user/models/artifex_pretrain_model/novelai" \
        --train_text_encoder \
        --instance_data_dir="/home/ec2-user/tools/train/Merona1" \
        --output_dir="/home/ec2-user/tools/train/Merona1_model" \
        --instance_prompt="artifex-queensblade-Merona1Crop" \
        --resolution=512 \
        --train_batch_size=1 \
        --use_8bit_adam \
        --gradient_accumulation_steps=4 --gradient_checkpointing \
        --learning_rate=5e-6 \
        --lr_scheduler="cosine"\
        --lr_warmup_steps=0 \
        --max_train_steps=100 \
        --mixed_precision=fp16