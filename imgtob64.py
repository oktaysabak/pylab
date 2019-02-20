# -*- coding: utf-8 -*-

import base64
import time
from random import randint
with open('imagebase64.txt','rb') as f:
    img_data = f.read()

with open("imageToSave" + str( randint(0,round(time.time()/1*60))) + '.png', "wb") as fh:
    fh.write(base64.decodebytes(img_data))

