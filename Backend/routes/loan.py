from fastapi import APIRouter
from models.loan import Loan
from services.loan_service import LoanService

router = APIRouter()

loan_service = LoanService()


@router.post("/loan")
def add_loan(loan: Loan):
    return loan_service.add_loan(loan)


@router.get("/loans")
def get_all_loans():
    return loan_service.get_all_loans()


@router.get("/loan/{loan_id}")
def get_loan(loan_id: int):
    return loan_service.get_loan(loan_id)


@router.put("/loan/{loan_id}")
def update_loan(loan_id: int, loan: Loan):
    return loan_service.update_loan(loan_id, loan)


@router.delete("/loan/{loan_id}")
def delete_loan(loan_id: int):
    return loan_service.delete_loan(loan_id)