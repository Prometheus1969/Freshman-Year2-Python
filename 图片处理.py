#图片处理.py
#库导入

from PIL import Image
from PIL import ImageFilter

#打开图片

im = Image.open("samp.jpg")
print("读取中")

#图片处理

im1 = im.filter(ImageFilter.CONTOUR)

#命名

name = input("请输入要保存图片名称：")

#保存

im1.save("{}.jpg".format(name))
print("操作结束")
