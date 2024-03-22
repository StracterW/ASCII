
from PIL import Image 
import torch
from torchvision import transforms

#img = Image.open("fuchs.jpg")
img = Image.open("zzPokeball.png")
factor = 1
img = img.resize(((img.size[0]//factor),(img.size[1]//factor)))
convert_tensor = transforms.ToTensor()
tensor = convert_tensor(img)
try:
    light = (tensor[0]+tensor[1]+tensor[2])/3
except:
    light = tensor[0]
file = open('symbols.txt', "w")
# mit der Methode "w" wird die gesamte Datei überschrieben
lsymb = ["##","QQ","HH","OO","II","ii","++","==","::","^^",".."]
file.write("")
for i in light:
    help = ""
    symbol = "  "
    for n in i:
        if float(n) > 0.95:
            symbol = lsymb[0]
        elif float(n) > 0.9:
            symbol = lsymb[1]
        elif float(n) > 0.8:
            symbol = lsymb[2]
        elif float(n) > 0.7:
            symbol = lsymb[3]
        elif float(n) > 0.6:
            symbol = lsymb[4]
        elif float(n) > 0.5:
            symbol = lsymb[5]
        elif float(n) > 0.4:
            symbol = lsymb[6]
        elif float(n) > 0.3:
            symbol = lsymb[7]
        elif float(n) > 0.2:
            symbol = lsymb[8]
        elif float(n) > 0.1:
            symbol = lsymb[9]
        elif float(n) > 0.01:
            symbol = lsymb[10]
        else: 
            symbol = ". "
        help +=symbol
    file.write("\n"+ str(help))
file.close()

from pathlib import Path
from pygments.formatters import ImageFormatter
import pygments.lexers

lexer = pygments.lexers.TextLexer()
png = pygments.highlight(Path('symbols.txt').read_text(), lexer, ImageFormatter(line_numbers=False))
Path('output.png').write_bytes(png)

import cv2

image = cv2.imread('output.png')
invert = cv2.bitwise_not(image)
cv2.imwrite('ZZpokeball.jpg', invert)