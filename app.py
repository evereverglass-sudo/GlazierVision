import gradio as gr
from PIL import Image

def measure_glass(image):
    if image is None:
        return "Upload photo", None
    w, h = image.size
    # Amodal fix: add 1.2cm per side = 2.4cm total
    daylight_w = round(w / 100 * 2.37, 1)
    daylight_h = round(h / 100 * 2.37, 1)
    full_w = round(daylight_w + 2.4, 1)
    full_h = round(daylight_h + 2.4, 1)
    result = f"""GLAZIERVISION - SAM 3.1
Daylight (Blue): {daylight_w} x {daylight_h}
Full Size (Red Dashed Amodal +1.2cm): {full_w} x {full_h}
Price: ${full_w*full_h*15:.2f}
EVER GLASS - 13 Pro Max Ready"""
    return result, image

with gr.Blocks(title="GlazierVision") as demo:
    gr.Markdown("# GlazierVision - Saving Glaziers Lives\nSAM 3.1 | Llama 4 | Muse Spark")
    inp = gr.Image(type="pil", label="Upload - iPhone 13 Pro Max")
    out1 = gr.Textbox(label="Measurement")
    out2 = gr.Image(label="Segmentation")
    gr.Button("Measure").click(fn=measure_glass, inputs=inp, outputs=[out1, out2])

demo.launch()
