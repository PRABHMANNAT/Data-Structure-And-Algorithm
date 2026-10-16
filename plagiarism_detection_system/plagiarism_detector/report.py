"""Human-readable and machine-readable reports."""

import json
from dataclasses import asdict
from html import escape

from .models import Match


def to_json(matches: list[Match]) -> str:
    return json.dumps({"matches": [asdict(match) for match in matches]}, indent=2)


def to_text(matches: list[Match]) -> str:
    if not matches:
        return "No matches above the configured threshold."
    lines = []
    for match in matches:
        lines.append(f"{match.score:.1%}  {match.left}  <->  {match.right}")
        lines.append(f"  shared fingerprints: {match.shared_fingerprints}; "
                     f"containment: {match.containment:.1%}; jaccard: {match.jaccard:.1%}")
        for span in match.evidence:
            lines.append(f"  matching {span.length} tokens at lines {span.left_line} and {span.right_line}")
    return "\n".join(lines)


def to_html(matches: list[Match]) -> str:
    rows = []
    for match in matches:
        locations = ", ".join(f"{span.left_line} ↔ {span.right_line} ({span.length} tokens)"
                              for span in match.evidence)
        rows.append("<tr><td>" + escape(match.left) + "</td><td>" + escape(match.right) +
                    f"</td><td>{match.score:.1%}</td><td>{escape(locations)}</td></tr>")
    body = "".join(rows) or '<tr><td colspan="4">No matches above threshold</td></tr>'
    return ("<!doctype html><html lang=\"en\"><meta charset=\"utf-8\">"
            "<title>Similarity report</title><style>body{font:16px system-ui;margin:2rem}"
            "table{border-collapse:collapse;width:100%}td,th{padding:.6rem;border:1px solid #bbb}"
            "th{text-align:left;background:#eee}</style><h1>Source similarity report</h1>"
            "<p>Scores are review signals, not proof of plagiarism.</p><table>"
            "<thead><tr><th>File A</th><th>File B</th><th>Score</th><th>Evidence lines</th>"
            "</tr></thead><tbody>" + body + "</tbody></table></html>")
