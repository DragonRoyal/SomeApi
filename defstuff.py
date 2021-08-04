import random
from PIL import Image, ImageDraw, ImageFilter
def skewupper():
    low = 0
    high = 100
    mode = 80
    return random.triangular(low, high, mode)
  
def skewlower():
    low = 0
    high = 100
    mode = 20
    return random.triangular(low, high, mode)
      
# Function to convert into spongemock
# with more upper case charcters
def spongemockupper(input_text):
    output_text = ""
    for char in input_text:
        if char.isalpha():
            if skewupper() > 50:
                output_text += char.upper()
            else:
                output_text += char.lower()
        else:
            output_text += char
    return output_text
  
# Function to convert into spongemock
# with more lower case charcters
def spongemocklower(input_text):
    output_text = ""
    for char in input_text:
        if char.isalpha():
            if skewlower() > 50:
                output_text += char.upper()
            else:
                output_text += char.lower()
        else:
            output_text += char
    return output_text
  
def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    result = pil_img.copy()
    result.putalpha(mask)

    return result


