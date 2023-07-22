import qrcode as qr
data=input("Enter the text or link: ")
img=qr.make(data)
img.save("qr.png")