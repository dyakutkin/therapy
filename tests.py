from unittest import TestCase, main

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


class TestInput(TestCase):
    def test_t(self):
        test_table = (
            (
                {"a": True, "b": True, "c": False, "d": 1, "e": 13, "f": 15},
                {"h": "m", "k": 2.3},
            ),
            (
                {"a": True, "b": True, "c": True, "d": 1, "e": 13, "f": 15},
                {"h": "p", "k": 0.92},
            ),
            (
                {"a": False, "b": True, "c": True, "d": 1, "e": 13, "f": 15},
                {"h": "t", "k": 0.5},
            ),
            
        )
        for req, expected_resp in test_table:
            with self.subTest(req=req, expected_resp=expected_resp):
                response = client.post(
                    "/calculate/",
                    json=req,
                )
                self.assertEqual(response.json(), expected_resp)


if __name__ == '__main__':
    main()
