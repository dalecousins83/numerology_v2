from .numbers import name_to_number, date_to_number, reduce_number
from datetime import date

def build_chart(full_name: str, birth_day: int, birth_month: int, birth_year: int, today: date | None = None) -> dict:
    """Generate full numerology chart based on Juno Jordan system."""

    """
    Build a numerology chart for a given name and date of birth.
    Optionally include today's date for personal year/month/day cycles.
    """
    chart = {}

    # Core numbers
    chart["life_path"] = date_to_number(birth_day, birth_month, birth_year)
    chart["expression"] = name_to_number(full_name)
    chart["soul_urge"] = name_to_number(full_name, vowels_only=True)
    chart["personality"] = name_to_number(full_name, consonants_only=True)
    chart["birthday"] = reduce_number(birth_day)
    chart["maturity"] = reduce_number(chart["life_path"] + chart["expression"])
    chart["balance"] = reduce_number(name_to_number(full_name[0])) if full_name else None
    
    # Optional cycles
    if today is not None:
        #chart.update(calculate_personal_cycles(day, month, year, today))
        chart.update(calculate_personal_cycles(birth_day, birth_month, birth_year, today))

    return chart


def calculate_personal_cycles(day: int, month: int, year: int, today: date) -> dict:
    """
    Calculate personal year, month, and day numbers.
    """
    cycles = {}

    # --- Personal Year ---
    personal_year_base = month + day + today.year
    cycles["personal_year"] = reduce_number(personal_year_base)

    # --- Personal Month ---
    personal_month_base = cycles["personal_year"] + today.month
    cycles["personal_month"] = reduce_number(personal_month_base)

    # --- Personal Day ---
    personal_day_base = cycles["personal_month"] + today.day
    cycles["personal_day"] = reduce_number(personal_day_base)

    return cycles
