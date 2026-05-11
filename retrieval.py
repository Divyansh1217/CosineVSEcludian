from embedding import LocalEmbedder
from storage import LocalVectorStore
from typing import List

class MockGenerativeModel:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate_content(self, prompt: str) -> str:
        prompt_lower = prompt.lower()
        if "peak load" in prompt_lower:
            return "How does the system handle peak load? scaling, load balancing, high traffic, distributed throughput"
        elif "database node fails" in prompt_lower:
            return "What happens when a database node fails? fault tolerance, replication, failover, disaster recovery, raft consensus"
        elif "latency" in prompt_lower:
            return "Ways to reduce latency for global users? edge caching, CDN, geographic routing, connection pooling"
        return prompt

class ContextAwareRetrievalEngine:
    def __init__(self):
        self.embedder = LocalEmbedder()
        self.store = LocalVectorStore(self.embedder.dimension)
        self.llm = MockGenerativeModel("gemini-pro") 

    def ingest(self, texts: List[str]):
        embeddings = self.embedder.encode(texts)
        self.store.add(embeddings, texts)

    def strategy_a_search(self, query: str) -> List[str]:
        query_emb = self.embedder.encode([query])
        return self.store.search(query_emb)

    def strategy_b_search(self, query: str) -> List[str]:
        expanded_query = self.llm.generate_content(f"Expand query: {query}")
        expanded_emb = self.embedder.encode([expanded_query])
        return self.store.search(expanded_emb)