from enum import Enum
from typing import List, Tuple

from pydantic import BaseModel
from calc.expressions.expressions import BinaryExpression, Variable


class H(str, Enum):
    M = 'm'
    P = 'p'
    T = 't'


class ResultField(str, Enum):
    H = 'h'
    K = 'k'


class Input(BaseModel):
    a: bool = None
    b: bool = None
    c: bool = None
    d: float = None
    e: int = None
    f: int = None

    h: H = None
    k: float = None

    custom_expr_set: int = None


class Calculation(BaseModel):
    expression: BinaryExpression = None
    result_field: ResultField
    fallback_value: H = None


class Match(BaseModel):
    input: Input
    calculation: Calculation


class Matcher(BaseModel):
    mapping: List[Match]

    def evaluate(self, input: Input):
        results = {}
        current_input = input

        for match in self.mapping:
            matched_input, calculation = match.input, match.calculation
            current_input_dict = current_input.dict()
            
            not_matched = any(
                [
                    current_input_dict[field] != value
                    for field, value in matched_input.dict().items()
                    if value is not None
                ]
            )

            if not_matched:
                continue

            if calculation.expression is None:
                res = {calculation.result_field: calculation.fallback_value}
            else:
                value = calculation.expression.evaluate(variables=input.dict())
                res = {calculation.result_field: value}
            current_input = Input(**res)
            results.update(res)

        return results
