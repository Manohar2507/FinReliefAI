from pydantic import BaseModel

class FinancialInput(BaseModel):
    monthly_income: float
    monthly_expenses: float
    total_debt: float