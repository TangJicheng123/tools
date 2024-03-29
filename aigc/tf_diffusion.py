# export KERAS_BACKEND=tensorflow
import time
from tensorflow import keras
import keras_cv

model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

images = model.text_to_image("photograph of an astronaut riding a horse", batch_size=1)


# def plot_images(images):
#     plt.figure(figsize=(20, 20))
#     for i in range(len(images)):
#         ax = plt.subplot(1, len(images), i + 1)
#         plt.imshow(images[i])
#         plt.axis("off")


print(type(images))

# plot_images(images)

# images = model.text_to_image(
#     "cute magical flying dog, fantasy art, "
#     "golden color, high quality, highly detailed, elegant, sharp focus, "
#     "concept art, character concepts, digital painting, mystery, adventure",
#     batch_size=3,
# )
# plot_images(images)

# benchmark_result = []
# start = time.time()
# images = model.text_to_image(
#     "A cute otter in a rainbow whirlpool holding shells, watercolor",
#     batch_size=3,
# )
# end = time.time()
# benchmark_result.append(["Standard", end - start])
# plot_images(images)

# print(f"Standard model: {(end - start):.2f} seconds")
# keras.backend.clear_session()  # Clear session to preserve memory.