from app.utils.pdf_reader import pdf_reader

text = pdf_reader.read("uploads/sample.pdf")

print(text[:1000])