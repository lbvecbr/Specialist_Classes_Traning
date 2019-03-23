from PIL import Image, ImageDraw, ImageFont

A4_V = (620, 877)
A4_H = (877, 620)

img = Image.new('RGB', A4_V, color='white')
v_center = img.width/2
left_side = img.width/16

text = 'im – The image to draw in.\n\
mode – Optional mode to use for color\n values. For RGB images, this argument can be RGB or \nRGBA (to blend the drawing into the image). \nFor all other modes, this argument must be the same as the image mode. If omitted,\n the mode defaults to the mode of the \nimage.'

print(img.format, img.size, img.mode)

draw = ImageDraw.Draw(img)
font_large = ImageFont.truetype("C:\\WINDOWS\\FONTS\\TIMES.TTF", 12)
font_small = ImageFont.truetype("C:\\WINDOWS\\FONTS\\TIMES.TTF", 26)
WHITE = 0, 255, 255
YELLOW = 255, 255, 0
draw.line([(left_side, 50), (left_side, 100)], fill=YELLOW, width=2)
draw.multiline_text((left_side, 100), text, WHITE, font=font_large, align='center')
draw.text((60, 300), "@32secondsofcode", YELLOW, font=font_small)
img.save('with-text.png')
img.show()
