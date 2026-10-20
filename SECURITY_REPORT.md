# Exyora AI: Security & Compliance Self-Assessment Report
**Competition:** 2026 Shenzhen International FinTech Competition (FinTechathon) — International Track  
**Project Name:** Exyora AI (Topic C: Cross-Border & Student Finance Assistant)

## 1. Unified Permission-Tier Implementation Architecture
Exyora AI enforces a strict 4-Tier Permission and Access Control Model across its prototype and documentation:
* **Tier 1 (Advisory & Read-Only):** Natural language guidance, exchange rate comparisons, and budget tracking. Requires standard session state.
* **Tier 2 (Proactive Alert / Scam Warning):** Automated detection of suspicious payment requests (e.g., fraudulent housing deposit alerts) with risk breakdown.
* **Tier 3 (User-Confirmed Execution):** Initiating simulated cross-border remittances or starter accounts, requiring explicit user confirmation before action.
* **Tier 4 (Blocked or Unsafe):** Automatic transaction halting and quarantine for high-risk or non-compliant payment destinations.

## 2. Data Privacy & Compliance Alignment
* **Prototype Data Scope:** Operates entirely on simulated sample data and mock telemetry to protect user privacy during demonstration.
* **Production Privacy Roadmap:** Designed to comply with GDPR via federated processing principles where raw financial documents remain local.

## 3. Known-Risk List & Mitigation Strategies
1. **Risk 1 (Simulated Data Limitations):** Prototype relies on mock exchange rates and static provider parameters.  
   * *Mitigation:* Clearly labelled as sample data in the UI and documentation.
2. **Risk 2 (API Connection Stability):** Localhost port mismatches between frontend and backend during demo runs.  
   * *Mitigation:* CORS middleware enabled (`allow_origins=["*"]`) and robust fetch error handling implemented.
3. **Risk 3 (User Authorization Bypass):** Accidental confirmation of unsafe transfers.  
   * *Mitigation:* Enforced explicit Tier-3 confirmation screens with clear warnings.