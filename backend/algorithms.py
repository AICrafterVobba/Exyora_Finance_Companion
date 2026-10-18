import numpy as np

class ExyoraAlgorithms:
    @staticmethod
    def dfso_remittance_routing(providers, user_urgency_weight):
        scored_providers = []
        for p in providers:
            fee_score = p['flat_fee'] + (p['percentage_markup'] * p['amount'])
            latency_score = p['latency_hours']
            
            total_score = (0.4 * fee_score) + (0.4 * latency_score) + (0.2 * (1 / user_urgency_weight))
            scored_providers.append({**p, 'optimization_score': total_score})
        
        scored_providers.sort(key=lambda x: x['optimization_score'])
        return scored_providers[0]

    @staticmethod
    def fc_csm_credit_scoring(bank_stability_score, rental_history_verified, utility_on_time_pct):
        score = (bank_stability_score * 0.4) + (float(rental_history_verified) * 300) + (utility_on_time_pct * 3.0)
        return min(max(int(score), 300), 850)