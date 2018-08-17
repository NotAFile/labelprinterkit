"""
Objects that can be placed in a label template
"""

from PIL import Image, ImageDraw, ImageFont


class Text:
    """A simple text item"""
    def __init__(self, font: ImageFont = None, **kwargs) -> None:
        if font:
            self.font = font
        else:
            # fallback to default font
            self.font = ImageFont.load_default()

        self.pad_top = kwargs.get("pad_top", 0)
        self.pad_right = kwargs.get("pad_right", 0)
        self.pad_bottom = kwargs.get("pad_bottom", 0)
        self.pad_left = kwargs.get("pad_left", 0)

    def render(self, text):
        text_x, text_y = self.font.getsize(text)
        padded_size = (
            text_x + self.pad_left + self.pad_right,
            text_y + self.pad_top + self.pad_bottom,
        )
        image = Image.new("1", padded_size, "white")
        draw = ImageDraw.Draw(image)
        draw.text((self.pad_left, self.pad_top), text, "black", self.font)
        return image
