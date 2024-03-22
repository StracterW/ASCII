
from PIL import Image 
import torch
from torchvision import transforms

img = Image.open("image.jpg") 
convert_tensor = transforms.ToTensor()  # convert image to tensor
tensor = convert_tensor(img)
try:
    light = (tensor[0]+tensor[1]+tensor[2])/3       # brightness of the image 
except:
    light = tensor[0]
file = open('symbols.txt', "w")
lsymb = ["##","HH","OO","II","ii","==","::","..", ". "]   # Symbols for specific brightness
file.write("")
for i in light:
    help = ""
    symbol = "  "
    for n in i:
        if float(n) > 0.9:
            symbol = lsymb[0]
        elif float(n) > 0.8:
            symbol = lsymb[1]
        elif float(n) > 0.7:
            symbol = lsymb[2]
        elif float(n) > 0.6:
            symbol = lsymb[3]
        elif float(n) > 0.5:
            symbol = lsymb[4]
        elif float(n) > 0.3:
            symbol = lsymb[5]
        elif float(n) > 0.2:
            symbol = lsymb[6]
        elif float(n) > 0.1:
            symbol = lsymb[7]
        else: 
            symbol = lsymb[8]
        help +=symbol
    file.write("\n"+ str(help))
file.close()

from pathlib import Path
from pygments.formatters import ImageFormatter
import pygments.lexers

lexer = pygments.lexers.TextLexer()
png = pygments.highlight(Path('symbols.txt').read_text(), lexer, ImageFormatter(line_numbers=False))     #text file to png
Path('output.png').write_bytes(png)

import cv2

image = cv2.imread('output.png')
invert = cv2.bitwise_not(image)
cv2.imwrite('result.jpg', invert)             # switch white and black
