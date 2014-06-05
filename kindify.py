import sys

if __name__ == '__main__' and len(sys.argv) > 0 and sys.argv[1][-3:].upper() == 'PDF':
	original = sys.argv[1]
	target = original[:-4] + '-kindified.pdf'
	
	from pyPdf import PdfFileWriter, PdfFileReader
	output = PdfFileWriter()
	input1 = PdfFileReader(file(original, "rb"))
	numPages = input1.getNumPages()
	# print the title of document1.pdf
	# print "title = %s" % (input1.getDocumentInfo().title)
	print "Number Of Pages:"
	print numPages
	print "Select Profile to crop"
	print "1. Orielly"
	print "2. Dummies"
	print "3. Make guides"
	print "4. Evil Genius"
	print "5. Custom"
	ch=raw_input("Enter Now ")
	if ch=='1':
		top=45
		bottom=35
		right=65
		left=65
	elif ch=='2':
		top=40
		bottom=57
		right=52
		left=52
	elif ch=='3':
		top=30
		bottom=50
		right=40
		left=40
	elif ch=='4':
		top=40
		bottom=50
		right=65
		left=60
	elif ch=='5':
		top=int(raw_input("Enter Top margin in px \n"))
		bottom=int(raw_input("Enter Bottom margin in px \n"))
		right=int(raw_input("Enter Right margin in px \n"))
		left=int(raw_input("Enter left margin in px \n"))
	for i in range(numPages):
		    page = input1.getPage(i)
		    print page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y()
		    page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right, page.mediaBox.getUpperRight_y() - top)
		    page.mediaBox.lowerLeft  = (page.mediaBox.getLowerLeft_x()  + left,  page.mediaBox.getLowerLeft_y()  + bottom)
		    output.addPage(page)
    
outputStream = file(target, "wb")
output.write(outputStream)
outputStream.close()
