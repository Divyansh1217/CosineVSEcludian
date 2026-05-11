import faiss
from typing import List

class LocalVectorStore:
    def __init__(self, dimension: int):
        # Inner Product acts as Cosine Similarity when vectors are L2 normalized
        self.index = faiss.IndexFlatIP(dimension) 
        self.documents = []

    def add(self, embeddings, texts: List[str]):
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings)
        self.documents.extend(texts)

    def search(self, query_embedding, top_k: int = 3) -> List[str]:
        faiss.normalize_L2(query_embedding)
        distances, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for i in indices[0]:
            if i != -1 and i < len(self.documents):
                results.append(self.documents[i])
        return results