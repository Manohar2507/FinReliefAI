from fastapi import APIRouter
from models.predictor import SettlementInput

router = APIRouter()

@router.post("/settlement")
def settlement_prediction(data: SettlementInput):

    if data.credit_score >= 750:
        settlement_percentage = 90
    elif data.credit_score >= 650:
        settlement_percentage = 70
    else:
        settlement_percentage = 50

    settlement_amount = (data.total_debt * settlement_percentage) / 100

    return {
        "credit_score": data.credit_score,
        "settlement_percentage": settlement_percentage,
        "recommended_settlement": settlement_amount
    }