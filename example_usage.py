from client import MultiTenantFederatedRagPrivacyEnclaveClient

def main():
    client = MultiTenantFederatedRagPrivacyEnclaveClient()
    res = client.query_confidential_knowledge_enclave('Cross-jurisdiction fintech AML fraud velocity index', 8)
    print('Federated RAG Privacy Enclave: ' + res['enclave_query_id'] + ' (' + str(res['enclaves_queried_count']) + ' enclaves)')
    print('DP Epsilon: ' + str(res['differential_privacy_epsilon']) + ' | ZK Proof Attested: ' + str(res['zero_knowledge_proof_attested']))
    print('PII Risk: ' + str(res['raw_pii_leakage_risk']))
    print('Answer: ' + res['homomorphic_aggregated_answer'])
    print('Certificate: ' + res['attestation_certificate_url'])

if __name__ == '__main__':
    main()
