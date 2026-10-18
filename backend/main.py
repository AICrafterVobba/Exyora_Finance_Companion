from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from algorithms import ExyoraAlgorithms

app = FastAPI(title="Exyora AI Engine", version="1.0.0")

# Enable CORS for frontend and collaboration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for local testing & deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RemittanceRequest(BaseModel):
    amount: float
    urgency_weight: float

class CreditRequest(BaseModel):
    bank_stability: float
    rental_verified: bool
    utility_score: float

@app.get("/")
def home():
    return {"message": "Welcome to Exyora AI FinTech Backend API"}

@app.post("/api/v1/optimize-remittance")
def optimize_remittance(data: RemittanceRequest):
    providers = [
        {"name": "BankWire Global", "flat_fee": 25.0, "percentage_markup": 0.015, "latency_hours": 48, "amount": data.amount},
        {"name": "Exyora Direct Route", "flat_fee": 5.0, "percentage_markup": 0.003, "latency_hours": 2, "amount": data.amount},
        {"name": "StandardRemit", "flat_fee": 15.0, "percentage_markup": 0.01, "latency_hours": 24, "amount": data.amount}
    ]
    best_route = ExyoraAlgorithms.dfso_remittance_routing(providers, data.urgency_weight)
    return {"status": "success", "optimal_provider": best_route}

@app.post("/api/v1/calculate-credit")
def calculate_credit(data: CreditRequest):
    score = ExyoraAlgorithms.fc_csm_credit_scoring(data.bank_stability, data.rental_verified, data.utility_score)
    return {"status": "success", "portable_credit_score": score, "tier": "Prime-Equivalent"}