import cv2
import numpy as np
import onnxruntime as rt
import gradio as gr
from huggingface_hub import hf_hub_download
from dataclasses import dataclass

tagger_model_path = hf_hub_download(
    repo_id="skytnt/deepdanbooru_onnx", filename="deepdanbooru.onnx")

tagger_model = rt.InferenceSession(
    tagger_model_path, providers=['CPUExecutionProvider'])
tagger_model_meta = tagger_model.get_modelmeta().custom_metadata_map
tagger_tags = eval(tagger_model_meta['tags'])


@dataclass
class Tag:
    lable: str
    prob: float


def tagger_predict(image, score_threshold):
    image = np.array(image)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    s = 512
    h, w = image.shape[:-1]
    h, w = (s, int(s * w / h)) if h > w else (int(s * h / w), s)
    ph, pw = s - h, s - w
    image = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
    image = cv2.copyMakeBorder(
        image, ph // 2, ph - ph // 2, pw // 2, pw - pw // 2, cv2.BORDER_REPLICATE)
    image = image.astype(np.float32) / 255
    image = image[np.newaxis, :]
    probs = tagger_model.run(None, {"input_1": image})[0][0]
    probs = probs.astype(np.float32)
    res = []
    for prob, label in zip(probs.tolist(), tagger_tags):
        if prob < score_threshold:
            continue
        res.append(Tag(label, prob))
    sorted_res = sorted(res, key=lambda Tag: Tag.prob, reverse=True)
    output_string = ""
    output_string_without_prob = ""
    for iter in sorted_res:
        output_string += iter.lable + f" : {iter.prob:.2f}\n"
        output_string_without_prob += iter.lable + "\n"
    output_string = output_string[:-1]
    output_string_without_prob = output_string_without_prob[:-1]
    return (output_string, output_string_without_prob)


def gradio_wrapper(image, score_threshold):
    return tagger_predict(image, score_threshold)


inputs = gr.inputs.Image()
slider = gr.inputs.Slider(minimum=0, maximum=1, default=0.5)
outputs = gr.outputs.Textbox()
outputs_list = gr.outputs.Textbox()

iface = gr.Interface(fn=gradio_wrapper,
                     inputs=[inputs, slider],
                     outputs=[outputs, outputs_list])

iface.launch()
