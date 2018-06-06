from PIL import Image
from PIL import ImageFilter
im = Image.open("qie.jpg")
e = im.filter(ImageFilter.CONTOUR)
e.save("e.jpg")
