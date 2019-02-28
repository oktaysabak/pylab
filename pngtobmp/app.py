from PIL import Image
filename = 'test'
png = Image.open(filename)
png = png.resize((75,75), Image.ANTIALIAS)
new_png = png.convert("1")
new_png.save(filename+'.bmp')
