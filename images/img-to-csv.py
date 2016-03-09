from PIL import Image
im = Image.open('wasp1.png')
 
pixels = list(im.getdata())
width, height = im.size 
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
print pixels
import json
with open('wasp1.json', 'w') as outfile:
    json.dump(pixels, outfile)