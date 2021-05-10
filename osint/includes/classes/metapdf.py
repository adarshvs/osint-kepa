from PyPDF2 import PdfFileReader
class PdfMeta:
    def pdf_metadata(self):
        pdf_toread = PdfFileReader(open(self.path, "rb"))
        pdf_info = pdf_toread.getDocumentInfo()
        return pdf_info
    def __init__(self, path):
        self.path = path

