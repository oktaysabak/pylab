from PIL import Image
import base64
import cups
from escpos.printer import Usb
p = Usb(0x04b8,0x0e15)

class UsbPrint():
    _name = 'deneme.deneme'

    
    def hello(self,args):
        image = args['receipt']
        filename = '/tmp/someImage.png'
        basewidth = 550
        receipt = image.replace('data:image/png;base64,', '')
        image = base64.b64decode(receipt)
        with open(filename, 'wb') as f:
            f.write(image)
        img = Image.open(filename)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(filename)
        p.set('LEFT')
        p.image(filename)
        p.text("\n")
        p.cut()