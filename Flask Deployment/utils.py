from PIL.Image import open
from io import BytesIO
from base64 import b64encode,b64decode


def pil_image_to_base64(pil_image):
    buf = BytesIO()
    pil_image.save(buf, format="JPEG")
    return b64encode(buf.getvalue())


def base64_to_pil_image(base64_img):
    return open(BytesIO(b64decode(base64_img)))
