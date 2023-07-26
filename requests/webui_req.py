import requests
import json
import base64
import io

base_url = 'http://127.0.0.1:7860'
txt2img_path = '/sdapi/v1/txt2img'

false = False
true = True
data = {
    "enable_hr": false,
    "denoising_strength": 0.5,
    "firstphase_width": 0,
    "firstphase_height": 0,
    "hr_scale": 2,
    "hr_upscaler": "string",
    "hr_second_pass_steps": 0,
    "hr_resize_x": 0,
    "hr_resize_y": 0,
    "hr_sampler_name": "string",
    "hr_prompt": "",
    "hr_negative_prompt": "",
    "prompt": "1girl",
    "styles": [
        "string"
    ],
    "seed": -1,
    "subseed": -1,
    "subseed_strength": 0,
    "seed_resize_from_h": -1,
    "seed_resize_from_w": -1,
    "sampler_name": "LMS",
    "batch_size": 1,
    "n_iter": 1,
    "steps": 20,
    "cfg_scale": 7,
    "width": 512,
    "height": 512,
    "restore_faces": false,
    "tiling": false,
    "do_not_save_samples": false,
    "do_not_save_grid": false,
    "negative_prompt": "",
    "eta": 0,
    "s_min_uncond": 0,
    "s_churn": 0,
    "s_tmax": 0,
    "s_tmin": 0,
    "s_noise": 1,
    "override_settings": {},
    "override_settings_restore_afterwards": true,
    "script_args": [],
    "sampler_index": "Euler",
    "script_name": "",
    "send_images": true,
    "save_images": false,
    "alwayson_scripts": {}
    }

input2_adetailer = '''{
                "enable_hr": false,
                "denoising_strength": 0.5,
                "firstphase_width": 0,
                "firstphase_height": 0,
                "hr_scale": 2,
                "hr_upscaler": "string",
                "hr_second_pass_steps": 0,
                "hr_resize_x": 0,
                "hr_resize_y": 0,
                "hr_sampler_name": "string",
                "hr_prompt": "",
                "hr_negative_prompt": "",
                "prompt": "1girl,  <lora:test_lora:1:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0>",
                "styles": [
                    "string"
                ],
                "seed": 123,
                "subseed": 123,
                "subseed_strength": 0,
                "seed_resize_from_h": -1,
                "seed_resize_from_w": -1,
                "sampler_name": "LMS",
                "batch_size": 1,
                "n_iter": 1,
                "steps": 20,
                "cfg_scale": 7,
                "width": 512,
                "height": 512,
                "restore_faces": false,
                "tiling": false,
                "do_not_save_samples": false,
                "do_not_save_grid": false,
                "negative_prompt": "",
                "eta": 0,
                "s_min_uncond": 0,
                "s_churn": 0,
                "s_tmax": 0,
                "s_tmin": 0,
                "s_noise": 1,
                "override_settings": {},
                "override_settings_restore_afterwards": true,
                "script_args": [],
                "sampler_index": "Euler",
                "script_name": "",
                "send_images": true,
                "save_images": false,
                "alwayson_scripts": {
                    "ADetailer": {
                        "args": [
                            true,
                            {
                            "ad_model": "face_yolov8n.pt",
                            "ad_inpaint_only_masked": true
                            }
                        ]
                        }
                }
                }'''

input2 = '''{
                "enable_hr": false,
                "denoising_strength": 0.5,
                "firstphase_width": 0,
                "firstphase_height": 0,
                "hr_scale": 2,
                "hr_upscaler": "string",
                "hr_second_pass_steps": 0,
                "hr_resize_x": 0,
                "hr_resize_y": 0,
                "hr_sampler_name": "string",
                "hr_prompt": "",
                "hr_negative_prompt": "",
                "prompt": "1girl,  <lora:test_lora:1:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0>",
                "styles": [
                    "string"
                ],
                "seed": 123,
                "subseed": 123,
                "subseed_strength": 0,
                "seed_resize_from_h": -1,
                "seed_resize_from_w": -1,
                "sampler_name": "LMS",
                "batch_size": 1,
                "n_iter": 1,
                "steps": 20,
                "cfg_scale": 7,
                "width": 512,
                "height": 512,
                "restore_faces": false,
                "tiling": false,
                "do_not_save_samples": false,
                "do_not_save_grid": false,
                "negative_prompt": "",
                "eta": 0,
                "s_min_uncond": 0,
                "s_churn": 0,
                "s_tmax": 0,
                "s_tmin": 0,
                "s_noise": 1,
                "override_settings": {},
                "override_settings_restore_afterwards": true,
                "script_args": [],
                "sampler_index": "Euler",
                "script_name": "",
                "send_images": true,
                "save_images": false,
                "alwayson_scripts": {}
                }'''

from PIL import Image
import image_base64
image_path = "./girl.jpeg"
my_image = Image.open("./girl.jpeg")
my_image_b64 = image_base64.encode_pil_to_base64(my_image, "jpeg", 90)

input2_controlnet = '''{
                "enable_hr": false,
                "denoising_strength": 0.5,
                "firstphase_width": 0,
                "firstphase_height": 0,
                "hr_scale": 2,
                "hr_upscaler": "string",
                "hr_second_pass_steps": 0,
                "hr_resize_x": 0,
                "hr_resize_y": 0,
                "hr_sampler_name": "string",
                "hr_prompt": "",
                "hr_negative_prompt": "",
                "prompt": "1girl,  <lora:test_lora:1:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0>",
                "styles": [
                    "string"
                ],
                "seed": 123,
                "subseed": 123,
                "subseed_strength": 0,
                "seed_resize_from_h": -1,
                "seed_resize_from_w": -1,
                "sampler_name": "LMS",
                "batch_size": 1,
                "n_iter": 1,
                "steps": 20,
                "cfg_scale": 7,
                "width": 512,
                "height": 512,
                "restore_faces": false,
                "tiling": false,
                "do_not_save_samples": false,
                "do_not_save_grid": false,
                "negative_prompt": "",
                "eta": 0,
                "s_min_uncond": 0,
                "s_churn": 0,
                "s_tmax": 0,
                "s_tmin": 0,
                "s_noise": 1,
                "override_settings": {},
                "override_settings_restore_afterwards": true,
                "script_args": [],
                "sampler_index": "Euler",
                "script_name": "",
                "send_images": true,
                "save_images": false,
                "alwayson_scripts": {
                    "controlnet": {
                    "args": [
                        {
                            "enabled": true,
                            "model": "control_v11p_sd15_depth",
                            "mask": "",
                            "module": "depth_midas",
                            "weight": 1,
                            "resize_mode": "Scale to Fit (Inner Fit)",
                            "guidance_start": 0,
                            "guidance_end": 1, 
                            "threshold_a": 64,
                            "threshold_b": 64,
                            "control_mode": "My prompt is more important",
                            "pixel_perfect": true,
                            "input_image": "'''
end_str = '''"
                        }
                    ]
                    }
                }
                }'''

input2_controlnet = input2_controlnet + my_image_b64.decode('utf-8') + end_str

data2 = json.loads(input2_controlnet)
response = requests.post(base_url + txt2img_path, json=data2)

# response = requests.post(base_url + txt2img_path, data=json.dumps(data))

p1 = "1girl,  <lora:test_lora:1:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0>"
p2 = "1girl,  <lora:test_lora:1:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1>"
p3 = "1girl,  <lora:test_lora:1:1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1>"

data = response.json()
print("[response] ", data)

i = 0
for image_str in data["images"]:
    i += 1
    image_data = base64.b64decode(image_str)
    with open("11.jpg", "wb") as f:
        f.write(image_data)