
from io import BytesIO
import warnings
from fastai.vision.all import PILImage
def open_image(fn:str)->PILImage:
    "Return `Image` object created from image in file `fn`."
    return PILImage.create(fn)

async def get_uploaded_image(request):
    data = await request.form()
    img_bytes = await (data['file'].read())
    img = open_image(BytesIO(img_bytes))
    return img


__all__ = ['get_uploaded_image']