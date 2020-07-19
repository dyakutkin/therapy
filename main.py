from fastapi import FastAPI
from pydantic import BaseModel

from storage import fetch_evaluation_data
from therapy.evaluator import Evaluator, Input


matcher = Evaluator(rules=fetch_evaluation_data())
app = FastAPI()


class CalculateRequest(BaseModel):
    a: bool
    b: bool
    c: bool
    d: float
    e: int
    f: int


@app.post("/calculate/")
def read_root(req: CalculateRequest):
    result = matcher.evaluate(Input(**req.dict()))
    return result
