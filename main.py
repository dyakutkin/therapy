from pydantic import BaseModel
from typing import Union, Dict
from enum import Enum


class Variable(str, Enum):
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'
    F = 'f'


class OperationType(str, Enum):
    sum = '+'
    difference = '-'
    multiplication = '*'
    division = '/'


class Operation(BaseModel):
    type: OperationType

    operation_funcs = {
        OperationType.sum: lambda x, y: x + y,
        OperationType.difference: lambda x, y: x - y,
        OperationType.multiplication: lambda x, y: x * y,
        OperationType.division: lambda x, y: x / y,
    }

    def get_evaluation_func(self):
        return self.operation_funcs[self.type]


class BinaryExpression(BaseModel):
    x: Union[int, float, Variable, 'BinaryExpression']
    y: Union[int, float, Variable, 'BinaryExpression']
    operation_type: OperationType

    @classmethod
    def evaluate_operand(cls, operand, variables):
        if isinstance(operand, Variable):
            return variables.get(operand)
        if isinstance(operand, cls):
            return operand.evaluate(variables)
        return operand

    def evaluate(self, variables: Dict[Variable, Union[int, bool, float]]) -> float:
        operation = Operation(type=self.operation_type)
        func = operation.get_evaluation_func()
        return func(
            self.evaluate_operand(self.x, variables),
            self.evaluate_operand(self.y, variables)
        )

BinaryExpression.update_forward_refs()
