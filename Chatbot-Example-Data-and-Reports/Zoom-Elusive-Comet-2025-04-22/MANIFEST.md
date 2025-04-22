# CAVEaT STIX Data - Zoom ELUSIVE COMET Attack

## Directory Contents

This directory contains STIX 2.1 formatted data documenting the ELUSIVE COMET threat actor's attack using Zoom's remote control feature to target cryptocurrency organizations and users.

### Overview Report

- `ELUSIVE-COMET-Zoom-Attack-Report.md` - Comprehensive research report documenting the attack, vulnerabilities, and mitigations

### STIX Objects

- `attack-pattern-zoom-remote-control-hijacking.json` - Documents the Zoom remote control hijacking technique
- `threat-actor-elusive-comet.json` - Describes the ELUSIVE COMET threat actor
- `vulnerability-zoom-remote-control-design.json` - Documents the design vulnerability in Zoom's remote control feature
- `malware-goopdate.json` - Documents the GOOPDATE credential stealer malware used in the attack

### Courses of Action (Mitigations)

- `course-of-action-org-restrictions.json` - Restricting Zoom remote control to organization members only
- `course-of-action-disable-remote-control.json` - Disabling Zoom remote control feature entirely
- `course-of-action-macos-pppc-profile.json` - Implementing macOS PPPC profiles to block Zoom accessibility permissions
- `course-of-action-macos-tcc-monitoring.json` - Implementing active TCC database monitoring for Zoom permissions
- `course-of-action-uninstall-zoom.json` - Completely removing Zoom and using browser alternatives
- `course-of-action-platform-architectural-solutions.json` - Platform-level architectural solutions for Zoom
- `course-of-action-user-education.json` - User education and training on Zoom remote control risks

### Relationships and Visualizations

- `relationships.json` - STIX relationships between all objects
- `relationship-diagram.mmd` - Mermaid diagram visualizing relationships between objects

## Usage

These STIX files can be imported into any STIX-compatible threat intelligence platform or viewed using STIX visualization tools. The comprehensive report provides detailed context and analysis for human readers.

## Generation Date

These files were generated on April 22, 2025, based on threat intelligence available at that time.
