import PyPDF2
import os

merger = PyPDF2.PdfMerger()

# (1). "Rename_Folder" is where your ".pdf" archives need to be.
# (2). This part will sort your archives in sequence (numeric)

archiv_list = os.listdir("Rename_folder")
archiv_list.sort()
print(archiv_list)

# (1).

for archive in archiv_list:
    if '.pdf' in archive:
        merger.append(f"Rename_folder/{archive}")
        
# (3). You can RENAME your "file.pdf" here.
merger.write("Rename_or_not_Final_PDF.pdf")
