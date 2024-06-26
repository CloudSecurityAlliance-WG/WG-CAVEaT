3/22/24, 3:48 PM Cloud Service Dashboard, Technique T1538 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1538/ 1/1Thank you to Tidal Cyber and SOC Prime for becoming ATT&CK's ﬁrst Benefactors. To join the cohort, or learn more about this program visit our
Benefactors page.
Home>Techniques>Enterprise>Cloud Service Dashboard
Cloud Service Dashboard
Mitigations
ID Mitigation Description
M1018 User Account
ManagementEnforce the principle of least-privilege by limiting dashboard visibility to only the resources required.
This may limit the discovery value of the dashboard in the event of a compromised account.
Detection
ID Data Source Data Component Detects
DS0028 Logon Session Logon Session Creation Monitor for newly constructed logon behavior across cloud service management
consoles.
DS0002 User Account User Account
AuthenticationCorrelate other security systems with login information, such as user accounts, IP
addresses, and login names.
ReferencesAn adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an operational cloud
environment, such as speciﬁc services, resources, and features. For example, the GCP Command Center can be used to view all assets,
ﬁndings of potential security risks, and to run additional queries, such as ﬁnding public IP addresses and open ports.
Depending on the conﬁguration of the environment, an adversary may be able to enumerate more information via the graphical dashboard
than an API. This allows the adversary to gain information without making any API requests.[1]
Version PermalinkID: T1538
Sub-techniques:  No sub-techniques

Tactic: Discovery

Platforms: Azure AD, Google Workspace, IaaS, Oﬃce 365
Contributors: Praetorian
Version: 1.2
Created: 30 August 2019
Last Modiﬁed: 16 October 2023
[2]
[2]
1. Google. (2019, October 3). Quickstart: Using the dashboard.
Retrieved October 8, 2019.2. Pany, D. & Hanley, C. (2023, May 3). Cloudy with a Chance of
Bad Logs: Cloud Platform Log Conﬁgurations to Consider in
Investigations. Retrieved October 16, 2023.