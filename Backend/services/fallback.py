class FallbackEngine:

    def fallback_response(self, risk_level):

        if risk_level == "High":
            return {
                "recommendation": "Consult a financial advisor immediately.",
                "next_step": "Request debt restructuring."
            }

        elif risk_level == "Moderate":
            return {
                "recommendation": "Negotiate an installment payment plan.",
                "next_step": "Reduce unnecessary monthly expenses."
            }

        else:
            return {
                "recommendation": "Continue regular payments.",
                "next_step": "Maintain a healthy financial record."
            }