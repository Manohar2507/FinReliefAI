class LoanProcessing:

    def process_loan(self, loan):

        # Monthly EMI (Simple Approximation)
        monthly_emi = (
            loan.loan_amount +
            (loan.loan_amount * loan.interest_rate / 100)
        ) / loan.tenure_months

        # Debt-to-Income Ratio
        debt_ratio = round(loan.total_debt / loan.monthly_income, 2)

        # Risk Level
        if debt_ratio < 2:
            risk = "Low"
            settlement = "20%"
            status = "Healthy"

        elif debt_ratio < 5:
            risk = "Moderate"
            settlement = "35%"
            status = "Needs Monitoring"

        else:
            risk = "High"
            settlement = "50%"
            status = "Eligible for Settlement"

        return {
            "loan_id": loan.loan_id,
            "customer_name": loan.customer_name,
            "monthly_income": loan.monthly_income,
            "loan_amount": loan.loan_amount,
            "monthly_emi": round(monthly_emi, 2),
            "debt_ratio": debt_ratio,
            "risk_level": risk,
            "recommended_settlement": settlement,
            "status": status
        }