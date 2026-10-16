"""Extension mapping and keyword sets for normalized token streams."""

from pathlib import Path

EXTENSIONS = {
    ".py": "python", ".js": "javascript", ".jsx": "javascript",
    ".ts": "typescript", ".tsx": "typescript", ".java": "java",
    ".c": "c", ".h": "c", ".cpp": "cpp", ".cc": "cpp",
    ".hpp": "cpp", ".go": "go", ".rs": "rust",
}

KEYWORDS = set("""
abstract as async await bool break byte case catch char class const continue def
default defer delete do double else enum except export extends false final finally
float for from func function goto if import in int interface is lambda let long
match module new nil null package pass private protected public raise return self
short static struct super switch this throw throws trait true try type typeof
uint union use var void while yield
""".split())


def language_for(path: str | Path) -> str | None:
    return EXTENSIONS.get(Path(path).suffix.lower())
