from .numbers import name_to_number, date_to_number, reduce_number

def build_chart(full_name: str, birth_day: int, birth_month: int, birth_year: int) -> dict:
    """Generate full numerology chart based on Juno Jordan system."""

    chart = {}
    chart["life_path"] = date_to_number(birth_day, birth_month, birth_year)
    chart["expression"] = name_to_number(full_name)
    chart["soul_urge"] = name_to_number(full_name, vowels_only=True)
    chart["personality"] = name_to_number(full_name, consonants_only=True)
    chart["birthday"] = reduce_number(birth_day)
    chart["maturity"] = reduce_number(chart["life_path"] + chart["expression"])
    chart["balance"] = reduce_number(name_to_number(full_name[0])) if full_name else None

    return chart
