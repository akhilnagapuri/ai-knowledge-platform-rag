from app.utils.pdf_reader import pdf_reader
from app.utils.text_chunker import text_chunker

text = pdf_reader.read("uploads/sample.pdf")

chunks = text_chunker.chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])
print("\nsecond chunk:\n")
print(chunks[1])
print("\nsixth chunk:\n")
print(chunks[5])