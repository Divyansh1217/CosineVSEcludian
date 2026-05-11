import json
from retrieval import ContextAwareRetrievalEngine

def generate_benchmark_report():
    engine = ContextAwareRetrievalEngine()
    
    sample_data = [
        "The system utilizes an API gateway pattern to route incoming requests to various microservices.",
        "To manage high traffic and distributed throughput, auto-scaling groups deploy additional instances when CPU utilization exceeds 70%.",
        "Data is sharded across multiple regional clusters to ensure compliance and reduce lookup times.",
        "In the event of a crash, the raft consensus algorithm ensures a standby replica is promoted to primary within 500ms.",
        "Static assets are pushed to a global Content Delivery Network (CDN) to ensure quick load times regardless of geographic location.",
        "Database connections are pooled at the middleware layer to prevent exhausting the Postgres connection limit."
    ]
    engine.ingest(sample_data)

    queries = [
        "How does the system handle peak load?", 
        "What happens when a database node fails?",
        "Ways to reduce latency for global users?"
    ]

    report = {}
    for q in queries:
        report[q] = {
            "Strategy A (Raw)": engine.strategy_a_search(q),
            "Strategy B (Expanded)": engine.strategy_b_search(q)
        }
    
    with open("retrieval_benchmark.md", "w") as f:
        f.write("# Strategy A vs Strategy B Comparison\n\n")
        f.write("```json\n")
        f.write(json.dumps(report, indent=4))
        f.write("\n```")

if __name__ == "__main__":
    generate_benchmark_report()