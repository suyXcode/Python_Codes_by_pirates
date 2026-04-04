import pyqrcode
from pyqrcode import QRCode
#text or url to encode
s = "https://www.youtube.com/"
# create the qr code that you want to save
url = pyqrcode.create(s)
# save the qr code generated
url.svg("Qr_Generator/youtube.svg", scale = 8)

# save as png file
url.png("Qr_Generator/youtube.png", scale = 6)
