"""Load the Kolors colour library."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLORS_DIR = ROOT / "colors"

_HEX_LINE = re.compile(r"^- HEX:\s*(#[0-9A-Fa-f]{6})", re.M)
_TITLE = re.compile(r"^## (.+)$", re.M)
_CHARACTER = re.compile(r"^- Character:\s*(.+)$", re.M)
INDEX_PAGE = "index"


def load_colors():
    """Return {slug: {"slug", "name", "hex", "character"}} for every colour file with a readable HEX."""
    colors = {}
    for path in sorted(COLORS_DIR.glob("*.md")):
        if path.stem == INDEX_PAGE:
            continue
        text = path.read_text()
        hex_match = _HEX_LINE.search(text)
        title = _TITLE.search(text)
        if not hex_match or not title:
            continue
        character = _CHARACTER.search(text)
        colors[path.stem] = {"slug": path.stem, "name": title.group(1).strip(), "hex": hex_match.group(1).upper(),
                             "character": character.group(1).strip() if character else ""}
    return colors

