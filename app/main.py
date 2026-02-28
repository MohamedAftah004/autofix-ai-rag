from fastapi import FastAPI, HTTPException
from app.schemas import DiagnoseRequest
from app.agents.retriever import FaultRetriever
from app.agents.analyzer import analyze_input
from app.agents.diagnosis_agent import run_diagnosis
from app.agents.critic_agent import validate_answer

app = FastAPI(title="AutoFix AI")

retriever = FaultRetriever()


@app.post("/diagnose")
def diagnose(req: DiagnoseRequest):
    try:
        analysis = analyze_input(req.description, req.car_model)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    record = retriever.retrieve(
        description=analysis["description"],
        car_model=analysis["car_model"]
    )

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="المعلومة غير متوفرة عندي"
        )

    answer = run_diagnosis(record)

    ok, error = validate_answer(answer)
    if not ok:
        raise HTTPException(status_code=400, detail=error)

    return {
        "diagnosis": answer,
        "confidence": record["confidence"]
    }