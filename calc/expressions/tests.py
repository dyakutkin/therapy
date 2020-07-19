from unittest import TestCase, main

from calc.expressions.expressions import OperationType, Variable, BinaryExpression


class TestInput(TestCase):
    def test_expressions(self):
        test_table = (
            # Basic binary operators.
            ((3, 4, OperationType.multiplication,), {}, 12,),
            ((1, 2, OperationType.difference,), {}, -1,),
            ((1, 2, OperationType.sum), {}, 3,),
            ((3, 2, OperationType.division,), {}, 1.5,),
            # Nested expressions.
            ((2, BinaryExpression(x=1, y=1, operation_type=OperationType.sum), OperationType.multiplication,), {}, 4),
            (
                (
                    BinaryExpression(x=1, y=1, operation_type=OperationType.sum),
                    BinaryExpression(x=1, y=1, operation_type=OperationType.sum),
                    OperationType.division,
                ),
                {},
                1
            ),
            # Expressions with variables.
            (
                (
                    BinaryExpression(x=Variable.A, y=1, operation_type=OperationType.sum),
                    BinaryExpression(x=1, y=1, operation_type=OperationType.sum),
                    OperationType.division,
                ),
                {Variable.A: 2},
                1.5
            ),
        )
        for ((x, y, operation_type,), variables, expected_result,) in test_table:
            with self.subTest(x=x, y=y, operation_type=operation_type, variables=variables, expected_result=expected_result):
                expression = BinaryExpression(
                    x=x,
                    y=y,
                    operation_type=operation_type,
                )
                self.assertEqual(expression.evaluate(variables=variables), expected_result)



if __name__ == '__main__':
    main()
