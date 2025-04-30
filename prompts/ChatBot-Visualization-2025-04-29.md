# CAVEaT STIX Generator - Visualization Module

Version: 2025-04-29
Author: Kurt Seifried, kseifried@cloudsecurityalliance.org

## Purpose
Guidelines for creating relationship visualizations and research reports for cloud threats in STIX format.

## Mermaid Diagram Standards

### Basic Structure
- Use graph TD (top-down) for hierarchical relationships
- Use graph LR (left-right) for sequential flows
- Label nodes with object type and name
- Use consistent arrow styles for relationship types

### Node Representation
- Include object type prefix (e.g., "Attack Pattern: Name")
- Use consistent shapes for different object types
- Keep labels concise but descriptive

### Relationship Representation
- Label lines with relationship_type
- Use arrows to show direction (source → target)
- Group related relationships

### Visual Organization
- Minimize crossing lines
- Group objects by category or function
- Position key objects centrally

## Visualization Best Practices
- Limit diagrams to 15-20 nodes
- Use subgraphs for grouping
- Position primary threat centrally
- Include brief legend for complex diagrams
- Ensure relationship types match STIX specifications

## Research Report Structure

### Core Components
1. **Executive Summary**: Overview, key findings, affected services
2. **Technical Details**: Description, attack mechanism, root cause
3. **Cross-Provider Analysis**: AWS, Azure, GCP specific impacts
4. **Courses of Action**: Implementation instructions for each provider
5. **STIX Objects Summary**: Visual representation and relationships
6. **References**: Sources and research methodology

### Formatting Guidelines
- Use consistent header hierarchy
- Format code blocks with language specification
- Use tables for comparisons
- Include mermaid diagrams for visualizations
- Bold important points, use code formatting for technical terms

## Report Quality Standards
- Technical accuracy across all providers
- Complete coverage of all sections
- Clear explanations of concepts
- Cloud-specific focus
- Consistent formatting

## Cloud-Specific Considerations
- Note service evolution and API dependencies
- Address shared responsibility model implications
- Include compliance context where relevant
- Consider cost implications of mitigations
