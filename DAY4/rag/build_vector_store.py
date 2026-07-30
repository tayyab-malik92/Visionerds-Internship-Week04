import os
import pickle

from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer


# -----------------------------
# Configuration
# -----------------------------

PDF_FOLDER = "rag/documents"

CHUNK_SIZE = 500

MODEL_NAME = "all-MiniLM-L6-v2"


# -----------------------------
# Load Embedding Model
# -----------------------------

print("Loading embedding model...")

model = SentenceTransformer(MODEL_NAME)


# -----------------------------
# Read PDFs
# -----------------------------

documents = []

for file in os.listdir(PDF_FOLDER):

    if file.endswith(".pdf"):

        path = os.path.join(PDF_FOLDER, file)

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        documents.append(text)

print(f"Loaded {len(documents)} PDF(s).")


# -----------------------------
# Chunk Documents
# -----------------------------

chunks = []

for document in documents:

    for i in range(0, len(document), CHUNK_SIZE):

        chunk = document[i:i + CHUNK_SIZE].strip()

        if chunk:

            chunks.append(chunk)

print(f"Created {len(chunks)} chunks.")


# -----------------------------
# Generate Embeddings
# -----------------------------

print("Generating embeddings...")

embeddings = model.encode(
    chunks,
    show_progress_bar=True
)

print("Embeddings generated.")


# -----------------------------
# Save Files
# -----------------------------

with open("rag/chunks.pkl", "wb") as f:

    pickle.dump(chunks, f)


with open("rag/vector_store.pkl", "wb") as f:

    pickle.dump(embeddings, f)


print("\nDone!")
print("Saved:")
print(" - rag/chunks.pkl")
print(" - rag/vector_store.pkl")