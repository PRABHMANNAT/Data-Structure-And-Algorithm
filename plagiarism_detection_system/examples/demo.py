"""Run the bundled sample submissions and print a review report."""

from pathlib import Path

from plagiarism_detector import Detector
from plagiarism_detector.files import discover
from plagiarism_detector.report import to_text


def main() -> None:
    folder = Path(__file__).with_name("submissions")
    matches = Detector().compare(discover(folder))
    print(to_text(matches))


if __name__ == "__main__":
    main()
