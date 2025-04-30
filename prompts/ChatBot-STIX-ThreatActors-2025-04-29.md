# CAVEaT STIX Generator - Threat Actors and Campaigns Module

Version: 2025-04-29
Author: Kurt Seifried, kseifried@cloudsecurityalliance.org

## Purpose

This module provides templates and guidelines for creating threat actor-related STIX objects for cloud security threats. It focuses on Threat Actor, Intrusion Set, Campaign, and Identity objects.

## Threat Actor Object

### STIX Threat Actor Requirements

A STIX Threat Actor object represents individuals, groups, or organizations believed to be operating with malicious intent. For cloud environments, these include actors specifically targeting cloud infrastructure and services.

#### Required Properties:
- **type**: Must be "threat-actor"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "threat-actor--cloud-resource-hijacker")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **name**: A descriptive name for the threat actor

#### Recommended Properties:
- **description**: Detailed explanation of the threat actor
- **threat_actor_types**: Types of threat actor
- **aliases**: Alternative names used to identify this threat actor
- **roles**: Roles this threat actor plays
- **goals**: High-level goals of this threat actor
- **sophistication**: Level of sophistication of this threat actor
- **resource_level**: Level of resources available to this threat actor
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Threat Actor Template

```json
{
  "type": "threat-actor",
  "spec_version": "2.1",
  "id": "threat-actor--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "name": "[Descriptive Name]",
  "description": "[Detailed description of the threat actor, including their activities targeting cloud environments]",
  "threat_actor_types": ["[threat-actor-type]"],
  "aliases": ["[alias-1]", "[alias-2]"],
  "roles": ["[role]"],
  "goals": ["[goal-1]", "[goal-2]"],
  "sophistication": "[sophistication-level]",
  "resource_level": "[resource-level]",
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

## Intrusion Set Object

### STIX Intrusion Set Requirements

A STIX Intrusion Set object represents a grouped set of adversarial behaviors and resources with common properties believed to be orchestrated by a single organization. For cloud environments, these include collections of TTPs specifically targeting cloud services.

#### Required Properties:
- **type**: Must be "intrusion-set"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "intrusion-set--cloud-account-takeover")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **name**: A descriptive name for the intrusion set

#### Recommended Properties:
- **description**: Detailed explanation of the intrusion set
- **aliases**: Alternative names used to identify this intrusion set
- **first_seen**: When this intrusion set was first seen
- **last_seen**: When this intrusion set was last seen
- **goals**: High-level goals of this intrusion set
- **resource_level**: Level of resources available to this intrusion set
- **primary_motivation**: Primary motivation of this intrusion set
- **secondary_motivations**: Secondary motivations of this intrusion set
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Intrusion Set Template

```json
{
  "type": "intrusion-set",
  "spec_version": "2.1",
  "id": "intrusion-set--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "name": "[Descriptive Name]",
  "description": "[Detailed description of the intrusion set, including their cloud-focused TTPs and targeted services]",
  "aliases": ["[alias-1]", "[alias-2]"],
  "first_seen": "[timestamp]",
  "last_seen": "[timestamp]",
  "goals": ["[goal-1]", "[goal-2]"],
  "resource_level": "[resource-level]",
  "primary_motivation": "[motivation]",
  "secondary_motivations": ["[motivation-1]", "[motivation-2]"],
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

## Campaign Object

### STIX Campaign Requirements

A STIX Campaign object represents a grouping of adversarial behaviors that describes a set of malicious activities or attacks occurring over a period of time against a specific set of targets. For cloud environments, these include coordinated attacks against cloud providers or tenants.

#### Required Properties:
- **type**: Must be "campaign"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "campaign--cloud-crypto-mining")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **name**: A descriptive name for the campaign

#### Recommended Properties:
- **description**: Detailed explanation of the campaign
- **aliases**: Alternative names used to identify this campaign
- **first_seen**: When this campaign was first seen
- **last_seen**: When this campaign was last seen
- **objective**: Objective of this campaign
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Campaign Template

