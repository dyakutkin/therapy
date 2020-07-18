from dataclasses import dataclass
from numbers import Number
from enum import Enum


@dataclass
class Input:
    a: bool = None
    b: bool = None
    c: bool = None
    d: float = None
    e: int = None
    f: int = None

    custom_expr_set: int = None


class OperationTypes(str, Enum):
    sum = '+'
    difference = '-'
    multiplication = '*'


@dataclass
class Operation:
    type: OperationTypes

    operation_funcs = {
        OperationTypes.sum: lambda x, y: x + y,
        OperationTypes.difference: lambda x, y: x - y,
        OperationTypes.multiplication: lambda x, y: x * y,
    }

    def get_evaluation_func(self):
        return self.operation_funcs[self.type]
