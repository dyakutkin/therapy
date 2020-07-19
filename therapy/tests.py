from unittest import TestCase, main

from therapy.evaluator import Evaluator, Input, H, Calculation, ResultField, Rule
from therapy.expressions import Expression, Variable, OperationType


class TestInput(TestCase):
    def test_t(self):
        rules = [
            Rule(
                input=Input(a=True, b=True, c=False),
                calculation=Calculation(
                    result_field=ResultField.H,
                    value=H.M,
                ),
            ),
            Rule(
                input=Input(h=H.M),
                calculation=Calculation(
                    expression=Expression(
                        x=Variable.D,
                        y = Expression(
                            x=Variable.D,
                            y=Expression(x=Variable.E, y=10, operation_type=OperationType.division),
                            operation_type=OperationType.multiplication,
                        ),
                        operation_type=OperationType.sum,
                    ),
                    result_field=ResultField.K,
                ),
            ),
        ]
        matcher = Evaluator(rules=rules)
        results = matcher.evaluate(Input(h=H.M, d=1.0, e=2))
        self.assertEqual(results[ResultField.K], 1.2)


if __name__ == '__main__':
    main()
