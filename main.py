from pdf2docx import Converter

pdf_input = 'sample.pdf'
docx_output = 'sample.docx'

cv = Converter(pdf_input)
cv.convert(docx_output)
cv.close()


