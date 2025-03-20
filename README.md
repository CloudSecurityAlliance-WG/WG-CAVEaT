# WG-CAVEaT (Cloud Adversarial Vectors, Exploits, and Threats)

## About the Project

The WG-CAVEaT (Cloud Adversarial Vectors, Exploits, and Threats) Working Group focuses on identifying, documenting, and mitigating cloud-specific security threats and attack vectors. Our mission is to create a comprehensive framework—similar to MITRE ATT&CK—but specifically tailored to cloud environments.

### Key Objectives

- **Identify and document** cloud-specific attack vectors, techniques, and vulnerabilities
- **Provide actionable remediation guidance** for AWS, Azure, GCP, and other cloud platforms
- **Map cloud threats** to established security frameworks and control matrices
- **Develop detection methods** to help organizations identify attack attempts
- **Create practical tools and resources** for security practitioners to improve cloud security posture
- **Publish standardized threat intelligence** using STIX format for interoperability

You can learn more about the [CAVEaT Working Group in Circle](https://circle.cloudsecurityalliance.org/community-home1?communitykey=cce2fd58-ba71-4280-9e3d-018c352d4100).

If you are interested in contributing to this project, please [sign up with your email address](https://csaurl.org/WG-CAVEaT-Form)

## STIX Data and CTI Repository

The CAVEaT data is published in the Structured Threat Information Expression (STIX) format, a standardized language for cyber threat intelligence. This enables interoperability with other threat intelligence platforms and tools.

- **CTI Repository**: [https://github.com/cloudsecurityalliance/cti](https://github.com/cloudsecurityalliance/cti)

Using the STIX format allows:
- Integration with existing threat intelligence platforms
- Automated processing and analysis of cloud threats
- Standardized sharing of threat data across organizations
- Mapping CAVEaT entries to ATT&CK and other frameworks
- Consistent representation of tactics, techniques, and procedures

## CAVEaT Chatbot

The CAVEaT Chatbot is an AI-powered tool that helps security professionals navigate the CAVEaT framework and implement practical security controls. The chatbot serves as an interactive reference for cloud security threats and their mitigations.

- **ChatBot URL (v2)**: [https://csaurl.org/CAVEaT-Chatbot](https://csaurl.org/CAVEaT-Chatbot)
- **ChatBot URL (v3)**: [https://chatgpt.com/g/g-xXpnPwHaD-cloud-adversarial-vectors-and-threat-solutions-v3](https://chatgpt.com/g/g-xXpnPwHaD-cloud-adversarial-vectors-and-threat-solutions-v3)
- **ChatBot data**: [https://github.com/Cloudsecurityalliance-Chatbots/chatbot-CAVEaT-data](https://github.com/Cloudsecurityalliance-Chatbots/chatbot-CAVEaT-data)

### Chatbot Capabilities

The GPT-powered chatbot is designed to assist users in exploring and understanding the Cloud Adversarial Vectors and Threats (CAVEaT) dataset. It provides:

- **Detailed explanations** of cloud attack vectors and adversarial tactics
- **Actionable defensive strategies** tailored to specific threats and cloud providers
- **Clear explanations** of complex cybersecurity terminology and concepts
- **Interactive query handling** for specific threats or categories
- **Up-to-date security guidance** aligned with current cybersecurity best practices
- **Cloud provider-specific remediation steps** for AWS, Azure, and GCP

The chatbot prioritizes delivering practical, implementable security controls that organizations can use to strengthen their cloud security posture.

## Current Work and Roadmap

### In Progress

- Identifying vendor-specific CAVEaT files that need more vendor-neutral coverage across AWS/Azure/GCP
- Developing a new template structure with detailed sections for:
  * Description
  * Examples
  * Mitigations (specific to each cloud provider)
  * Detection methods
  * References
- Adding cloud provider-specific guidance for security controls
- Mapping CAVEaT entries to established security frameworks
- Expanding the knowledge base with real-world case studies
- Converting all CAVEaT data to standardized STIX format for the CTI repository

### Planned Mappings

#### Cloud Security Alliance
- Mapping to [CSA CAIQ/CCM](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4)
- Mapping to [CSA Top Threats report](https://cloudsecurityalliance.org/research/topics/top-threats) including mitigations, controls, etc.
- Mapping to [CSA Pandemic 11](https://cloudsecurityalliance.org/artifacts/top-threats-to-cloud-computing-pandemic-eleven-deep-dive) and other top 10s

#### MITRE Frameworks
- [ATLAS](https://atlas.mitre.org/)
- [ATT&CK](https://attack.mitre.org/)
- [CAVEaT](https://github.com/CloudSecurityAlliance-WG/WG-CAVEaT/tree/main/CAVEaT-files/md-files)
- [FIGHT](https://fight.mitre.org/)
- [ICS](https://attack.mitre.org/techniques/ics/)
- [CWE](https://cwe.mitre.org/)
- [CVE](https://github.com/cveproject/cvelistV5/)

#### Center for Threat Informed Defense
- [ALL DATA](https://github.com/center-for-threat-informed-defense/mappings-explorer/tree/main/mappings)
- [AWS](https://center-for-threat-informed-defense.github.io/mappings-explorer/external/aws/) 
- [Azure](https://center-for-threat-informed-defense.github.io/mappings-explorer/external/aws/)
- [CVE](https://center-for-threat-informed-defense.github.io/mappings-explorer/external/cve/)
- [GCP](https://center-for-threat-informed-defense.github.io/mappings-explorer/external/gcp/)
- [NIST 800-53](https://center-for-threat-informed-defense.github.io/mappings-explorer/external/nist/)
- [M365](https://center-for-threat-informed-defense.github.io/mappings-explorer/external/m365/)
- [VERIS](https://center-for-threat-informed-defense.github.io/mappings-explorer/external/veris/)

## Repository Organization

- `/Chatbot/`: Contains the chatbot implementation and knowledge base
- `/data/`: Contains core CAVEaT entries and mappings
- `/file-utils/`: Utilities for file conversion and processing
- `/mapping-attempts/`: Mapping CAVEaT entries to other security frameworks

## Data Format Note

For internal representation, JSON is preferred, then either HTML or MD, finally text. For public threat intelligence sharing, we use STIX format in our CTI repository.
