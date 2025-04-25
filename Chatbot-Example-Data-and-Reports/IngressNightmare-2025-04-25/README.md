# IngressNightmare Vulnerability - CAVEaT STIX Documentation

## Overview

This directory contains STIX 2.1 format documentation of the IngressNightmare vulnerability (CVE-2025-1974 and related CVEs) that affects Kubernetes deployments across multiple cloud providers. The vulnerability allows unauthenticated remote code execution in the Ingress NGINX Controller for Kubernetes.

## Files in this Directory

### STIX Files

- `ingress-nightmare-attack-pattern.json`: Documents the attack pattern for exploiting the IngressNightmare vulnerability
- `ingress-nightmare-vulnerabilities.json`: Contains detailed information about CVE-2025-1974 and related vulnerabilities
- `ingress-nightmare-courses-of-action.json`: Provides mitigation strategies for different cloud platforms
- `ingress-nightmare-relationships.json`: Shows the relationships between the STIX objects

### Documentation and Visualization

- `IngressNightmare-Final-Report.md`: Comprehensive report on the vulnerability, impacts, and mitigation strategies
- `ingress-nightmare-visualization.md`: Mermaid diagram visualizing the relationships between STIX objects
- `README.md`: This file, providing an overview of the directory contents

## Quick Reference

- **Primary CVE**: CVE-2025-1974
- **Related CVEs**: CVE-2025-1097, CVE-2025-1098, CVE-2025-24514
- **Affected Component**: Ingress NGINX Controller for Kubernetes
- **Affected Cloud Platforms**: AWS, Azure, GCP
- **Main Mitigation**: Update to Ingress NGINX Controller v1.9.5 or later

## How to Use These Files

The STIX files in this directory can be imported into STIX-compatible threat intelligence platforms or visualized using tools like the [OASIS STIX Visualizer](https://oasis-open.github.io/cti-stix-visualization/).

The Markdown report provides a human-readable analysis of the vulnerability and can be viewed in any Markdown reader.

## Generated

This documentation was generated on April 25, 2025, for the Cloud Security Alliance's CAVEaT (Cloud Adversarial Vectors, Exploits, and Threats) working group.