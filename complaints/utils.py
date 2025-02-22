import numpy as np
from sentence_transformers import SentenceTransformer
import pytesseract
from pdf2image import convert_from_path
import faiss
import pickle
from .models import DocumentChunk   
class DocumentProcessor:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.chunk_size = 512

    def extract_text(self, file_path):
        if file_path.endswith('.pdf'):
            images = convert_from_path(file_path)
            text = "\n".join(pytesseract.image_to_string(img) for img in images)
            return text.strip()
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()

    def split_text(self, text):
        return [text[i:i+self.chunk_size] for i in range(0, len(text), self.chunk_size)]

    def process_document(self, document):
        text = self.extract_text(document.file.path)
        chunks = self.split_text(text)
        
        for i, chunk in enumerate(chunks):
            embedding = self.model.encode(chunk)
            DocumentChunk.objects.create(
                document=document,
                content=chunk,
                embedding=pickle.dumps(embedding),
                chunk_index=i
            )
        
        document.processed = True
        document.save()

class QueryProcessor:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def get_relevant_chunks(self, query, top_k=3):
        # Get all chunks and convert to list
        chunks = list(DocumentChunk.objects.all())
        
        if not chunks:
            return []

        # Create embeddings array
        embeddings = np.array([pickle.loads(chunk.embedding) for chunk in chunks])
        dimension = embeddings.shape[1]
        
        # Create FAISS index
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)

        # Search for similar chunks
        query_embedding = self.model.encode(query).reshape(1, -1)
        distances, indices = index.search(query_embedding, top_k)
        
        # Convert int64 indices to Python integers and get corresponding chunks
        relevant_chunks = [chunks[int(i)].content for i in indices[0]]
        
        return relevant_chunks