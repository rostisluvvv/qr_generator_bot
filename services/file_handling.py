import pyqrcode
import io


def generate_qr_code(url_link: str):
    qr_code = pyqrcode.create(url_link)
    buffer = io.BytesIO()
    qr_code.png(buffer, scale=6)
    photo = buffer.getvalue()
    return photo