```json
{
  "type": "campaign",
  "spec_version": "2.1",
  "id": "campaign--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "name": "[Descriptive Name]",
  "description": "[Detailed description of the campaign, including its focus on cloud environments and timeline of activities]",
  "aliases": ["[alias-1]", "[alias-2]"],
  "first_seen": "[timestamp]",
  "last_seen": "[timestamp]",
  "objective": "[campaign-objective]",
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

## Identity Object

### STIX Identity Requirements

A STIX Identity object represents individuals, organizations, or groups, as well as classes of individuals, organizations, systems, or groups. For cloud environments, these include cloud service providers, cloud tenants, and cloud administrators.

#### Required Properties:
- **type**: Must be "identity"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "identity--cloud-provider")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **name**: A descriptive name for the identity
- **identity_class**: Type of identity (e.g., individual, organization, group)

#### Recommended Properties:
- **description**: Detailed explanation of the identity
- **sectors**: List of industry sectors this identity belongs to
- **contact_information**: Contact information for this identity
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Identity Template

```json
{
  "type": "identity",
  "spec_version": "2.1",
  "id": "identity--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "name": "[Descriptive Name]",
  "description": "[Detailed description of the identity, including its role in the cloud ecosystem]",
  "identity_class": "[identity-class]",
  "sectors": ["[sector-1]", "[sector-2]"],
  "contact_information": "[contact-information]",
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

## Relationships with Other Objects

When linking threat actor-related objects to other STIX objects, use the following relationship patterns:

### Threat Actor Relationships
- **uses**: A threat actor uses an attack pattern, malware, or tool
- **attributed-to**: A campaign or intrusion set is attributed to a threat actor
- **impersonates**: A threat actor impersonates an identity
- **located-at**: A threat actor is located at a location
- **targets**: A threat actor targets an identity or vulnerability

### Intrusion Set Relationships
- **attributed-to**: An intrusion set is attributed to a threat actor
- **compromises**: An intrusion set compromises infrastructure
- **originates-from**: An intrusion set originates from a location
- **targets**: An intrusion set targets an identity or vulnerability
- **uses**: An intrusion set uses an attack pattern, malware, or tool

### Campaign Relationships
- **attributed-to**: A campaign is attributed to a threat actor or intrusion set
- **originates-from**: A campaign originates from a location
- **targets**: A campaign targets an identity or vulnerability
- **uses**: A campaign uses an attack pattern, malware, or tool

### Identity Relationships
- **located-at**: An identity is located at a location
- **targets**: An identity targets another identity
- **related-to**: An identity is related to another identity

## Quality Checklist

Before finalizing threat actor-related objects, verify they meet these quality standards:

1. ☐ Names clearly describe the threat actor, intrusion set, campaign, or identity
2. ☐ Descriptions include cloud-specific details and impact
3. ☐ External references are included to credible sources
4. ☐ Motivations, goals, and sophistication are accurately described
5. ☐ Relationship mappings are logical and properly structured

## Cloud-Specific Considerations

When documenting threat actors for cloud environments, consider these cloud-specific aspects:

1. **Cloud-Specific TTPs**:
   - Document techniques specifically developed for cloud environments
   - Note differences in tactics between on-premises and cloud attacks
   - Describe cloud service-specific techniques

2. **Multi-Tenant Impact**:
   - Describe how threat actors leverage multi-tenancy
   - Document blast radius across tenants
   - Note techniques for breaking tenant isolation

3. **Service Provider Targeting**:
   - Document techniques targeting cloud providers rather than tenants
   - Note supply chain implications
   - Describe impact on provider and customer relationship

4. **Cloud-Native Motivations**:
   - Document motivations specific to cloud environments (e.g., cryptomining, data exfiltration)
   - Note the scale and impact potential of cloud attacks
   - Describe economic and strategic drivers
