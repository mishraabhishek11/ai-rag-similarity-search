import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

MODEL = os.getenv("EMBEDDING_MODEL")

 


def create_embedding(text):

    response = client.embeddings.create(
        model=MODEL,
        input=text
    )

    return response.data[0].embedding


def embed_chunks(chunks):

    embedded_chunks = []

    for chunk in chunks:

        embedding = create_embedding(
            chunk["text"]
        )

        embedded_chunks.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "embedding": embedding
        })

    return embedded_chunks

