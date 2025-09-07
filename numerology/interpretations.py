import json
from pathlib import Path

INTERP_FILE = Path(__file__).parent.parent / "data" / "interpretations.json"
with open(INTERP_FILE, "r") as f:
    INTERPRETATIONS = json.load(f)

def get_interpretation(category: str, number: int) -> str:
    """Fetch interpretation text for a number under a given category."""
    return INTERPRETATIONS.get(category, {}).get(str(number), "No interpretation available.")
