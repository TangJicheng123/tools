# train

## train dog

```
./dog_download.py
mkdir -p dog_model
./train_dogs.sh
python diffusers2webui.py -i dog_model -o dog.safetensors
```