from fastapi import APIRouter
from models.predictor import FinancialInput
from services.financial_engine import FinancialEngine

router = APIRouter()

engine = FinancialEngine()

@router.post("/financial")
def financial_analysis(data: FinancialInput):
    return engine.calculate(
        data.monthly_income,
        data.monthly_expenses,
        data.total_debt
    )