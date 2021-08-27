from pdfrw import PdfReader
from pagelabels import PageLabels

reader = PdfReader("CMI_clase2.pdf")
labels = PageLabels.from_pdf(reader)
pageAmount = len(reader.pages)

pages = [i.startpage for i in labels]
pages.append(pageAmount)
print(pages)

