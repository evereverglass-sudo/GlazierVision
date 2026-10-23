# GlazierVision - Meta AI Hackathon 2026
# Step 1: SAM 3.1 Glass Measurement Prototype

import gradio as gr
from PIL import Image

def measure_glass(image):
    # TODO: Add SAM 3.1 segmentation here (starts Oct 26)
    # For now: demo placeholder
    w, h = image.size
    # Assume credit card reference = 3.37 inches
    estimated_width = round(w / 100 * 3.37, 2)
    estimated_height = round(h / 100 * 3.37, 2)
    
    result = f"""
    GLAZIERVISION RESULT:
    - Detected Frame: Yes (SAM 3.1 will do this)
    - Width: {estimated_width} inches
    - Height: {estimated_height} inches
    - Suggested Glass: Double Pane Low-E
    - Quote: ${estimated_width * estimated_height * 2.5:.2f}
    """
    return result, image

with gr.Blocks(title="GlazierVision") as demo:
    gr.Markdown("# GlazierVision - Measure Glass from Photo")
    gr.Markdown("Upload window photo with credit card for scale - SAM 3.1 Powered")
    
    inp = gr.Image(type="pil", label="Window Photo")
    out_text = gr.Textbox(label="Measurement")
    out_img = gr.Image(label="Segmented")
    
    btn = gr.Button("Measure")
    btn.click(measure_glass, inputs=inp, outputs=[out_text, out_img])

demo.launch()