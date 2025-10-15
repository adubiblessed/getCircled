import qrcode, os
from PIL import Image
from PIL.Image import Resampling as ImageResampling
from django.conf import settings

def generate_qr_code(data, filename, logo_path=None):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')




    directory = os.path.join(settings.MEDIA_ROOT, 'qr_codes')
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, filename)
    img.save(file_path)

    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)
        # Resize logo (max 20% of QR code width)
        qr_width, qr_height = img.size
        logo_size = int(qr_width * 0.2)
        logo = logo.resize((logo_size, logo_size), ImageResampling.LANCZOS)

        # Calculate position to paste the logo in the center
        pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        img.paste(logo, pos, mask=logo if logo.mode=='RGBA' else None)

    img.save(file_path)
    # Return the relative path (for ImageField)
    return f"qr_codes/{filename}"
