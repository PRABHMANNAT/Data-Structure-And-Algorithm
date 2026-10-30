from workbench.lab_inputs import words, whole
from .models import Config


def parse(data):
    return Config(
        words(data, "items"),
        words(data, "queries"),
        whole(data.get("bits", 128), 8, 4096),
        whole(data.get("hashes", 4), 1, 12),
        whole(data.get("width", 32), 4, 256),
    )
