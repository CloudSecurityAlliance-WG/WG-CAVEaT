# CAVEaT STIX Generator - Kubernetes Courses of Action Module

Version: 2025-04-29
Author: Kurt Seifried, kseifried@cloudsecurityalliance.org

## Purpose

This module provides detailed Kubernetes-specific guidance for implementing mitigations and courses of action for cloud security vulnerabilities. It includes standardized formats for kubectl commands, Kubernetes manifests, Helm charts, and security policy implementations that work across cloud providers.

## Kubernetes Implementation Standards

When documenting Kubernetes mitigations, follow these standards to ensure consistency and completeness:

### Kubernetes Resource Coverage

For each mitigation, identify which Kubernetes resources are involved, including:
- Primary resources (e.g., Pods, Deployments, Services)
- Supporting resources (e.g., NetworkPolicies, RBAC, PodSecurityPolicies)
- Integration points with cloud provider resources
- Dependencies and prerequisites

### Kubernetes Command Line Instructions

When documenting kubectl-based remediation steps:

1. **Command Structure**:
   - Provide the complete kubectl command with all required parameters
   - Include flags with descriptions
   - Show example values for variables
   - Include both the command and its expected output

2. **Prerequisites**:
   - Specify required kubectl version
   - Note any required authentication context
   - Include any necessary permissions or roles

3. **Format Template**:
   ```bash
   # Verify kubectl installation and version (if needed)
   kubectl version --client

   # Confirm connection to the cluster (if needed)
   kubectl cluster-info

   # Set context (if needed)
   kubectl config use-context my-cluster-context

   # Main remediation command
   kubectl [verb] [resource-type] [resource-name] \
     --flag1=value1 \
     --flag2=value2 \
     --flag3=value3

   # Verification command
   kubectl get [resource-type] [resource-name] -o yaml
   ```

### Kubernetes Manifest Files

When documenting YAML manifest-based remediation:

1. **Manifest Structure**:
   - Provide complete, validated YAML manifests
   - Include all required fields and security-relevant annotations
   - Add comments explaining security-relevant settings
   - Structure manifests for readability and maintainability

2. **Secure Defaults**:
   - Ensure manifests have secure default values
   - Apply principle of least privilege
   - Include resource limitations
   - Set appropriate security contexts

3. **Format Template**:
   ```yaml
   # secure-deployment.yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: secure-app
     namespace: default
     labels:
       app: secure-app
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: secure-app
     template:
       metadata:
         labels:
           app: secure-app
       spec:
         # Security context at the Pod level
         securityContext:
           fsGroup: 1000
           runAsNonRoot: true  # Prevent running as root
         containers:
         - name: secure-container
           image: myregistry/secure-app:1.0.0
           imagePullPolicy: Always  # Always pull latest image
           # Security context at the container level
           securityContext:
             allowPrivilegeEscalation: false  # Prevent privilege escalation
             capabilities:
               drop:
               - ALL  # Drop all capabilities
             readOnlyRootFilesystem: true  # Read-only file system
             runAsUser: 1000  # Run as non-root user
           resources:
             limits:
               cpu: "500m"
               memory: "512Mi"
             requests:
               cpu: "100m"
               memory: "128Mi"
           ports:
           - containerPort: 8080
   ```

### Helm Chart Remediation

When documenting Helm-based remediation:

1. **Chart Structure**:
   - Provide complete Helm chart configurations
   - Include all security-relevant values
   - Document proper installation and upgrade commands
   - Explain security impact of configuration options

2. **Values Configuration**:
   - Provide a values.yaml with secure defaults
   - Document security-relevant values
   - Explain the implications of each security setting

3. **Format Template**:
   ```bash
   # Install or upgrade a Helm chart with secure values
   helm upgrade --install my-release my-repo/my-chart \
     --values secure-values.yaml \
     --set securityContext.runAsNonRoot=true \
     --set securityContext.runAsUser=1000 \
     --set securityContext.readOnlyRootFilesystem=true
   ```

   ```yaml
   # secure-values.yaml
   # Security-focused values file for my-chart
   
   securityContext:
     # Run as non-root user
     runAsNonRoot: true
     runAsUser: 1000
     # Prevent privilege escalation
     allowPrivilegeEscalation: false
     # Use read-only root filesystem
     readOnlyRootFilesystem: true
     capabilities:
       drop:
       - ALL
   
   podSecurityContext:
     fsGroup: 1000
     
   # Network policy configuration
   networkPolicy:
     enabled: true
     ingressRules:
       - from:
         - podSelector:
             matchLabels:
               app: frontend
         ports:
         - port: 8080
           protocol: TCP
   
   # Resource limitations
   resources:
     limits:
       cpu: 500m
       memory: 512Mi
     requests:
       cpu: 100m
       memory: 128Mi
   
   # Image pull policy
   image:
     pullPolicy: Always
   ```

## Cross-Provider Kubernetes Security

### Cloud Provider Differences

Document how Kubernetes security implementations differ across cloud providers:

