export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_SESSION_TOKEN=""

export MODEL_DIR="runwayml/stable-diffusion-v1-5"
export OUTPUT_DIR="results"
# export CACHE_DIR="model_cache"

accelerate launch --aws_access_key_id $AWS_ACCESS_KEY_ID --aws_secret_access_key $AWS_SECRET_ACCESS_KEY train_controlnet.py \
 --pretrained_model_name_or_path $MODEL_DIR \
 --output_dir $OUTPUT_DIR \
 --num_train_epochs 10 \
 --dataset_name fusing/fill50k \
 --resolution 512 \
 --learning_rate 1e-5 \
 --train_batch_size 4 \
 --gradient_accumulation_steps 8 \
 --gradient_checkpointing True \
 --use_8bit_adam True \
 --enable_xformers_memory_efficient_attention True \
 --set_grads_to_none True