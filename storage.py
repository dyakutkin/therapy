import json

from settings import EVALUATOR_DUMP_PATH


def fetch_evaluation_data():
    with open(EVALUATOR_DUMP_PATH, 'r') as fp:
        return json.loads(fp.read())
