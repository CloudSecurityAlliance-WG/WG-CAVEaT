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

## CAVEaT Local Setup

### Introduction

Setting up a local environment for CAVEaT work provides several important benefits:

- **Privacy and control**: Work with sensitive security information without exposing it to external services
- **Offline capabilities**: Continue development without requiring constant internet connectivity
- **Customization**: Tailor the environment to your specific workflow and preferences
- **Direct file access**: Seamlessly integrate with local git repositories and file systems
- **Consistency**: Ensure everyone on the team is using the same tooling and workflow

This guide will walk you through the process of setting up your local environment for contributing to the CAVEaT project, including repository configuration and AI tooling with Model Context Protocol support.

### Git Repository Setup for CTI Data Contributions

The CAVEaT project stores threat intelligence data in the CTI repository. To contribute to this data:

1. **Fork the repository**:
   - Visit https://github.com/CloudSecurityAlliance/cti/
   - Click the "Fork" button in the upper right corner
   - This creates your own copy of the repository under your GitHub account

2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/cti.git
   cd cti
   ```

3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/CloudSecurityAlliance/cti.git
   ```
   This allows you to keep your fork synchronized with the main repository.

4. **Create a branch for your work**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

5. **Make changes, commit, and push to your fork**:
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**:
   - Visit your fork on GitHub
   - Click "Pull Request"
   - Select your branch and the main repository's main branch
   - Provide a description of your changes
   - Submit the pull request

### Git Repository Setup for WG-CAVEaT Tools and Research Contributions

To contribute to the tools, prompts, and research components of CAVEaT:

1. **Fork the WG-CAVEaT repository**:
   - Visit https://github.com/CloudSecurityAlliance-WG/WG-CAVEaT
   - Click the "Fork" button in the upper right corner

2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/WG-CAVEaT.git
   cd WG-CAVEaT
   ```

3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/CloudSecurityAlliance-WG/WG-CAVEaT.git
   ```

4. **Create a branch for your contributions**:
   ```bash
   git checkout -b feature/your-contribution-name
   ```

5. **Make changes, commit, and push to your fork**:
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin feature/your-contribution-name
   ```

6. **Create a Pull Request**:
   - Visit your fork on GitHub
   - Click "Pull Request"
   - Select your branch and the main repository's main branch
   - Provide a description of your changes
   - Submit the pull request

### Setting Up Local AI with Model Context Protocol Support

The Model Context Protocol (MCP) allows AI assistants to interact with your local environment, including file systems and web services. This is essential for working effectively with the CAVEaT framework.

1. **Install MCP servers**:
   - Visit the official repository: http://github.com/modelcontextprotocol/servers/
   - Follow the installation instructions for your operating system
   - The CSA AI Tool Setup repository also provides helpful scripts: https://github.com/CloudSecurityAlliance/CSA-AI-Tool-Setup

2. **Required MCP servers**:
   - **Filesystem MCP server**: Allows the AI to read and write files on your system
   - **Fetch MCP server**: Enables retrieval of online resources
   - **Web search MCP server**: Provides search capabilities for research
   - **Git MCP server**: Allows direct interaction with git repositories

3. **Configuration**:
   - Each server requires specific configuration for permissions and access
   - Refer to the documentation in the CSA-AI-Tool-Setup repository for recommended configurations
   - Ensure you restrict file system access to only the necessary directories

### Working with the CAVEaT Prompts

The CAVEaT project maintains a collection of prompts that instruct AI assistants on how to work with the framework:

1. **Access the latest prompts**:
   - Browse the prompt directory: https://github.com/CloudSecurityAlliance-WG/WG-CAVEaT/tree/main/Chatbot/prompts
   - Clone this repository if you haven't already:
     ```bash
     git clone https://github.com/CloudSecurityAlliance-WG/WG-CAVEaT.git
     ```

2. **Loading prompts into your AI assistant**:
   - Use clear instructions to direct your AI to read the prompt file:
     ```
     Please read the latest prompt file in /User/KurtSeifried/GitHub/WG_CAVEaT/Chatbot/prompts/
     ```
   - Adapt the path to match your local directory structure

3. **Working with the CTI repository**:
   - Instruct the AI to output to your fork of the CTI repository:
     ```
     I want you to write the output files to the appropriate directories in /User/KurtSeifried/GitHub/cti/ in STIX format, using UUID's and make sure they are referenced correctly and so on
     ```
   - Again, adjust paths to match your local setup

### Claude Desktop-Specific Instructions

Claude Desktop can be configured to work with the CAVEaT framework:

1. **Installation**:
   - Download and install Claude Desktop from the official Anthropic website
   - Follow the standard installation instructions for your operating system

2. **MCP Integration**:
   - Claude Desktop supports the Model Context Protocol
   - Configure Claude to connect to your local MCP servers
   - This typically involves providing the server endpoints in Claude's settings

3. **Working with prompts**:
   - Start a new conversation
   - Ask Claude to read the prompt file from your local file system
   - Provide clear instructions about file paths and expected outputs

4. **Additional tips**:
   - For complex tasks, consider breaking them down into smaller steps
   - Verify Claude's understanding by asking it to summarize the task
   - Review generated STIX objects carefully before committing them to your repository

## CAVEaT Chatbot

The CAVEaT Chatbot is an AI-powered tool that helps security professionals navigate the CAVEaT framework and implement practical security controls. The chatbot serves as an interactive reference for cloud security threats and their mitigations.

- **ChatBot URL (v2)**: [https://csaurl.org/CAVEaT-Chatbot](https://csaurl.org/CAVEaT-Chatbot)
- **ChatBot URL (v3.2)**: [https://chatgpt.com/g/g-xXpnPwHaD-cloud-adversarial-vectors-and-threat-chatbot-v3-2](https://chatgpt.com/g/g-xXpnPwHaD-cloud-adversarial-vectors-and-threat-chatbot-v3-2)
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

### Current Chatbot Version

The current prompt version is v4 (April 2025), which includes significant enhancements:
- Expanded focus on platform-level architectural solutions that cloud providers could implement
- Comprehensive course of action development for both customer-level and provider-level mitigations
- Improved STIX data quality with descriptive IDs instead of random UUIDs
- Enhanced relationship mapping and visualization capabilities
- See `/Chatbot/prompts/ChatBot-v4.md` for the complete prompt specification

### Example Work

The repository includes example research and STIX objects for several cloud security threats:
- **Object Bucket Re-registration Attack** (April 2025): A comprehensive analysis of the vulnerability where deleted cloud storage buckets can be re-registered by attackers, enabling supply chain attacks and malware distribution. This example includes:
  * Attack pattern documentation
  * Vulnerability analysis
  * Cross-provider impact assessment (AWS, Azure, GCP)
  * Customer-level mitigation strategies
  * Platform-level architectural solutions
  * STIX objects with descriptive IDs
  * Relationship mapping and visualization
  * See `/Chatbot-Example-Data-and-Reports/Object-Buckets-2025-04-02/` for this example

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
- `/Chatbot/prompts/`: Contains the prompt specifications for different chatbot versions
- `/Chatbot-Example-Data-and-Reports/`: Contains example STIX objects and research reports
- `/data/`: Contains core CAVEaT entries and mappings
- `/file-utils/`: Utilities for file conversion and processing
- `/mapping-attempts/`: Mapping CAVEaT entries to other security frameworks

## Data Format Note

For internal representation, JSON is preferred, then either HTML or MD, finally text. For public threat intelligence sharing, we use STIX format in our CTI repository.
