import PyPDF2
pdfFileObj=open('abc.pdf','rb')
pdfReader=PyPDF2.PdffileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj=pdfReader.getPage(0)
print(pageObj.extractText())
pdfFileObj.close()
