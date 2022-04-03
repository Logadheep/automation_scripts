from PyPDF2 import PdfFileWriter, PdfFileReader

out = PdfFileWriter()
file = PdfFileReader("myfile_encrypted.pdf")

password = "******"
if file.isEncrypted:
    file.decrypt(password)
    for idx in range(file.numPages):
        page = file.getPage(idx)
        out.addPage(page)
    with open("myfile_decrypted.pdf", "wb") as f:
        out.write(f)
    print("File decrypted Successfully.")
else:
    print("File already decrypted.")