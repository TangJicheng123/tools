from huggingface_hub import snapshot_download
snapshot_location = snapshot_download(repo_id="runwayml/stable-diffusion-v1-5", ignore_patterns=["*.safetensors", "*.ckpt"], cache_dir="/Users/ctw/cache_dir")
snapshot_location