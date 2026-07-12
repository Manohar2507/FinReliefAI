from data.loan_store import loan_database
from services.processing import LoanProcessing


class LoanService:

    def __init__(self):
        self.processor = LoanProcessing()

    def add_loan(self, loan):
        loan_database.append(loan)

        analysis = self.processor.process_loan(loan)

        return {
            "message": "Loan added successfully",
            "loan": loan,
            "analysis": analysis
        }

    def get_all_loans(self):
        return loan_database

    def get_loan(self, loan_id):
        for loan in loan_database:
            if loan.loan_id == loan_id:
                return loan
        return {"message": "Loan not found"}

    def update_loan(self, loan_id, updated_loan):
        for index, loan in enumerate(loan_database):
            if loan.loan_id == loan_id:
                loan_database[index] = updated_loan
                return {
                    "message": "Loan updated successfully",
                    "loan": updated_loan
                }
        return {"message": "Loan not found"}

    def delete_loan(self, loan_id):
        for loan in loan_database:
            if loan.loan_id == loan_id:
                loan_database.remove(loan)
                return {"message": "Loan deleted successfully"}
        return {"message": "Loan not found"}