from fastapi import APIRouter
from numerology.charts import build_chart
from numerology.interpretations import get_interpretation

router = APIRouter()

@router.get("/personality")
def personality(name: str, day: int, month: int, year: int, today: date):
    chart = build_chart(name, day, month, year)
    enriched = {k: {"number": v, "meaning": get_interpretation(k, v)} for k, v in chart.items()}
    return {"chart": enriched}
