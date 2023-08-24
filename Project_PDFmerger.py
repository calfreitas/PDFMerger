import PyPDF2
import os

merger = PyPDF2.PdfMerger()

archiv_list = os.listdir("archives")
archiv_list.sort()
print(archiv_list)

for archive in archiv_list:
    if '.pdf' in archive:
        merger.append(f"archives/{archive}")

merger.write("PDF Final.pdf")