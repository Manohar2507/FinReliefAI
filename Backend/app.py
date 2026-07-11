from fastapi import FastAPI
import uvicorn

from routes.settlement import router as settlement_router
from routes.financial import router as financial_router
from routes.negotiation import router as negotiation_router

app = FastAPI(title="FinReliefAI Backend")

app.include_router(settlement_router)
app.include_router(financial_router)
app.include_router(negotiation_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to FinReliefAI Backend",
        "status": "Running Successfully"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)