1. **Authentication and Authorization**:
   - AWS EKS: IAM integration, service account IAM roles
   - Azure AKS: Azure AD integration, managed identities
   - GCP GKE: IAM integration, Workload Identity

2. **Network Security**:
   - AWS EKS: AWS Security Groups, Calico CNI options
   - Azure AKS: Network Security Groups, Azure CNI
   - GCP GKE: Cloud Armor, GCP Firewall Rules

3. **Pod Security**:
   - AWS EKS: Pod Security Admission, Security Groups for Pods
   - Azure AKS: Pod Security Admission, Azure Policy for AKS
   - GCP GKE: Pod Security Admission, GKE Sandbox

### Provider-Agnostic Security Patterns

For each mitigation, include provider-agnostic security patterns that work across clouds:

1. **Format Template**:
   ```
   ## [Security Pattern Name]
   
   ### Universal Implementation
   [Provider-agnostic implementation details]
   
   ### Provider-Specific Considerations
   
   #### AWS EKS
   [AWS-specific implementation notes]
   
   #### Azure AKS
   [Azure-specific implementation notes]
   
   #### GCP GKE
   [GCP-specific implementation notes]
   ```

## Kubernetes Security Dimensions

For each Kubernetes vulnerability, address these key security dimensions:

### Pod Security

1. **Security Context Configuration**:
   ```yaml
   # Pod security context
   securityContext:
     runAsNonRoot: true
     runAsUser: 1000
     allowPrivilegeEscalation: false
     capabilities:
       drop:
       - ALL
     readOnlyRootFilesystem: true
   ```

2. **Pod Security Standards Implementation**:
   ```yaml
   # Namespace label for Pod Security Standards
   apiVersion: v1
   kind: Namespace
   metadata:
     name: secure-namespace
     labels:
       pod-security.kubernetes.io/enforce: restricted
       pod-security.kubernetes.io/audit: restricted
       pod-security.kubernetes.io/warn: restricted
   ```

3. **Resource Limits Enforcement**:
   ```yaml
   # Resource limits
   resources:
     limits:
       cpu: "500m"
       memory: "512Mi"
     requests:
       cpu: "100m"
       memory: "128Mi"
   ```

### Network Security

1. **Network Policy Implementation**:
   ```yaml
   # Basic network policy
   apiVersion: networking.k8s.io/v1
   kind: NetworkPolicy
   metadata:
     name: secure-network-policy
     namespace: default
   spec:
     podSelector:
       matchLabels:
         app: secure-app
     policyTypes:
     - Ingress
     - Egress
     ingress:
     - from:
       - podSelector:
           matchLabels:
             app: frontend
       ports:
       - protocol: TCP
         port: 8080
     egress:
     - to:
       - podSelector:
           matchLabels:
             app: backend
       ports:
       - protocol: TCP
         port: 5432
   ```

2. **Service Mesh Integration**:
   ```yaml
   # Istio authorization policy example
   apiVersion: security.istio.io/v1beta1
   kind: AuthorizationPolicy
   metadata:
     name: secure-auth-policy
     namespace: default
   spec:
     selector:
       matchLabels:
         app: secure-app
     rules:
     - from:
       - source:
           principals: ["cluster.local/ns/default/sa/frontend-service-account"]
       to:
       - operation:
           methods: ["GET"]
           paths: ["/api/v1/data"]
   ```

### Authentication and Authorization

1. **RBAC Configuration**:
   ```yaml
   # Role definition
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     namespace: default
     name: pod-reader
   rules:
   - apiGroups: [""]
     resources: ["pods"]
     verbs: ["get", "watch", "list"]
   ---
   # Role binding
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: read-pods
     namespace: default
   subjects:
   - kind: ServiceAccount
     name: api-service-account
     namespace: default
   roleRef:
     kind: Role
     name: pod-reader
     apiGroup: rbac.authorization.k8s.io
   ```

2. **Service Account Configuration**:
   ```yaml
   # Service account with limited privileges
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: restricted-service-account
     namespace: default
   automountServiceAccountToken: false  # Prevent automatic token mounting
   ```

### Secrets Management

1. **Kubernetes Secrets Best Practices**:
   ```yaml
   # Properly configured secret
   apiVersion: v1
   kind: Secret
   metadata:
     name: secure-secret
     namespace: default
   type: Opaque
   data:
     username: base64EncodedUsername
     password: base64EncodedPassword
   ```

2. **External Secrets Integration**:
   ```yaml
   # AWS Secrets Manager integration example
   apiVersion: external-secrets.io/v1beta1
   kind: ExternalSecret
   metadata:
     name: aws-secret
     namespace: default
   spec:
     refreshInterval: 1h
     secretStoreRef:
       kind: SecretStore
       name: aws-secretstore
     target:
       name: secret-from-aws
     data:
     - secretKey: username
       remoteRef:
         key: my-aws-secret
         property: username
     - secretKey: password
       remoteRef:
         key: my-aws-secret
         property: password
   ```

## Verification Methods

For each Kubernetes mitigation, include specific verification methods:

