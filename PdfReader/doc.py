import minecart
import os
import PyPDF2



# making new directory if it doesn't exist
new_dir_name = 'output'
filename = './sample.pdf'

if not os.path.exists(new_dir_name):
    os.makedirs(new_dir_name + '/images')
    os.makedirs(new_dir_name + '/text')



def searchKeyword(eText,keyWord):
    pass

def searchImages(filename):
    pass






extractedText = ''

# open the target file
pdf_file = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf_file)


# printing number of pages in pdf file
pageCount = pdfReader.numPages

for i in range(pageCount):

    pageObj = pdfReader.getPage(i)
    extractedText += pageObj.extractText()
    extractedText+=' '


print(extractedText)



# closing the pdf file object
pdf_file.close()
