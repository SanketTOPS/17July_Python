import qrcode

qr=qrcode.make("https://www.tops-int.com/")
qr.save("tops.png")