### kubectl Verification Commands
```bash
# Verify pod security context
kubectl get pod secure-app-pod -o jsonpath='{.spec.securityContext}'

# Verify network policies
kubectl get networkpolicy -n default

# Verify RBAC configuration
kubectl auth can-i get pods --as=system:serviceaccount:default:api-service-account

# Verify pod security admission enforcement
kubectl get ns secure-namespace -o jsonpath='{.metadata.labels}'
```

### Kubernetes Security Tools Integration

1. **Trivy Scanning**:
   ```bash
   # Scan Kubernetes resources
   trivy k8s --report summary cluster
   
   # Scan a specific namespace
   trivy k8s --report summary --namespace default
   ```

2. **Kube-bench Compliance Checks**:
   ```bash
   # Run CIS benchmark checks
   kube-bench run --targets master,node
   ```

3. **Falco Detection Rules**:
   ```yaml
   # Falco rule to detect privilege escalation
   - rule: Privilege Escalation
     desc: Detect privilege escalation activities in containers
     condition: spawned_process and container and not user_expected_terminal_shell_in_container_conditions and proc.name in (privilege_escalation_procs)
     output: "Privilege escalation activity detected in container (user=%user.name command=%proc.cmdline container=%container.name)"
     priority: WARNING
   ```

## Kubernetes Security Patterns

Include these common security patterns for Kubernetes deployments:

### Sidecar Security Pattern
```yaml
# Security sidecar pattern
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-with-security-sidecar
spec:
  replicas: 1
  selector:
    matchLabels:
      app: secure-app
  template:
    metadata:
      labels:
        app: secure-app
    spec:
      containers:
      - name: app-container
        image: myregistry/app:1.0.0
        ports:
        - containerPort: 8080
      - name: security-sidecar
        image: myregistry/security-sidecar:1.0.0
        volumeMounts:
        - name: shared-data
          mountPath: /var/log
      volumes:
      - name: shared-data
        emptyDir: {}
```

### Init Container Security Pattern
```yaml
# Security init container pattern
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-with-security-init
spec:
  replicas: 1
  selector:
    matchLabels:
      app: secure-app
  template:
    metadata:
      labels:
        app: secure-app
    spec:
      initContainers:
      - name: security-init
        image: myregistry/security-init:1.0.0
        securityContext:
          runAsNonRoot: true
        command: ['sh', '-c', 'configure-security.sh']
      containers:
      - name: app-container
        image: myregistry/app:1.0.0
        ports:
        - containerPort: 8080
```

### Multi-Level Security Pattern
```yaml
# Multi-level security pattern
apiVersion: v1
kind: Namespace
metadata:
  name: security-zone-a
  labels:
    security-level: restricted
    pod-security.kubernetes.io/enforce: restricted
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: zone-isolation
  namespace: security-zone-a
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          security-level: restricted
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          security-level: restricted
```

## Provider-Specific Extended Security

Include provider-specific extended security features when appropriate:

### AWS EKS Extended Security
```yaml
# Security Groups for Pods (AWS EKS specific)
apiVersion: vpcresources.k8s.aws/v1beta1
kind: SecurityGroupPolicy
metadata:
  name: security-group-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: secure-app
  securityGroups:
    groupIds:
      - sg-123456789abcdef0
```

### Azure AKS Extended Security
```yaml
# Azure Policy for AKS (Azure specific)
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sPodSecurityStandard
metadata:
  name: pss-restricted
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
  parameters:
    exemptImages: []
    version: "latest"
    level: "restricted"
```

### GCP GKE Extended Security
```yaml
# Binary Authorization (GCP GKE specific)
# This is configured at the cluster level in GCP console or with gcloud
# Example gcloud command:
gcloud container clusters update my-cluster \
  --enable-binauthz \
  --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE
```

## Compliance Mapping

When relevant, include Kubernetes compliance framework mappings:

1. **CIS Kubernetes Benchmark**:
   - Reference specific section numbers from CIS benchmark

2. **Common Compliance Standards**:
   - NIST 800-53 (specify control IDs)
   - PCI DSS (specify requirement numbers)
   - HIPAA (specify relevant controls)
   - ISO 27001 (specify control IDs)

Example compliance mapping:
```
This mitigation addresses:
- CIS Kubernetes Benchmark: 5.2.1, 5.2.2
- NIST 800-53: AC-3, AC-6
- PCI DSS: 7.1, 7.2
- ISO 27001: A.9.2, A.9.4
```

## Quality Checklist

Before finalizing Kubernetes mitigations, verify they meet these quality standards:

1. ☐ Security context properly configured at pod and container level
2. ☐ Resource limits set for all containers
3. ☐ Network policies implemented for both ingress and egress
4. ☐ RBAC follows principle of least privilege
5. ☐ Secrets are properly managed using best practices
6. ☐ Service accounts have appropriate privileges
7. ☐ Pod Security Standards applied at appropriate level
8. ☐ Verification methods included for all mitigations
9. ☐ Provider-specific considerations documented
10. ☐ Compliance mappings included where applicable
