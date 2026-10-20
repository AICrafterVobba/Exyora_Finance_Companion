# Exyora AI: Autonomous Cross-Border & Student Finance Assistant
> Submitted for the 2026 Shenzhen International FinTech Competition (FinTechathon) — International Track (Topic C: Cross-Border & Student Finance Assistant).

## 🚀 Executive Summary
Exyora AI is an interactive prototype financial assistant designed to address cross-border financial friction points for international students. By combining a Python backend engine with a Swiss-design frontend, Exyora AI simulates smart remittance routing calculations, alternative credit scoring models, and scam detection guardrails.

---

## 🛠️ Implemented Prototype Features vs. Planned Architecture
### What is Built in This Prototype:
1. **DFSO-R Simulation Engine:** Python algorithm evaluating simulated provider flat fees, markups, and latencies.
2. **FC-CSM Credit Calculator:** Alternative scoring logic taking bank stability and utility payment metrics.
3. **Swiss-Design Glassmorphism UI:** Interactive frontend dashboard with live JSON terminal feedback.
4. **Audit & Safety Guardrails:** 4-tier permission logic and simulated scam risk analysis.

### Planned Production Architecture:
- Live API integration with global SWIFT/remittance gateways.
- Fully distributed Federated Learning pipeline and Vector Database (Milvus/Pinecone) for deep RAG memory.
- Biometric FIDO2 / hardware-level MFA enforcement.

---

## 📦 Deployment Instructions & Local Setup

**Requirements:** Python 3.10 or newer and a modern web browser. All data in this prototype is simulated.

1. **Clone the repository**
```bash
git clone https://github.com/AICrafterVobba/Exyora_Finance_Companion.git
cd Exyora_Finance_Companion
```

2. **Install backend dependencies**
```bash
cd backend
pip install fastapi uvicorn numpy pydantic
```

3. **Start the backend**
```bash
uvicorn main:app --reload --port 8000
```

4. **Open the frontend:** open the `index.html` file in the `frontend` folder in your browser. Make sure it points to the backend at `http://localhost:8000`.

## ✅ Test Cases

| # | Module | Input | Expected result |
|---|---|---|---|
| 1 | Tuition engine | Amount 5012 USD, urgency weight 1.6 | "Exyora Direct Route" is ranked optimal: fee $5, markup 0.3%, latency 2h, score 8.9 |
| 2 | Credit builder | Home bank stability 93, utility on-time rate 91 | A portable score out of 850 is shown |
| 3 | Scam Guard | A message asking for an urgent deposit to a personal account | Warning signs are listed and no action is taken |

Sandbox operation logs are in the `sandbox_logs` folder.

## 👥 Team
Byte Voyegers, Daffodil International University. Contact: byte.voyegers.exyora@gmail.com
