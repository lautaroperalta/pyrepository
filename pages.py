import PyPDF2

def getLimit_File(pag):
    splitpage = pag.split("\n")
    numberstr = splitpage.pop(-2)
    number = int(numberstr.split('/')[1])
    return number+1

pdf_file = open('/home/lautaro/Descargas/CMI_clase2.pdf','rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
i=0
mainpage = read_pdf.getPage(0)
paginasFinal = [None]*getLimit_File(mainpage.extractText())
while(i < number_of_pages):
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    splitpage = page_content.split("\n")
    numberstr = splitpage.pop(-2)
    number = int(numberstr.split('/')[0])
    paginasFinal[number] = str(i+1)
    i += 1
paginasFinal.pop(0)    
print(','.join(paginasFinal))

