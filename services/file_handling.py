import pyqrcode



def generate_qr_code(url_link: str):
    qr_code = pyqrcode.create(url_link)
    qr_name = ''.join(e for e in url_link if e.isalnum())
    qr_code.png(f'{qr_name}.png', scale=6)
    return f'C:\Dev\8qr_generator_bot\services\{qr_name}.png'




