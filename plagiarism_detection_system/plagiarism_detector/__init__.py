"""Source-code similarity detection for teaching and triage."""

from .engine import Detector, DetectorConfig
from .models import Match, SourceDocument

__all__ = ["Detector", "DetectorConfig", "Match", "SourceDocument"]
