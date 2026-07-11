class FinancialEngine:

    def calculate(self, income, expenses, debt):

        remaining_income = income - expenses

        debt_to_income_ratio = debt / income

        if debt_to_income_ratio < 0.3:
            status = "Low Risk"

        elif debt_to_income_ratio < 0.6:
            status = "Moderate Risk"

        else:
            status = "High Risk"

        return {
            "monthly_income": income,
            "monthly_expenses": expenses,
            "remaining_income": remaining_income,
            "total_debt": debt,
            "debt_to_income_ratio": round(debt_to_income_ratio, 2),
            "financial_status": status
        }