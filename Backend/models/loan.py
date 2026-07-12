from pydantic import BaseModel

class Loan(BaseModel):
    loan_id: int
    customer_name: str
    monthly_income: float
    total_debt: float
    loan_amount: float
    interest_rate: float
    tenure_months: int
