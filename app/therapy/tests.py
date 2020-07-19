from unittest import TestCase, main

from therapy.evaluator import Evaluator, Input, H, Calculation, ResultField, Rule
from therapy.expressions import Expression, Variable, OperationType


class TestInput(TestCase):
    test_table = (
        (
            [
                Rule(
                    input=Input(a=True, b=True, c=False),
                    calculation=Calculation(
                        result_field=ResultField.H,
                        value=H.M,
                    ),
                ),
            ],
            Input(a=True, b=True, c=False),
            {ResultField.H: H.M},
        ),
        (
            [
                Rule(
                    input=Input(a=True, b=True, c=False),
                    calculation=Calculation(
                        result_field=ResultField.H,
                        value=H.M,
                    ),
                ),
                Rule(
                    input=Input(a=True, b=True, c=False),
                    calculation=Calculation(
                        result_field=ResultField.H,
                        value=H.T,
                    ),
                ),
            ],
            Input(a=True, b=True, c=False),
            {ResultField.H: H.T},
        ),
        (
            [
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
                                y=Expression(
                                    x=Variable.E,
                                    y=10,
                                    operation_type=OperationType.division,
                                ),
                                operation_type=OperationType.multiplication,
                            ),
                            operation_type=OperationType.sum,
                        ),
                        result_field=ResultField.K,
                    ),
                ),
            ],
            Input(h=H.M, d=1.0, e=2),
            {ResultField.K: 1.2},
        ),
    )

    def test(self):
        for rules, input, expected_result in self.test_table:
            with self.subTest(rules=rules, input=input, expected_result=expected_result):
                evaluator = Evaluator(rules=rules)
                results = evaluator.evaluate(input)
                self.assertEqual(results, expected_result)


if __name__ == '__main__':
    main()
