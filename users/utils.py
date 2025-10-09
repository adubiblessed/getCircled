import qrcode, os
from django.conf import settings

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    directory = os.path.join(settings.MEDIA_ROOT, 'qr_codes')
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, file_path)
    img.save(file_path)

    # Return the relative path (for ImageField)
    return f"qr_codes/{file_path}"
