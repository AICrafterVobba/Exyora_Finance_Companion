from algorithms import ExyoraAlgorithms

def test_remittance_routing():
    providers = [
        {"name": "Provider A", "flat_fee": 10.0, "percentage_markup": 0.01, "latency_hours": 24, "amount": 5000},
        {"name": "Provider B", "flat_fee": 5.0, "percentage_markup": 0.003, "latency_hours": 2, "amount": 5000}
    ]
    best = ExyoraAlgorithms.dfso_remittance_routing(providers, 1.5)
    assert best["name"] == "Provider B"

def test_credit_scoring():
    score = ExyoraAlgorithms.fc_csm_credit_scoring(85, True, 0.95)
    assert 300 <= score <= 850