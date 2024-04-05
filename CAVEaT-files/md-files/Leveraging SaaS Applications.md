# Leveraging SaaS Applications (version 1.0)

**Cloud Service Label:** SaaS IaaS

## Description

The adversary is trying to communicate with compromised systems to control them. Command and Control consists of techniques that adversaries may use to communicate with systems under their control within a victim network. Adversaries commonly attempt to mimic normal expected traffic to avoid detection. There are many ways an adversary can establish command and control with various levels of stealth depending on the victim’s network structure and defenses.

## Examples

| Name     | Description |
|----------|-------------|
| SLUB     | Malware spreading through unique watering hole websites and vulnerabilities CVE-2018-8174 and CVE-2019-0752. Command and Control vectors include GitHub and Slack, with a significant focus on the latter. Utilizes TLS from APIs to evade detection since it is presented as normal network traffic. |
| SaaSy_boi | Proof-of-Concept project presented at DEFCON27. The purpose is to establish CnC vectors through various SaaS and social media services. Examples include Slack, Twitter, and GitHub, starting by retrieving their respective API keys. SaaSy_boi offers file upload, download, and execute functionality, creating reverse shells and actively taking screenshots of the compromised machine. |
| Gcat     | Python-based backdoor that uses Gmail as a CnC server. |
| Twittor  | Python-based backdoor that uses Twitter direct messages (DM’s) as a CnC server. |
| Slackor  | A GoLang project that uses Slack as a CnC server. |

## Mitigations

| Mitigation                             | Description |
|----------------------------------------|-------------|
| Manage log data like other sensitive data | Ensure log data is protected and managed like any other confidential data source, with encryption at rest and positive control. |
| Cloud Access Security Broker           | Implement CASB solutions to ensure cloud resources are being properly accessed. |
| Endpoint Detection                     | Anti-virus or malware detection services will flag and protect against any suspicious information and files. |
| Disable unnecessary SaaS               | Adversaries could potentially exploit available Enterprise SaaS the same as an open port or service on a machine. Harden, lockdown, or outright disable any SaaS that is not needed. |

## Detections

| Detection                             | Description |
|---------------------------------------|-------------|
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: Create a metric filter that checks for IAM policy changes and the `<cloudtrail_log_group_name>`. Create an SNS topic. Create an SNS subscription to the above topic. Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively. |
| Monitor Activity in AWS Account       | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports that can be run on a daily basis. Azure AD Identity Protection shows current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | Similar to the AWS detection, involves creating metric filters and alarms for CloudTrail changes. |
| Create Activity Log Alerts in Azure   | Instructions for creating log activity alerts for deletion in the Azure Console, including navigation and alert rule setup. |
| Create View and Manage Activity Alerts in Azure Monitor | Steps to create, view, and manage log alerts in the Azure portal. |
| Azure Resource Manager Templates      | Description of using Azure Resource Manager templates for configuring metric alerts in Azure Monitor. |
| Enable CloudTrail across all regions in AWS | Steps to enable CloudTrail logging across all AWS regions. |
| Configure log profile to capture activity logs for all regions in Azure | Instructions for setting up activity logs for all regions in the Azure console. |

## References

- https://blog.trendmicro.com/trendlabs-security-intelligence/slub-gets-rid-of-github-intensifies-slack-use/. Accessed July 9, 2020.
- https://www.youtube.com/watch?v=m5NxE9yZjR4. Accessed July 9, 2020.
- https://github.com/netskopeOSS/saasy_boi. Accessed July 9, 2020.
- https://github.com/byt3bl33d3r/gcat. Accessed July 9, 2020.
- https://github.com/PaulSec/twittor. Accessed July 9, 2020.
- https://github.com/Coalfire-Research/Slackor. Accessed July 9, 2020.

(© 2022 The MITRE Corporation All Rights Reserved.
