import pytest
from retrieval import ContextAwareRetrievalEngine, MockGenerativeModel

@pytest.fixture
def engine():
    eng = ContextAwareRetrievalEngine()
    eng.ingest([
        "Auto-scaling handles high traffic.",
        "Raft consensus handles failover.",
        "CDNs reduce geographic latency."
    ])
    return eng

def test_ingestion(engine):
    # FIXED: We now access documents and index through the 'store' module
    assert len(engine.store.documents) == 3
    assert engine.store.index.ntotal == 3

def test_strategy_a(engine):
    results = engine.strategy_a_search("peak load")
    assert len(results) > 0
    assert isinstance(results[0], str)

def test_mock_generative_model():
    mock_llm = MockGenerativeModel("mock")
    expanded = mock_llm.generate_content("peak load")
    assert "scaling" in expanded

def test_strategy_b(engine):
    results = engine.strategy_b_search("database node fails")
    assert len(results) > 0