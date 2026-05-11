Context-Aware Retrieval Engine

This is my submission for the Senior Gen AI Engineering assessment. 

I built this local Retrieval-Augmented Generation (RAG) pipeline to test out a pretty interesting question: **Does a vector database retrieve better results if we let an LLM rewrite the user's prompt first?** This repo sets up a local environment to benchmark "Raw Vector Search" against an "AI-Enhanced Query Expansion" strategy. 

How to Run It
 pytest test_rag_pipeline.py  
 python -m main



Why Cosine Similarity? (And not Euclidean)
For the vector math, I went with Cosine Similarity (implemented via FAISS IndexFlatIP using L2-normalized vectors).
Honestly, for text embeddings, Cosine is almost always the right call over Euclidean distance. Here's my thought process on why:
Meaning is about direction, not length: Cosine measures the angle between two vectors. This brilliantly captures their semantic relationship regardless of how long the actual text chunks are.
Euclidean gets confused by text length: Euclidean distance measures the literal straight-line distance in vector space. If you have a short search query and a massive paragraph that mean the exact same thing, Euclidean distance might incorrectly push them far apart just because their magnitudes are so different. Cosine keeps them tightly clustered.
The GCP Production Roadmap
Right now, this is a local prototype using sentence-transformers and an in-memory FAISS index. To migrate this stack to a production-grade Google Cloud environment, here is my step-by-step plan:
Swap the Embedder: I'd drop the local sentence-transformers library and hook up the official  SDK.
Code: TextEmbeddingModel.from_pretrained("textembedding-gecko")
Upgrade the Query Expander: Swap out my MockGenerativeModel for a live production Gemini model via  to handle real-world query expansion.
Code: GenerativeModel("gemini-1.5-pro")
Migrate Storage to  Vector Search: * Instead of holding vectors in RAM, I would run a batch job to format the document chunks and embeddings into JSONL files.
Push those files to a Google Cloud Storage (GCS) bucket.
Create a Vector Search Index pointing to that GCS bucket. I'd configure it to use the DOT_PRODUCT_DISTANCE algorithm (which gives us our preferred Cosine similarity).
Finally, deploy that Index to an IndexEndpoint so our backend can query it with sub-millisecond latency at scale!
