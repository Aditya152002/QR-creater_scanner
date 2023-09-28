import qrcode
# QR code generator is here
class Creator:
    def qrcreator(qrdetail):
        qr = qrcode.QRCode(
            version=10,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=10,
            mask_pattern=7,
        )
        qr.add_data(qrdetail)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        return img.save("static/qrcode.png")

#QR code Scanner is here
class scanner():
    def qrscanner(scaned_img):
        pass