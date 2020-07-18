from unittest import TestCase, main

from main import Operation, OperationType, BinaryExpression


class TestInput(TestCase):
    def test_simple_expression(self):
        test_table = (
            ((3, 4, OperationType.multiplication), 12,),
            ((1, 2, OperationType.difference), -1,),
            ((1, 2, OperationType.sum), 3,),
        )
        for ((x, y, operation_type,), expected_result,) in test_table:
            with self.subTest(x=x, y=y, operation_type=operation_type, expected_result=expected_result):
                expression = BinaryExpression(
                    x=x,
                    y=y,
                    operation_type=operation_type,
                )
                self.assertEqual(expression.evaluate(), expected_result)


if __name__ == '__main__':
    main()
