import gradio as gr

def get_png_meta_info(image):
    return image.info

# 创建Gradio界面
input_image = gr.inputs.Image(type='pil')
output_text = gr.outputs.Textbox()
interface = gr.Interface(fn=get_png_meta_info, inputs=input_image, outputs=output_text)

# 运行Gradio界面
interface.launch()
