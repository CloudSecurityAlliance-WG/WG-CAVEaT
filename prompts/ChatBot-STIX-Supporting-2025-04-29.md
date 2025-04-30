# CAVEaT STIX Generator - Supporting Objects Module

Version: 2025-04-29
Author: Kurt Seifried, kseifried@cloudsecurityalliance.org

## Purpose

This module provides templates and guidelines for creating supporting STIX objects for cloud security threats. It focuses on Location objects, Relationship objects, and Sighting objects.

## Location Object

### STIX Location Requirements

A STIX Location object represents a geographic location. For cloud environments, these include physical locations of data centers, infrastructure, and threat actors, as well as logical locations like cloud regions and availability zones.

#### Required Properties:
- **type**: Must be "location"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "location--cloud-region-us-east-1")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")

#### Recommended Properties:
- **name**: A descriptive name for this location
- **description**: A detailed description of the location
- **latitude**: The latitude of the location
- **longitude**: The longitude of the location
- **precision**: The precision of the coordinates
- **region**: The region that contains this location
- **country**: The country that contains this location
- **administrative_area**: The administrative area that contains this location
- **city**: The city that contains this location
- **street_address**: The street address that contains this location
- **postal_code**: The postal code for this location
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Location Template

```json
{
  "type": "location",
  "spec_version": "2.1",
  "id": "location--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "name": "[Descriptive Name]",
  "description": "[Detailed description of the location, including its significance in cloud environments]",
  "latitude": [latitude],
  "longitude": [longitude],
  "precision": [precision],
  "region": "[region]",
  "country": "[country]",
  "administrative_area": "[administrative_area]",
  "city": "[city]",
  "street_address": "[street_address]",
  "postal_code": "[postal_code]",
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

### Cloud Region Location Template

Cloud environments have specific location considerations. Use this template for cloud regions:

```json
{
  "type": "location",
  "spec_version": "2.1",
  "id": "location--cloud-region-[region-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "name": "[Cloud Provider] Region [Region Name]",
  "description": "Cloud region representing [description of geographic coverage]. This is a logical location that may encompass multiple physical data centers.",
  "region": "[geographic region]",
  "country": "[primary country or countries]",
  "external_references": [
    {
      "source_name": "[Cloud Provider Documentation]",
      "url": "[URL to region documentation]",
      "description": "Official documentation for this cloud region"
    }
  ],
  "x_cloud_region_properties": {
    "provider": "[cloud provider name]",
    "region_id": "[provider-specific region identifier]",
    "availability_zones": ["[zone-1]", "[zone-2]", "[zone-3]"],
    "service_availability": "[information about services available in this region]"
  }
}
```

## Relationship Object

### STIX Relationship Requirements

A STIX Relationship object links together two STIX Domain Objects (SDOs) or STIX Cyber-observable Objects (SCOs) to describe how they are related. For cloud environments, these include relationships between cloud-specific threats, vulnerabilities, and mitigations.

#### Required Properties:
- **type**: Must be "relationship"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "relationship--targets")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **relationship_type**: The type of relationship
- **source_ref**: The ID of the source object
- **target_ref**: The ID of the target object

#### Recommended Properties:
- **description**: A description of the relationship
- **start_time**: The time at which the relationship began
- **stop_time**: The time at which the relationship ended
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Relationship Template

```json
{
  "type": "relationship",
  "spec_version": "2.1",
  "id": "relationship--[relationship-type]-[source-type]-[target-type]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "relationship_type": "[relationship-type]",
  "source_ref": "[source-object-id]",
  "target_ref": "[target-object-id]",
  "description": "[Detailed description of the relationship in a cloud security context]",
  "start_time": "[timestamp]",
  "stop_time": "[timestamp]",
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

### Common Cloud Security Relationship Types

For cloud security STIX objects, these are the most common relationship types:

1. **Attack Pattern Relationships**:
   - `targets`: An attack pattern targets a vulnerability or identity
   - `uses`: An attack pattern uses a tool or malware
   - `mitigated-by`: An attack pattern is mitigated by a course of action

2. **Vulnerability Relationships**:
   - `exploited-by`: A vulnerability is exploited by an attack pattern
   - `mitigated-by`: A vulnerability is mitigated by a course of action
   - `affects`: A vulnerability affects an identity (e.g., cloud service)

3. **Course of Action Relationships**:
   - `mitigates`: A course of action mitigates a vulnerability or attack pattern
   - `implemented-by`: A course of action is implemented by an identity
   - `investigates`: A course of action investigates an indicator

4. **Threat Actor Relationships**:
   - `targets`: A threat actor targets an identity or vulnerability
   - `uses`: A threat actor uses an attack pattern, malware, or tool
   - `attributed-to`: A campaign is attributed to a threat actor

5. **Cloud Provider and Service Relationships**:
   - `has`: A cloud provider has a vulnerability
   - `provides`: A cloud provider provides a service
   - `hosts`: A cloud service hosts infrastructure or data

### Relationship Mapping Examples

```json
{
  "type": "relationship",
  "spec_version": "2.1",
  "id": "relationship--targets-attack-pattern-cloud-service",
  "created": "2025-01-15T18:30:00.000Z",
  "modified": "2025-01-15T18:30:00.000Z",
  "relationship_type": "targets",
  "source_ref": "attack-pattern--cloud-storage-bucket-reregistration",
  "target_ref": "identity--cloud-storage-service",
  "description": "This attack pattern specifically targets cloud storage services by exploiting the deletion lifecycle of storage resources."
}
```

```json
{
  "type": "relationship",
  "spec_version": "2.1",
  "id": "relationship--mitigates-course-of-action-vulnerability",
  "created": "2025-01-15T18:30:00.000Z",
  "modified": "2025-01-15T18:30:00.000Z",
  "relationship_type": "mitigates",
  "source_ref": "course-of-action--implement-bucket-retention-policy",
  "target_ref": "vulnerability--cloud-storage-bucket-reuse",
  "description": "Implementing bucket retention policies mitigates the vulnerability of cloud storage buckets being reused after deletion by preventing immediate deletion."
}
```

## Sighting Object

### STIX Sighting Requirements

A STIX Sighting object represents the belief that something in cyber threat intelligence (e.g., an indicator, malware, tool, threat actor, etc.) was seen. For cloud environments, these include observations of cloud-specific threats and indicators.

#### Required Properties:
- **type**: Must be "sighting"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "sighting--cloud-attack-indicator")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **sighting_of_ref**: The ID of the object that was sighted
- **count**: The number of times the object was sighted
- **first_seen**: The beginning of the time window during which the object was sighted
- **last_seen**: The end of the time window during which the object was sighted

