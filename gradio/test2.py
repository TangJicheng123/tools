import gradio as gr


def test2(input):
    print(input)
    return "/Users/tangjicheng/tools/gradio/hello.py"


input_text = gr.Textbox(label="haha_text")
output_file = gr.File(label="file_out")

app = gr.Interface(fn=test2, inputs=input_text, outputs=output_file)

app.launch()
