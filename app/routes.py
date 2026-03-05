from fastapi import APIRouter, HTTPException
from app.models import QuestionRequest, AnswerResponse, HistoryResponse
from app.session import add_message, get_history
from app.rag import get_qa_chain

router = APIRouter()
qa_chain = get_qa_chain()

@router.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):

    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Pergunta não pode estar vazia.")

    try:
        result = qa_chain.invoke(request.question)

        add_message(request.session_id, f"User: {request.question}")
        add_message(request.session_id, f"AI: {result}")

        return AnswerResponse(
            answer=result,
            session_id=request.session_id
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{session_id}", response_model=HistoryResponse)
async def get_session_history(session_id: str):
    try:
        history = get_history(session_id)
        return HistoryResponse(
            session_id=session_id,
            history=history
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))