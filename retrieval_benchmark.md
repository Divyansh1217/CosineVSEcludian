# Strategy A vs Strategy B Comparison

```json
{
    "How does the system handle peak load?": {
        "Strategy A (Raw)": [
            "To manage high traffic and distributed throughput, auto-scaling groups deploy additional instances when CPU utilization exceeds 70%.",
            "In the event of a crash, the raft consensus algorithm ensures a standby replica is promoted to primary within 500ms.",
            "Static assets are pushed to a global Content Delivery Network (CDN) to ensure quick load times regardless of geographic location."
        ],
        "Strategy B (Expanded)": [
            "To manage high traffic and distributed throughput, auto-scaling groups deploy additional instances when CPU utilization exceeds 70%.",
            "In the event of a crash, the raft consensus algorithm ensures a standby replica is promoted to primary within 500ms.",
            "The system utilizes an API gateway pattern to route incoming requests to various microservices."
        ]
    },
    "What happens when a database node fails?": {
        "Strategy A (Raw)": [
            "Database connections are pooled at the middleware layer to prevent exhausting the Postgres connection limit.",
            "In the event of a crash, the raft consensus algorithm ensures a standby replica is promoted to primary within 500ms.",
            "Data is sharded across multiple regional clusters to ensure compliance and reduce lookup times."
        ],
        "Strategy B (Expanded)": [
            "In the event of a crash, the raft consensus algorithm ensures a standby replica is promoted to primary within 500ms.",
            "Data is sharded across multiple regional clusters to ensure compliance and reduce lookup times.",
            "Database connections are pooled at the middleware layer to prevent exhausting the Postgres connection limit."
        ]
    },
    "Ways to reduce latency for global users?": {
        "Strategy A (Raw)": [
            "To manage high traffic and distributed throughput, auto-scaling groups deploy additional instances when CPU utilization exceeds 70%.",
            "Static assets are pushed to a global Content Delivery Network (CDN) to ensure quick load times regardless of geographic location.",
            "Data is sharded across multiple regional clusters to ensure compliance and reduce lookup times."
        ],
        "Strategy B (Expanded)": [
            "Static assets are pushed to a global Content Delivery Network (CDN) to ensure quick load times regardless of geographic location.",
            "To manage high traffic and distributed throughput, auto-scaling groups deploy additional instances when CPU utilization exceeds 70%.",
            "Data is sharded across multiple regional clusters to ensure compliance and reduce lookup times."
        ]
    }
}
```