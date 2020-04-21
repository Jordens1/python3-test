'''
when a dir has a  __init__.py    is called a package

'''
from PIL import Image


im = Image.open('test.jpg')

print(im.format, im.size, im.mode)

im.thumbnail((2000, 1500))

im.save('test3.jpg')







































