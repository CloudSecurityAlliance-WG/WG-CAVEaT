# CAVEaT STIX Generator - Intelligence and Analysis Module

Version: 2025-04-29
Author: Kurt Seifried, kseifried@cloudsecurityalliance.org

## Purpose

This module provides templates and guidelines for creating intelligence-related STIX objects for cloud security threats. It focuses on Indicator, Observed Data, Opinion, Note, Report, and Grouping objects.

## Indicator Object

### STIX Indicator Requirements

A STIX Indicator object contains a pattern that can be used to detect suspicious or malicious cyber activity. For cloud environments, these include patterns that can detect cloud-specific attack behaviors.

#### Required Properties:
- **type**: Must be "indicator"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "indicator--unusual-cloud-api-calls")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **name**: A descriptive name for the indicator
- **pattern**: The detection pattern for this indicator
- **pattern_type**: The pattern language used in the pattern property
- **pattern_version**: The version of the pattern language
- **valid_from**: The time from which this indicator is considered valid

#### Recommended Properties:
- **description**: Detailed explanation of the indicator
- **indicator_types**: Types of indicator
- **valid_until**: The time at which this indicator should no longer be considered valid
- **kill_chain_phases**: Phases of the kill chain this indicator corresponds to
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Indicator Template

```json
{
  "type": "indicator",
  "spec_version": "2.1",
  "id": "indicator--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "name": "[Descriptive Name]",
  "description": "[Detailed description of the indicator, including its significance in cloud environments]",
  "indicator_types": ["[indicator-type]"],
  "pattern": "[pattern]",
  "pattern_type": "stix",
  "pattern_version": "2.1",
  "valid_from": "[timestamp]",
  "valid_until": "[timestamp]",
  "kill_chain_phases": [
    {
      "kill_chain_name": "mitre-attack",
      "phase_name": "[phase-name]"
    }
  ],
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

## Observed Data Object

### STIX Observed Data Requirements

A STIX Observed Data object conveys information about cyber security related entities such as files, systems, and networks. For cloud environments, these include observations of cloud service API calls, resource configurations, and user activities.

#### Required Properties:
- **type**: Must be "observed-data"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "observed-data--cloud-api-activity")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **first_observed**: The beginning of the time window during which the data was observed
- **last_observed**: The end of the time window during which the data was observed
- **number_observed**: The number of times the data was observed during the window

#### Recommended Properties:
- **objects**: Cyber observable objects observed
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Observed Data Template

```json
{
  "type": "observed-data",
  "spec_version": "2.1",
  "id": "observed-data--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "first_observed": "[timestamp]",
  "last_observed": "[timestamp]",
  "number_observed": [count],
  "objects": {
    "0": {
      "type": "[observable-type]",
      "property1": "value1",
      "property2": "value2"
    },
    "1": {
      "type": "[observable-type]",
      "property1": "value1",
      "property2": "value2"
    }
  },
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

## Opinion Object

### STIX Opinion Requirements

A STIX Opinion object represents an assessment of the correctness of information contained in another STIX object. For cloud environments, these include expert opinions on cloud-specific threats and indicators.

#### Required Properties:
- **type**: Must be "opinion"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "opinion--cloud-attack-assessment")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **object_refs**: References to the STIX Objects that the opinion is about
- **opinion**: The opinion that the producer has about all of the STIX Objects referenced in the object_refs property

#### Recommended Properties:
- **explanation**: A description of why the producer has this opinion
- **authors**: The authors of this opinion
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Opinion Template

```json
{
  "type": "opinion",
  "spec_version": "2.1",
  "id": "opinion--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "object_refs": ["[object-id-1]", "[object-id-2]"],
  "opinion": "strongly-agree",
  "explanation": "[Detailed explanation of why this opinion is held, including cloud security context]",
  "authors": ["[author-1]", "[author-2]"],
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

## Note Object

### STIX Note Requirements

A STIX Note object conveys informative text to provide further context and analysis not contained in other STIX objects. For cloud environments, these include additional context for cloud-specific threats and vulnerabilities.

#### Required Properties:
- **type**: Must be "note"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "note--cloud-threat-analysis")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **object_refs**: References to the STIX Objects that the note is about
- **content**: The content of the note

#### Recommended Properties:
- **abstract**: A brief summary of the note content
- **authors**: The authors of this note
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Note Template

```json
{
  "type": "note",
  "spec_version": "2.1",
  "id": "note--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "object_refs": ["[object-id-1]", "[object-id-2]"],
  "content": "[Detailed note content with cloud security context and analysis]",
  "abstract": "[Brief summary of the note]",
  "authors": ["[author-1]", "[author-2]"],
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

## Report Object

### STIX Report Requirements

A STIX Report object represents a collection of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including context and related details. For cloud environments, these include comprehensive reports on cloud security threats.

#### Required Properties:
- **type**: Must be "report"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "report--cloud-attack-analysis")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **name**: A descriptive name for this report
- **object_refs**: References to the STIX Objects that are included in this report
- **published**: The date this report was published

