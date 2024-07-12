# WG-CAVEaT (Cloud Adversarial Vectors, Exploits, and Threats)

WG-CAVEaT Working Group data, you can find out more about the (CAVEaT Working Group in Circle)[https://circle.cloudsecurityalliance.org/community-home1?communitykey=cce2fd58-ba71-4280-9e3d-018c352d4100].

If you are interested in this project feel free to (sign up with your email address)[https://csaurl.org/WG-CAVEaT-Form]

## CAVEaT Chatbot:

https://csaurl.org/WG-CAVEaT-Chatbot

https://github.com/Cloudsecurityalliance-Chatbots/chatbot-CAVEaT-data

The prompt is:

> The GPT-powered chatbot is designed to assist users in exploring and understanding the Cloud Adversarial, Vectors,
> and Threats (CAVEaT) dataset, which focuses on cloud-based cyber threats similar to the MITRE ATT&CK framework. The
> bot will:
>
> Explain Specific Attacks and Vectors: Provide detailed explanations of various cloud attack vectors and adversarial
> tactics listed in CAVEaT, ensuring users have a comprehensive understanding of each entry.
> Recommend Defensive Measures: Suggest actionable defensive strategies and best practices tailored to specific threats,
> helping users to mitigate potential vulnerabilities.
> Clarify Concepts and Terminology: Help users understand complex cybersecurity terminology and concepts related to
> cloud security, enhancing their ability to apply this knowledge practically.
> Interactive Query Handling: Respond to user queries about specific threats or categories by fetching and interpreting
> relevant data from the CAVEaT dataset.
> Accuracy and Reliability: Deliver information that is accurate, up-to-date, and aligned with current cybersecurity
> best practices. Avoid speculation and ensure all recommendations are supported by verified data.
> User Engagement and Feedback: Engage with users to gather feedback on the utility of the information provided and
> suggestions for expanding the CAVEaT dataset.
> The chatbot will prioritize clear, concise, and contextually relevant information delivery to support cybersecurity
> professionals and enthusiasts in navigating and mitigating cloud security threats effectively.

And the data is the CAVEaT-files/CAVEaT-all-entries.html file


## TODO

* Identify which CAVEaT files are vendor specific and need a more vendor neutral writeup and coverage with AWS/Azure/GCE.
* Figure out a new template
  * Description
  * Examples
  * Mitigations
  * Detection
  * References
* Additional data
  * AWS/Azure/GCE and other vendor and service specific information
  * Mappings to other standards
  * Controls
  * Technical Impact
  * Business Impact
* Have AI build the case studies to add additional entries e.g. https://github.com/mitre-atlas/atlas-data/tree/main/data/case-studies

### Mappings

* Cloud Security Alliance
  * Mapping to CSA CAIQ/CCM (https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4)
  * Mapping to CSA Top Threats report (https://cloudsecurityalliance.org/research/topics/top-threats) including mitigations, controls, etc.
  * Mapping to CSA Pandemic 11 https://cloudsecurityalliance.org/artifacts/top-threats-to-cloud-computing-pandemic-eleven-deep-dive and other top 10s
* MITRE 
  * ATLAS - https://atlas.mitre.org/ https://atlas.mitre.org/resources/info
  * ATT&CK - https://attack.mitre.org/ https://github.com/mitre-attack/attack-stix-data
  * CAVEaT - https://github.com/CloudSecurityAlliance-WG/WG-CAVEaT/tree/main/CAVEaT-files/md-files
  * FIGHT - https://fight.mitre.org/ https://fight.mitre.org/fight.yaml
  * ICS - https://attack.mitre.org/techniques/ics/
  * CWE - https://cwe.mitre.org/
  * CVE - https://github.com/cveproject/cvelistV5/
* Center for Threat Informed Defense https://center-for-threat-informed-defense.github.io/mappings-explorer/ (get JSON files)
  * ALL DATA: https://github.com/center-for-threat-informed-defense/mappings-explorer/tree/main/mappings
  * AWS - https://center-for-threat-informed-defense.github.io/mappings-explorer/external/aws/ 
  * Azure - https://center-for-threat-informed-defense.github.io/mappings-explorer/external/aws/
  * CVE - https://center-for-threat-informed-defense.github.io/mappings-explorer/external/cve/
  * GCP - https://center-for-threat-informed-defense.github.io/mappings-explorer/external/gcp/
  * NIST 800-53 - https://center-for-threat-informed-defense.github.io/mappings-explorer/external/nist/
  * M365 - https://center-for-threat-informed-defense.github.io/mappings-explorer/external/m365/
  * VERIS - https://center-for-threat-informed-defense.github.io/mappings-explorer/external/veris/

## A note on data formats

JSON is preferred, then either HTML or MD, finally text.
