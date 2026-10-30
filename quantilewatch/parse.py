from workbench.lab_inputs import whole
from workbench.validation import numbers


def parse(data):
    return numbers(data, limit=300), whole(data.get("window", 5), 1, 100)
