from fastapi import FastAPI
from pydantic import BaseModel
from analyzer import analyze_code
from llm import get_refactoring_suggestions

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/refactor")
def refactor(req: CodeRequest):
    analysis = analyze_code(req.code)
    result = get_refactoring_suggestions(req.code, analysis)

    return {
        "analysis": analysis,
        "result": result
    }
