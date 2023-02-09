import pyqrcode


def generate_qr_code(url_link):
    qr_code = pyqrcode.create(url_link)
    qr_code.png(f'qr_{url_link}', scale=6)

