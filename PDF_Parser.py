import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
 
class PDF_Text_Extraction():
    def __init__(self, file_name):
        self.file_name = file_name

    def text_extraction(self):
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)

        with open(self.file_name, 'rb') as fh:
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                page_interpreter.process_page(page)

        self.text = fake_file_handle.getvalue()
        converter.close()
        fake_file_handle.close()

    def assign_text(self):
        text_storage = self.text
        #print(text_storage)
        return text_storage
    
    def execute(self):
        self.text_extraction()
        self.assign_text()

'''
import PyPDF2

file_object = open("file1.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(file_object)
pageObj = pdfReader.getPage(0)
text = pageObj.extractText()

word = []
for i in range(len(text)):
    if text[i] != " ":
        word.append(text[i])
    else:
        phrase = " ".join(word)
        word = []
        print(phrase)
'''

