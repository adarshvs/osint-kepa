from PyPDF2 import PdfFileReader
from PIL import Image
from tinytag import TinyTag
class PdfMeta:
    def pdf_metadata(self):
        pdf_toread = PdfFileReader(open(self.path, "rb"))
        pdf_info = pdf_toread.getDocumentInfo()
        return pdf_info
    def __init__(self, path):
        self.path = path

class ImgMeta:
    def image_metadata(self):
        image = Image.open(self.path)
        image.verify()
        return image.getexif()
    def __init__(self, path):
            self.path = path

class MultiMediaMeta:
    def multimedia_meta(self):
        try:
            media_meta = TinyTag.get(self.path)
        except :
            media_meta = "file type not supported"

        return media_meta
    def __init__(self, path):
        self.path = path


