# WG-CAVEaT

WG-CAVEaT Working Group data

## CAVEaT Chatbot:

https://csaurl.org/WG-CAVEaT-Chatbot

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

### Mappings

* Mapping to categories from ATT&CK, FIGHT and so on - DONE
* Mapping to CSA CCM (https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4) including mitigations, controls, etc.
* Mapping to CSA Top Threats report (https://cloudsecurityalliance.org/research/topics/top-threats) including mitigations, controls, etc.
* Mapping to CWE (https://cwe.mitre.org/)
* Mapping to https://cloudsecurityalliance.org/artifacts/top-threats-to-cloud-computing-pandemic-eleven-deep-dive and other top 10s

### Additional sources for new CAVEaT

* https://cloudsecurityalliance.org/artifacts/top-threats-to-cloud-computing-pandemic-eleven-deep-dive
* https://www.cisa.gov/resources-tools/resources/cyber-safety-review-board-releases-report-microsoft-online-exchange-incident-summer-2023
