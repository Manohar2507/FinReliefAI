class AINegotiationEngine:

    def negotiate(self, income, debt):

        debt_ratio = debt / income

        if debt_ratio >= 5:
            strategy = "Request 50% debt settlement"
            priority = "High"

        elif debt_ratio >= 3:
            strategy = "Request installment payment plan"
            priority = "Medium"

        else:
            strategy = "Pay normally or negotiate a small discount"
            priority = "Low"

        return {
            "monthly_income": income,
            "total_debt": debt,
            "debt_ratio": round(debt_ratio, 2),
            "strategy": strategy,
            "priority": priority
        }