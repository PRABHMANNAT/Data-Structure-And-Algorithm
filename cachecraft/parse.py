from workbench.lab_inputs import words, whole
from .models import Workload


def parse(data):
    return Workload(words(data, "keys"), whole(data.get("capacity", 3), 1, 40))
