from PyPDF2 import PdfFileWriter, PdfFileReader

out = PdfFileWriter()

file = PdfFileReader("myfile.pdf")
for idx in range(file.numPages):
    page = file.getPage(idx)
    out.addPage(page)
password = "******"
  
# Encrypt the new file with the entered password
out.encrypt(password)
# Open a new file "myfile_encrypted.pdf"
with open("myfile_encrypted.pdf", "wb") as f:
    out.write(f)
