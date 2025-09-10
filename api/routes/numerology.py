from fastapi import APIRouter, Query
from numerology.charts import build_chart
from numerology.interpretations import get_interpretation, enrich_chart
from datetime import date, datetime


router = APIRouter()

@router.get("/personality")
def personality(name: str, day: int, month: int, year: int):
    chart = build_chart(name, day, month, year)
    enriched = {k: {"number": v, "meaning": get_interpretation(k, v)} for k, v in chart.items()}
    return {"chart": enriched}

@router.get("/daily")
def daily_report(name: str, day: int, month: int, year: int, today: date | None = Query(default=None)):
    """
    Generate today's personal numerology report (year, month, day).
    - If 'today' is not provided, defaults to system date.
    """
    if today is None:
        today = datetime.today().date()

    chart = build_chart(name, day, month, year, today=today)
    enriched = enrich_chart(chart)

    # Only return daily cycle numbers
    daily_keys = ["personal_year", "personal_month", "personal_day"]
    return {k: enriched[k] for k in daily_keys if k in enriched}
