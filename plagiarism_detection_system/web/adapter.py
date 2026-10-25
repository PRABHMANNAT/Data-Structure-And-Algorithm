from dataclasses import asdict
from plagiarism_detector.engine import Detector, DetectorConfig
from plagiarism_detector.models import SourceDocument
from plagiarism_detector.tokenize import normalize_tokens
from workbench.validation import text

def run(data):
    language=text(data,'language','python')
    if language not in {'python','cpp','go','javascript'}:raise ValueError('Unsupported source language')
    left=text(data,'left',limit=6000);right=text(data,'right',limit=6000)
    documents=[SourceDocument('original',left,language),SourceDocument('comparison',right,language)]
    matches=Detector(DetectorConfig(k=3,window=2,min_score=0)).compare(documents)
    return dict(matches=[asdict(match) for match in matches],left_tokens=len(normalize_tokens(left,language)),
                right_tokens=len(normalize_tokens(right,language)),left=left,right=right)
