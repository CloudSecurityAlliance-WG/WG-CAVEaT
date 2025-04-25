# IngressNightmare Vulnerability Visualization

This diagram visualizes the relationships between the STIX objects documenting the IngressNightmare vulnerability.

```mermaid
graph TD
    classDef attackPattern fill:#FF9999,stroke:#333,stroke-width:2px;
    classDef vulnerability fill:#FFF49C,stroke:#333,stroke-width:2px;
    classDef courseOfAction fill:#9CFF9C,stroke:#333,stroke-width:2px;

    A["Attack Pattern: 
    Ingress NGINX Admission Controller RCE"] -->|exploits| B["Vulnerability: 
    CVE-2025-1974 (Primary)"]
    
    B -->|related to| C["Vulnerability: 
    CVE-2025-1097"]
    
    B -->|related to| D["Vulnerability: 
    CVE-2025-1098"]
    
    B -->|related to| E["Vulnerability: 
    CVE-2025-24514"]
    
    F["Course of Action: 
    Update Ingress NGINX Controller"] -->|mitigates| B
    
    G["Course of Action: 
    Implement Network Policies"] -->|mitigates| A
    
    H["Course of Action: 
    Implement RBAC Restrictions"] -->|mitigates| A
    
    I["Course of Action: 
    Platform-Level Solutions"] -->|mitigates| A
    
    subgraph Cloud Platforms
        AWS["AWS EKS"]
        Azure["Azure AKS"]
        GCP["Google GKE"]
    end
    
    B --> AWS
    B --> Azure
    B --> GCP
    
    class A attackPattern;
    class B,C,D,E vulnerability;
    class F,G,H,I courseOfAction;
```

## Cross-Cloud Impact

The IngressNightmare vulnerability affects Kubernetes deployments across all major cloud providers:

- **AWS**: Amazon Elastic Kubernetes Service (EKS)
- **Azure**: Azure Kubernetes Service (AKS)
- **GCP**: Google Kubernetes Engine (GKE)

This visualization shows how the vulnerability chain works and the relationships between the different mitigation strategies.

## Key Points

1. The primary vulnerability (CVE-2025-1974) is exploited by the attack pattern
2. Three related vulnerabilities contribute to the attack chain
3. Four different courses of action are available to mitigate the risk
4. All major cloud platforms are affected by this vulnerability