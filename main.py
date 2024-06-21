import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('00020126580014BR.GOV.BCB.PIX0136f699e909-3248-4909-8078-326a8868ecf15204000053039865802BR5925Rudimacy Allen Duprat Car6009SAO PAULO62140510NY0kvOaKS06304DD48')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.pix.png")