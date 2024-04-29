3/22/24, 3:46 PM Brute Force: Password Cracking, Sub-technique T1110.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1110/002/ 1/4Thank you to Tidal Cyber and SOC Prime for becoming ATT&CK's ﬁrst Benefactors. To join the cohort, or learn more about this program visit our
Benefactors page.3/22/24, 3:46 PM Brute Force: Password Cracking, Sub-technique T1110.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1110/002/ 2/4Home>Techniques>Enterprise>Brute Force>Password Cracking3/22/24, 3:46 PM Brute Force: Password Cracking, Sub-technique T1110.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1110/002/ 3/4Brute Force: Password Cracking
Procedure Examples
ID Name Description
G0022 APT3 APT3 has been known to brute force password hashes to be able to leverage plain text credentials.
G0096 APT41 APT41 performed password brute-force attacks on the local admin account.
G0035 Dragonﬂy Dragonﬂy has dropped and executed tools used for password cracking, including Hydra and CrackMapExec.
G0037 FIN6 FIN6 has extracted password hashes from ntds.dit to crack oﬄine.
S0056 Net Crawler Net Crawler uses a list of known credentials gathered through credential dumping to guess passwords to
accounts as it spreads throughout a network.
C0002 Night
DragonDuring Night Dragon, threat actors used Cain & Abel to crack password hashes.
Mitigations
ID Mitigation Description
M1032 Multi-factor
AuthenticationUse multi-factor authentication. Where possible, also enable multi-factor authentication on
externally facing services.
M1027 Password Policies Refer to NIST guidelines when creating password policies. Adversaries may use password cracking to attempt to recover usable credentials, such as plaintext passwords, when credential material
such as password hashes are obtained. OS Credential Dumping can be used to obtain password hashes, this may only get an adversary so
far when Pass the Hash is not an option. Further, adversaries may leverage Data from Conﬁguration Repository in order to obtain hashed
credentials for network devices.
Techniques to systematically guess the passwords used to compute hashes are available, or the adversary may use a pre-computed rainbow
table to crack hashes. Cracking hashes is usually done on adversary-controlled systems outside of the target network. The resulting
plaintext password resulting from a successfully cracked hash may be used to log into systems, resources, and services in which the
account has access.Other sub-techniques of Brute Force (4)
[1]
[2]
Version PermalinkID: T1110.002
Sub-technique of:  T1110

Tactic: Credential Access

Platforms: Azure AD, Linux, Network, Oﬃce 365, Windows, macOS
Contributors: Mohamed Kmal
Version: 1.2
Created: 11 February 2020
Last Modiﬁed: 30 March 2023
[3]
[4]
[5]
[6]
[7]
[8]
[9]
[10]3/22/24, 3:46 PM Brute Force: Password Cracking, Sub-technique T1110.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1110/002/ 4/4Detection
ID Data Source Data Component Detects
DS0015 Application Log Application Log
ContentMonitor authentication logs for system and application login failures of Valid
Accounts. It is diﬃcult to detect when hashes are cracked, since this is generally done
outside the scope of the target network. Consider focusing efforts on detecting other
adversary behavior used to acquire credential materials, such as OS Credential
Dumping or Kerberoasting.
DS0002 User Account User Account
AuthenticationMonitor for many failed authentication attempts across various accounts that may
result from password spraying attempts. It is diﬃcult to detect when hashes are
cracked, since this is generally done outside the scope of the target network. (ex:
Windows EID 4625 or 5379)
References
1. US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-
Sponsored Cyber Actors Targeting Network Infrastructure
Devices. Retrieved October 19, 2020.
2. Wikipedia. (n.d.). Password cracking. Retrieved December 23,
2015.
3. Korban, C, et al. (2017, September). APT3 Adversary
Emulation Plan. Retrieved January 16, 2018.
4. Fraser, N., et al. (2019, August 7). Double DragonAPT41, a
dual espionage and cyber crime operation APT41. Retrieved
September 23, 2019.
5. US-CERT. (2018, March 16). Alert (TA18-074A): Russian
Government Cyber Activity Targeting Energy and Other Critical
Infrastructure Sectors. Retrieved June 6, 2018.. Kali. (2014, February 18). THC-Hydra. Retrieved November 2,
2017.
7. FireEye Threat Intelligence. (2016, April). Follow the Money:
Dissecting the Operations of the Cyber Crime Group FIN6.
Retrieved June 1, 2016.
. Cylance. (2014, December). Operation Cleaver. Retrieved
September 14, 2017.
9. McAfee® Foundstone® Professional Services and McAfee
Labs™. (2011, February 10). Global Energy Cyberattacks:
“Night Dragon”. Retrieved February 19, 2018.
10. Grassi, P., et al. (2017, December 1). SP 800-63-3, Digital
Identity Guidelines. Retrieved January 16, 2019.