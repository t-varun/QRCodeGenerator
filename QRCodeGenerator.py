import pyqrcode
e = pyqrcode.create(input("Enter a String: "))
e.png('QR.png',scale=6)
