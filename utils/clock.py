import os
from datetime import datetime
from PIL import ImageFont

#Font helper
def make_font(name, size):
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fonts", name))
    return ImageFont.truetype(font_path, size)

clockFont = make_font("FreePixel.ttf", 30)
def showClock(draw, width, height):
    current_time = datetime.now().strftime("%I:%M%p")
    draw.text((10,20), current_time, fill="white", font=clockFont)
