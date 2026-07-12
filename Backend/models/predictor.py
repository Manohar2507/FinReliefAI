from pydantic import BaseModel

# Financial Engine Input
class FinancialInput(BaseModel):
    monthly_income: float
    monthly_expenses: float
    total_debt: float


# Settlement Prediction Input
class SettlementInput(BaseModel):
    credit_score: int
    monthly_income: float
    total_debt: float