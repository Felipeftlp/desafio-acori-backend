from fastapi.testclient import TestClient
from app.main import app
import app.routes as routes

client = TestClient(app)


def test_ask(monkeypatch):
    class FakeChain:
        def invoke(self, question):
            return "Resposta simulada sobre o Worlds."

    monkeypatch.setattr(routes, "qa_chain", FakeChain())

    response = client.post("/ask", json={
        "session_id": "test",
        "question": "O que é o Worlds?"
    })

    assert response.status_code == 200
    assert "Resposta simulada" in response.json()["answer"]


def test_history():
    response = client.get("/history/test")
    assert response.status_code == 200