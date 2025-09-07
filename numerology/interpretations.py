import json
from pathlib import Path

# Path to the JSON file
INTERP_FILE = Path(__file__).parent.parent / "data" / "interpretations.json"

# Load interpretations at import
with open(INTERP_FILE, "r", encoding="utf-8") as f:
    INTERPRETATIONS = json.load(f)


def get_interpretation(category: str, number: int) -> str:
    """
    Fetch interpretation text for a number under a given category.
    If not found, returns a fallback message.
    """
    category_data = INTERPRETATIONS.get(category.lower())
    if not category_data:
        return f"No interpretation found for category '{category}'."

    meaning = category_data.get(str(number))
    if not meaning:
        return f"No interpretation available for number {number} in {category}."

    return meaning


def enrich_chart(chart: dict) -> dict:
    """
    Given a raw chart dictionary (numbers only),
    return a dict with number + interpretation text.
    
    Example input:
    {
        "life_path": 5,
        "expression": 6
    }
    
    Output:
    {
        "life_path": {"number": 5, "meaning": "..."},
        "expression": {"number": 6, "meaning": "..."}
    }
    """
    enriched = {}
    for key, num in chart.items():
        if num is None:
            enriched[key] = {"number": None, "meaning": "Not calculated"}
            continue
        enriched[key] = {
            "number": num,
            "meaning": get_interpretation(key, num)
        }
    re
