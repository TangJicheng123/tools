import image_base64

from PIL import Image

girl_image = Image.open("./girl.jpeg")

girl_b64 = image_base64.encode_pil_to_base64(girl_image, "jpeg", 90)

girl2 = image_base64.decode_base64_to_image(girl_b64)

girl2.save("./girl2.png")

