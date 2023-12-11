import os
from PIL import Image
import asyncio
from pix2tex.cli import LatexOCR

async def process_image(image_path):
    latex_ocr = Image.open(image_path)
    model = LatexOCR()
    print(model(latex_ocr))
    return latex_ocr

def run_process_image(image_path):
    return asyncio.run(process_image(image_path))

run_process_image("app/services/physics_equation.png")
