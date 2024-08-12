import pyqrcode

url="https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/"

qr=pyqrcode.create(url)
qr.png("g4g.png")
