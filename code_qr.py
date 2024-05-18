import qrcode

# TODO: Hacer que la info entre por CLI

image = qrcode.make('https://latierramedia.com')
guardar = open("C:/Users/Usuario/Downloads/qr.png", 'wb')
image.save(guardar)