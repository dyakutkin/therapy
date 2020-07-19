import json

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from calc.calc import Matcher, Input


app = FastAPI()

def fetch_matcher_data():
    with open('dump.json', 'r') as fp:
        return json.loads(fp.read())

matcher_data = fetch_matcher_data()
matcher = Matcher(mapping=matcher_data)


class CalculateRequest(BaseModel):
    a: bool
    b: bool
    c: bool
    d: float
    e: int
    f: int


class CalculateResponse(BaseModel):
    h: str
    k: float


@app.post("/calculate/")
def read_root(req: CalculateRequest):
    result = matcher.evaluate(Input(**req.dict()))
    return result
