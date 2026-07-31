# Import helper functions
from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
# Import Pinecone
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

from dotenv import load_dotenv
import os
import time


# Load Environment Variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if PINECONE_API_KEY is None:
    raise ValueError("PINECONE_API_KEY not found")

# Load PDF Documents
print("Loading PDF...")
documents = load_pdf_file(data="Data/")
print("Documents:", len(documents))

# Split Documents into Chunks
print("Splitting documents...")
text_chunks = text_split(documents)
print("Total Chunks:", len(text_chunks))

# Load HuggingFace Embedding Model
print("Loading Embedding Model...")
embeddings = download_hugging_face_embeddings()

# Connect to Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medicalbot"

# Create Index (if not exists)
existing_indexes = [i["name"] for i in pc.list_indexes()]
if index_name not in existing_indexes:

    print("Creating Index...")

    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

    while True:
        status = pc.describe_index(index_name).status["ready"]
        if status:
            break
        print("Waiting for index...")
        time.sleep(2)

else:
    print("Index already exists.")

# Upload Embeddings to Pinecone
batch_size = 100
print("Uploading documents...")
for i in range(0, len(text_chunks), batch_size):

    batch = text_chunks[i:i + batch_size]
    PineconeVectorStore.from_documents(
        documents=batch,
        embedding=embeddings,
        index_name=index_name
    )

    print(f"Uploaded {min(i+batch_size,len(text_chunks))}/{len(text_chunks)}")
print("\nAll Documents Uploaded Successfully.")