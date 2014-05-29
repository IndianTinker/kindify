#Make ones work well

from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(file("kivy.pdf", "rb"))
numPages = input1.getNumPages()
# print the title of document1.pdf
print "title = %s" % (input1.getDocumentInfo().title)
print numPages
top=30
bottom=50
right=40
left=40
for i in range(numPages):
    page = input1.getPage(i)
    print page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y()
    page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right, page.mediaBox.getUpperRight_y() - top)
    page.mediaBox.lowerLeft  = (page.mediaBox.getLowerLeft_x()  + left,  page.mediaBox.getLowerLeft_y()  + bottom)
    output.addPage(page)
    
outputStream = file("kindified-output.pdf", "wb")
output.write(outputStream)
outputStream.close()
