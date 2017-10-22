import os
from os import path
from PIL import Image
import qrtools
import pyqrcode

filename= "\\bhimqr.jpg"
file = "\\testing"
dirpath = path.join(path.dirname(path.realpath(os.curdir)))
oldimagefile = path.join(dirpath + filename)

qr = qrtools.QR()
qr.decode(oldimagefile)
print(qr.data)

text = ""
with open(path.join(dirpath + file)) as testfile:
    text = testfile.read()

newqr = pyqrcode.create(text)

newqrfile = "\\download_20171021_225404.png"
newimagefile = path.join(dirpath + newqrfile)
newqr.png( newimagefile ,scale=6)

qr.decode(newimagefile)
print(qr.data);