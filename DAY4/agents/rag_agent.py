import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

from llm import ask_llm


# -----------------------------
# Load Model
# -----------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------------
# Load Vector Store
# -----------------------------

with open("rag/vector_store.pkl", "rb") as f:
    vectors = pickle.load(f)

with open("rag/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


# -----------------------------
# Cosine Similarity
# -----------------------------

def cosine_similarity(a, b):

    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) *
        np.linalg.norm(b)
    )


# -----------------------------
# Retrieve Top-K Chunks
# -----------------------------

def retrieve(query, top_k=3):

    query_embedding = model.encode(query)

    scores = []

    for vector in vectors:
        scores.append(
            cosine_similarity(query_embedding, vector)
        )

    indices = np.argsort(scores)[::-1][:top_k]

    return [chunks[i] for i in indices]


# -----------------------------
# Public Function
# -----------------------------

def answer(question):

    context = retrieve(question)

    context = "\n\n".join(context)

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
"""

    return ask_llm(prompt)