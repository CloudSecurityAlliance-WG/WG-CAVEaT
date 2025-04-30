# CAVEaT STIX Generator - Attack Vectors Module

Version: 2025-04-29
Author: Kurt Seifried, kseifried@cloudsecurityalliance.org

## Purpose
Guide creation of attack-related STIX objects for cloud security threats.

## Attack Pattern Object

### Required Properties
- **type**: "attack-pattern"
- **spec_version**: "2.1"
- **id**: Use descriptive format (e.g., "attack-pattern--cloud-storage-bucket-reregistration")
- **created**: Creation timestamp
- **modified**: Modification timestamp
- **name**: Descriptive name

### Recommended Properties
- **description**: Detailed explanation
- **kill_chain_phases**: Relevant kill chain phases
- **external_references**: Information sources

## Infrastructure Object

### Required Properties
- **type**: "infrastructure"
- **spec_version**: "2.1"
- **id**: Descriptive identifier
- **created**: Creation timestamp
- **modified**: Modification timestamp
- **name**: Descriptive name

### Recommended Properties
- **description**: Details about the infrastructure role
- **infrastructure_types**: Types of infrastructure
- **external_references**: Information sources

## Tool Object

### Required Properties
- **type**: "tool"
- **spec_version**: "2.1"
- **id**: Descriptive identifier
- **created**: Creation timestamp
- **modified**: Modification timestamp
- **name**: Descriptive name

### Recommended Properties
- **description**: Tool details including legitimate use and misuse
- **tool_types**: Types of tool
- **external_references**: Information sources

## Malware Object

### Required Properties
- **type**: "malware"
- **spec_version**: "2.1"
- **id**: Descriptive identifier
- **created**: Creation timestamp
- **modified**: Modification timestamp
- **name**: Descriptive name
- **is_family**: true/false

### Recommended Properties
- **description**: Malware details and cloud-specific targets
- **malware_types**: Types of malware
- **external_references**: Information sources

## Common Relationships

- **uses**: Actor/malware uses attack pattern or tool
- **targets**: Attack pattern targets vulnerability or identity
- **mitigated-by**: Attack pattern mitigated by course of action
- **delivers**: Attack pattern/tool delivers malware
- **consists-of**: Infrastructure consists of other components
- **communicates-with**: Infrastructure communication paths

## Cloud-Specific Considerations

1. **Multi-tenancy Impact**
   - Effect on other tenants
   - Isolation boundary breaches
   - Attack blast radius

2. **Service Model Variations**
   - IaaS/PaaS/SaaS implementation differences
   - Shared responsibility implications

3. **Provider-Specific Elements**
   - Cross-provider differences
   - Provider-specific defenses

4. **Cloud-Native Vectors**
   - Serverless/container specific attacks
   - Management plane vulnerabilities
   - Orchestration attacks
