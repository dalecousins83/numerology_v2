import json
from pathlib import Path

# Load interpretations JSON once
INTERPRETATIONS_FILE = Path(__file__).resolve().parent.parent / "data" / "interpretations.json"

with INTERPRETATIONS_FILE.open("r", encoding="utf-8") as f:
    INTERPRETATIONS = json.load(f)


def get_interpretation(category: str, number: int | str) -> str:
    """
    Look up the interpretation for a given category and number.
    Returns a string interpretation if found, otherwise a fallback message.
    """
    cat_data = INTERPRETATIONS.get(category, {})
    interp = cat_data.get(str(number))
    if interp:
        return interp
    return f"No interpretation found for {category} number {number}."


def enrich_chart(chart: dict) -> dict:
    """
    Attach interpretations to each element in a numerology chart.
    Chart dict should already include numeric values.
    """
    enriched = {}

    for key, value in chart.items():
        enriched[key] = {
            "number": value,
            "interpretation": get_interpretation(key, value)
        }

    return enriched
