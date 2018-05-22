"""
Objects that can be placed in a label template
"""

from PIL import Image, ImageDraw, ImageFont


class Text:
    """A simple text item"""
    def __init__(self, font: ImageFont = None) -> None:
        if font:
            self.font = font
        else:
            # fallback to default font
            self.font = ImageFont.load_default()

    def render(self, text):
        image = Image.new("1", self.font.getsize(text), "white")
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, "black", self.font)
        return image
