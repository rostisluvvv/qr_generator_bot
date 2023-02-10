import pyqrcode
import io


def generate_qr_code(url_link: str):

    url = pyqrcode.create(url_link)
    buffer = io.BytesIO()
    url.png(buffer)
    photo = buffer.getvalue()
    # qr_name = ''.join(e for e in url_link if e.isalnum())
    return photo


print(generate_qr_code('https://github.com/rostisluvvv'))


