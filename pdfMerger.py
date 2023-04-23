# pip install PyPDF2
import PyPDF2

pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
pdf_merger = PyPDF2.PdfFileMerger() # Create an instance of PdfFileMerger class

# Add each PDF file to the merger object
for pdf_file in pdf_files:
    with open(pdf_file, "rb") as f:
        pdf_merger.append(PyPDF2.PdfFileReader(f))

# Write the merged PDF file to disk
with open("merged_file.pdf", "wb") as f:
    pdf_merger.write(f)
