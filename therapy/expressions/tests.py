from unittest import TestCase, main

from therapy.expressions import OperationType, Variable, Expression


class TestInput(TestCase):
    test_table = (
        # Basic binary operators.
        (
            (3, 4, OperationType.multiplication,),
            {},
            12,
        ),
        (
            (1, 2, OperationType.difference,),
            {},
            -1,
        ),
        (
            (1, 2, OperationType.sum),
            {},
            3,
        ),
        (
            (3, 2, OperationType.division,),
            {},
            1.5,
        ),
        # Nested expressions.
        (
            (
                2,
                Expression(x=1, y=1, operation_type=OperationType.sum),
                OperationType.multiplication,
            ),
            {},
            4
        ),
        (
            (
                Expression(x=1, y=1, operation_type=OperationType.sum),
                Expression(x=1, y=1, operation_type=OperationType.sum),
                OperationType.division,
            ),
            {},
            1
        ),
        # Expressions with variables.
        (
            (
                Expression(x=Variable.A, y=1, operation_type=OperationType.sum),
                Expression(x=1, y=1, operation_type=OperationType.sum),
                OperationType.division,
            ),
            {Variable.A: 2},
            1.5
        ),
    )

    def test(self):
        for ((x, y, operation_type,), variables, expected_result,) in self.test_table:
            with self.subTest(
                    x=x,
                    y=y,
                    operation_type=operation_type,
                    variables=variables,
                    expected_result=expected_result
                ):
                expression = Expression(
                    x=x,
                    y=y,
                    operation_type=operation_type,
                )
                self.assertEqual(expression.evaluate(variables=variables), expected_result)


if __name__ == '__main__':
    main()
