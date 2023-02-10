import pyqrcode
import io


def generate_qr_code(url_link: str):

    url = pyqrcode.create(url_link)
    buffer = io.BytesIO()
    url.png(buffer)
    photo = buffer.getvalue()
    return photo





