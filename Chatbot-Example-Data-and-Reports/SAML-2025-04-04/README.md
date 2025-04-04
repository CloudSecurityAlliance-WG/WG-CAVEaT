# Silver SAML Attack STIX Documentation

This directory contains STIX 2.1 format documentation for the Silver SAML attack technique, discovered in early 2024. The Silver SAML attack is an evolution of the Golden SAML technique that was used in the SolarWinds breach.

## Contents

The STIX bundle has been split into multiple parts for easier handling:

1. **bundle-part1.json**: Contains the attack pattern and vulnerability objects
2. **bundle-part2.json**: Contains course of action and indicator objects
3. **bundle-part3.json**: Contains platform-level solution objects
4. **bundle-part4.json**: Contains the first set of relationships between objects
5. **bundle-part5.json**: Contains the remaining relationships and visualization

Additionally, this directory includes:

- **silver-saml-final-report.md**: A comprehensive human-readable report on the Silver SAML attack
- **Individual STIX objects**: Each STIX object is also available as a separate JSON file for easier reference

## Key Features

- Detailed technical information on the Silver SAML attack technique
- Analysis of impact across major cloud providers (Azure, AWS, GCP)
- Specific mitigations for each cloud provider with CLI, console, and API instructions
- Platform-level architectural solutions
- Indicators for detecting attack preparation and execution
- Visualization of relationships between STIX objects

## Summary

The Silver SAML attack enables threat actors to forge SAML authentication responses after obtaining the private key of an externally-generated certificate used by a cloud identity provider. Unlike Golden SAML which focused on AD FS, Silver SAML targets cloud identity providers directly, allowing attackers to impersonate any user to any application configured for SAML-based single sign-on.

This documentation provides a comprehensive overview of the attack vector, associated vulnerabilities, detection strategies, and mitigation approaches for security professionals working with cloud environments.

## Generation Date

This STIX content was generated on April 4, 2025, based on research and analysis of the Silver SAML attack technique discovered in early 2024.
