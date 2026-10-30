import json, unittest
from pathlib import Path
from flowfoundry.service import run


class AdapterTests(unittest.TestCase):
    def test_every_example_is_json_finite(self):
        manifest = json.loads(
            (Path(__file__).parent / "project.json").read_text(encoding="utf-8")
        )
        for preset in manifest["presets"]:
            with self.subTest(name=preset["name"]):
                result = run(preset["input"])
                self.assertTrue(result["metrics"])
                json.dumps(result, allow_nan=False)

    def test_wrong_field_type_is_a_validation_error(self):
        with self.assertRaises(ValueError):
            run({"edges": []})
