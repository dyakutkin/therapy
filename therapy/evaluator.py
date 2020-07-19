from enum import Enum
from typing import List

from pydantic import BaseModel

from therapy.expressions import Expression


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


class Calculation(BaseModel):
    expression: Expression = None
    result_field: ResultField
    value: H = None


class Rule(BaseModel):
    input: Input
    calculation: Calculation


class Evaluator(BaseModel):
    rules: List[Rule]

    def process_rules(self):
        rules = {}

        for rule in self.rules:
            key_ = tuple(v for v in rule.dict()['input'].values())
            rules[key_] = rule

        return rules.values()


    def evaluate(self, input: Input):
        results = {}
        current_input = input

        rules = self.process_rules()

        for match in rules:
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
                res = {calculation.result_field: calculation.value}
            else:
                value = calculation.expression.evaluate(variables=input.dict())
                res = {calculation.result_field: value}
            current_input = Input(**res)
            results.update(res)

        return results