#### Recommended Properties:
- **description**: A description of the sighting
- **observed_data_refs**: The IDs of the observed data objects that contain the raw cyber data for this sighting
- **where_sighted_refs**: The IDs of the identities that saw the object
- **summary**: Whether this sighting should be considered a summary sighting
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Sighting Template

```json
{
  "type": "sighting",
  "spec_version": "2.1",
  "id": "sighting--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "sighting_of_ref": "[sighted-object-id]",
  "count": [count],
  "first_seen": "[timestamp]",
  "last_seen": "[timestamp]",
  "description": "[Detailed description of the sighting in a cloud security context]",
  "observed_data_refs": ["[observed-data-id-1]", "[observed-data-id-2]"],
  "where_sighted_refs": ["[identity-id-1]", "[identity-id-2]"],
  "summary": false,
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

### Cloud Sighting Considerations

For cloud environments, sightings have special considerations:

1. **Cloud Telemetry Sources**:
   - Document the source of the sighting (e.g., CloudTrail, Azure Activity Logs)
   - Note the specific log types or event categories
   - Include service-specific context

2. **Multi-tenant Implications**:
   - Document whether the sighting applies to a single tenant or multiple tenants
   - Note the blast radius across tenants
   - Include isolation boundary considerations

3. **Cloud Provider Reporting**:
   - Document whether the sighting was reported by the cloud provider
   - Note any provider-specific incident response activities
   - Include provider notifications or advisories

4. **Regional Context**:
   - Document the specific cloud regions or availability zones where the sighting occurred
   - Note any geographic patterns or targeting
   - Include regulatory implications

### Cloud Sighting Example

```json
{
  "type": "sighting",
  "spec_version": "2.1",
  "id": "sighting--cloud-storage-bucket-enumeration",
  "created": "2025-01-15T18:30:00.000Z",
  "modified": "2025-01-15T18:30:00.000Z",
  "sighting_of_ref": "indicator--excessive-storage-api-calls",
  "count": 1243,
  "first_seen": "2025-01-01T00:00:00.000Z",
  "last_seen": "2025-01-07T23:59:59.000Z",
  "description": "Multiple instances of excessive API calls to list and enumerate cloud storage buckets, potentially indicating reconnaissance activity. Observed across multiple tenants in the us-east-1 region.",
  "observed_data_refs": ["observed-data--cloudtrail-storage-api-logs"],
  "where_sighted_refs": ["identity--cloud-security-service"],
  "summary": false,
  "external_references": [
    {
      "source_name": "Cloud Provider Security Advisory",
      "url": "https://example.com/security-advisory/2025-01",
      "description": "Advisory detailing unusual storage API activity"
    }
  ],
  "x_cloud_sighting_details": {
    "provider": "AWS",
    "regions": ["us-east-1", "us-west-2"],
    "affected_tenants": 37,
    "services": ["S3"],
    "detection_source": "CloudTrail",
    "event_types": ["ListBuckets", "GetBucketPolicy", "GetBucketAcl"],
    "anomaly_detection": {
      "baseline_deviation": "867% above normal activity",
      "confidence": "high"
    }
  }
}
```

## Relationship Visualization

For complex sets of STIX objects, create a Mermaid diagram showing the relationships:

```
graph TD
    AP[Attack Pattern: Cloud Storage Bucket Reregistration] --> |exploits| V[Vulnerability: Cloud Storage Bucket Reuse]
    V --> |affects| ID[Identity: Cloud Storage Service]
    TA[Threat Actor: Data Exfiltration Group] --> |uses| AP
    COA1[CoA: Implement Bucket Retention Policy] --> |mitigates| V
    COA2[CoA: Monitor Deletion Events] --> |mitigates| AP
    I[Indicator: Rapid Bucket Creation After Deletion] --> |indicates| AP
    S[Sighting] --> |sighting_of| I
    ID --> |located_at| L[Location: Cloud Region]
```

## Quality Checklist

Before finalizing supporting objects, verify they meet these quality standards:

1. ☐ Location objects include appropriate geographic or logical cloud locations
2. ☐ Relationship objects use proper relationship types
3. ☐ Relationship sources and targets are logically consistent
4. ☐ Sighting objects include appropriate cloud context
5. ☐ External references are included to credible sources

## Cloud-Specific Considerations

When documenting supporting objects for cloud environments, consider these cloud-specific aspects:

1. **Cloud Geography**:
   - Document both physical and logical cloud locations
   - Note differences between geographic regions and availability zones
   - Include data sovereignty implications

2. **Relationship Complexity**:
   - Document complex relationship chains involving cloud services
   - Note dependencies between cloud components
   - Include service integration points

3. **Sighting Frequency**:
   - Document the scale and frequency of cloud-specific sightings
   - Note patterns that indicate automated attacks
   - Include baseline deviations that trigger alerts

4. **Multi-provider Context**:
   - Document how objects relate across different cloud providers
   - Note mapping between equivalent services
   - Include cross-provider attack patterns and relationships
