# import qrcode
import segno

# qr = qrcode.make("kiyakeynia@gmail.com")

# qr.save("Assignment 9/qrcode.png")

qr = segno.make("kiyakeynia@gmail.com")

qr.save('Assignment 9/qrcode.png', dark='darkblue', light='lightblue', scale=10)