#### Recommended Properties:
- **description**: A description of the purpose or intent of this report
- **report_types**: The type(s) of report
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Report Template

```json
{
  "type": "report",
  "spec_version": "2.1",
  "id": "report--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "name": "[Descriptive Name]",
  "description": "[Detailed description of the report's purpose and contents related to cloud security]",
  "report_types": ["[report-type]"],
  "published": "[timestamp]",
  "object_refs": ["[object-id-1]", "[object-id-2]", "[object-id-3]"],
  "external_references": [
    {
      "source_name": "[Source Name]",
      "url": "[URL]",
      "description": "[Optional description]"
    }
  ]
}
```

## Grouping Object

### STIX Grouping Requirements

A STIX Grouping object explicitly asserts that the referenced STIX Objects have a shared context, unlike a STIX Bundle (which explicitly conveys no context). For cloud environments, these include groups of related cloud security threats or vulnerabilities.

#### Required Properties:
- **type**: Must be "grouping"
- **spec_version**: Must be "2.1"
- **id**: Unique identifier (use descriptive format like "grouping--cloud-attack-campaign")
- **created**: When this object was created (format: "2025-01-15T18:30:00.000Z")
- **modified**: When this object was last modified (format: "2025-01-15T18:30:00.000Z")
- **name**: A descriptive name for this grouping
- **object_refs**: References to the STIX Objects that are included in this grouping
- **context**: The context that defines this grouping

#### Recommended Properties:
- **description**: A description of the grouping
- **external_references**: References to sources of information
- **object_marking_refs**: Data markings for this object
- **granular_markings**: Granular markings for this object

### Grouping Template

```json
{
  "type": "grouping",
  "spec_version": "2.1",
  "id": "grouping--[descriptive-name]",
  "created": "[timestamp]",
  "modified": "[timestamp]",
  "name": "[Descriptive Name]",
  "description": "[Detailed description of the grouping and its cloud security context]",
  "context": "[grouping-context]",
  "object_refs": ["[object-id-1]", "[object-id-2]", "[object-id-3]"],
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

When linking intelligence-related objects to other STIX objects, use the following relationship patterns:

### Indicator Relationships
- **indicates**: An indicator indicates an attack pattern, campaign, intrusion set, malware, threat actor, or tool
- **based-on**: An indicator is based on observed data
- **derived-from**: An indicator is derived from another indicator

### Observed Data Relationships
- **derived-from**: Observed data is derived from other observed data
- **related-to**: Observed data is related to other STIX objects

### Opinion Relationships
- **object_refs**: An opinion references the STIX objects that the opinion is about

### Note Relationships
- **object_refs**: A note references the STIX objects that the note is about

### Report Relationships
- **object_refs**: A report references the STIX objects included in the report

### Grouping Relationships
- **object_refs**: A grouping references the STIX objects included in the grouping

## Quality Checklist

Before finalizing intelligence-related objects, verify they meet these quality standards:

1. ☐ Names clearly describe the indicator, report, note, or grouping
2. ☐ Descriptions include cloud-specific details and context
3. ☐ External references are included to credible sources
4. ☐ Patterns are accurate and effective for detection
5. ☐ Relationship mappings are logical and properly structured

## Cloud-Specific Considerations

When documenting intelligence for cloud environments, consider these cloud-specific aspects:

1. **Cloud Telemetry Sources**:
   - Document sources of cloud-specific telemetry (e.g., CloudTrail, Azure Monitor)
   - Note the types of events and logs available from cloud providers
   - Describe limitations in visibility across different service models

2. **Detection Challenges**:
   - Document challenges in detecting cloud-specific threats
   - Note differences in detection approaches between on-premises and cloud
   - Describe provider-specific detection capabilities and limitations

3. **Multi-Provider Intelligence**:
   - Document how to correlate intelligence across multiple cloud providers
   - Note provider-specific indicators and how they map to each other
   - Describe unified approaches to cloud threat detection

4. **Cloud-Native Analysis Methods**:
   - Document cloud-native approaches to threat analysis
   - Note the use of cloud services for security analytics
   - Describe automated response capabilities in cloud environments
