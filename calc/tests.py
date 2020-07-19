from unittest import TestCase, main

from calc.calc import Matcher, Input, H, Calculation, ResultField, Match
from calc.expressions.expressions import BinaryExpression, Variable, OperationType


class TestInput(TestCase):
    def test_t(self):
        mapping = [
            Match(
                input=Input(a=True, b=True, c=False),
                calculation=Calculation(
                    result_field=ResultField.H,
                    fallback_value=H.M,
                ),
            ),
            Match(
                input=Input(h=H.M),
                calculation=Calculation(
                    expression=BinaryExpression(
                        x=Variable.D,
                        y = BinaryExpression(
                            x=Variable.D,
                            y=BinaryExpression(x=Variable.E, y=10, operation_type=OperationType.division),
                            operation_type=OperationType.multiplication,
                        ),
                        operation_type=OperationType.sum,
                    ),
                    result_field=ResultField.K,
                ),
            ),
        ]
        matcher = Matcher(mapping=mapping)
        results = matcher.evaluate(Input(h=H.M, d=1.0, e=2))
        self.assertEqual(results[ResultField.K], 1.2)


if __name__ == '__main__':
    main()
