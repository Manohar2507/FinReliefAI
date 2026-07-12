from fastapi import APIRouter
from models.predictor import FinancialInput
from services.ai_negotiation import AINegotiationEngine
from services.fallback import FallbackEngine

router = APIRouter()

ai_engine = AINegotiationEngine()
fallback_engine = FallbackEngine()


@router.post("/negotiation")
def negotiation(data: FinancialInput):

    result = ai_engine.negotiate(
        data.monthly_income,
        data.total_debt
    )

    if result["priority"] == "High":
        result["fallback"] = fallback_engine.fallback_response("High")

    elif result["priority"] == "Medium":
        result["fallback"] = fallback_engine.fallback_response("Moderate")

    else:
        result["fallback"] = fallback_engine.fallback_response("Low")

    return result