from pdfrw import PdfReader, PdfWriter
from pagelabels import PageLabels

reader = PdfReader("CMI_clase2.pdf")
labels = PageLabels.from_pdf(reader)

pages = reader.pages
pageAmount = len(pages)

pageLabels = [i.startpage for i in labels][1:]
pageLabels.append(pageAmount)
print(pageLabels)

outdata = PdfWriter("out.pdf")
for p in pageLabels:
    outdata.addpage(pages[p-1])

outdata.write()

