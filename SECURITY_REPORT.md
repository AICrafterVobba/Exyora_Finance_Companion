# Exyora AI: Security & Compliance Self-Assessment Report
**Competition:** 2026 Shenzhen International FinTech Competition (FinTechathon) — International Track[cite: 1, 2]
**Project Name:** Exyora AI (Topic C: Cross-Border & Student Finance Assistant)[cite: 1, 2]

## 1. Permission-Tier Implementation Architecture
Exyora AI enforces a strict 4-Tier Permission and Access Control Model to safeguard user assets and data:
* **Tier 1 (Advisory & Read-Only):** Natural language conversational queries, exchange rate checks, and budget health tracking. Requires standard session authentication.
* **Tier 2 (Simulated Proactive Alerts):** Risk notifications, scam detection warnings (e.g., fraudulent housing deposit alerts), and liquidity thresholds.
* **Tier 3 (Transaction Confirmation & Execution):** Initiating cross-border tuition remittances or opening starter accounts. **Mandatory Multi-Factor Authentication (MFA) and FIDO2 Biometric authorization** required before execution.
* **Tier 4 (Autonomous Emergency Override):** Automatic transaction freezing and suspicious activity quarantining managed by the Compliance & AML guardrails agent.

## 2. Data Privacy & Compliance Measures
* **Cross-Border Data Protection:** Fully aligns with GDPR and international data transfer standards by employing **Federated Learning** for credit scoring (raw financial records never cross borders; only encrypted gradient updates are processed).
* **Encryption Standards:** End-to-end encryption for all data in transit via **TLS 1.3** and data at rest protected using **AES-256**. Tokenization is enforced for all banking credentials.

## 3. Known-Risk List & Mitigation Strategies
1. **Risk 1 (LLM Hallucination in Financial Calculations):** Mitigated by routing all financial computations (remittance scoring, credit metrics) through deterministic Python algorithms (`algorithms.py`) rather than relying solely on probabilistic LLM text generation.
2. **Risk 2 (API Latency / Third-Party Gateway Failure):** Mitigated by implementing fallback multi-provider routing matrices in the DFSO-R protocol.
3. **Risk 3 (Unauthorized Access to Execution Endpoints):** Mitigated by strict separation of concerns between conversational chat layers and transactional APIs protected by OAuth 2.0 / OIDC tokens.