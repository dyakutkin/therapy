from pydantic import BaseModel
from typing import Union
from enum import Enum


class Input(BaseModel):
    a: bool = None
    b: bool = None
    c: bool = None
    d: float = None
    e: int = None
    f: int = None

    custom_expr_set: int = None


class OperationType(str, Enum):
    sum = '+'
    difference = '-'
    multiplication = '*'


class Operation(BaseModel):
    type: OperationType

    operation_funcs = {
        OperationType.sum: lambda x, y: x + y,
        OperationType.difference: lambda x, y: x - y,
        OperationType.multiplication: lambda x, y: x * y,
    }

    def get_evaluation_func(self):
        return self.operation_funcs[self.type]


class BinaryExpression(BaseModel):
    x: Union[int, float]
    y: Union[int, float]
    operation_type: OperationType
    

    def evaluate(self) -> float:
        operation = Operation(type=self.operation_type)
        func = operation.get_evaluation_func()
        return func(self.x, self.y)

