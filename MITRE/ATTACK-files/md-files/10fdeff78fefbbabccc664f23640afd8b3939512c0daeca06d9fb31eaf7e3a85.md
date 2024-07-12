3/22/24, 3:43 PM Masquerading: Invalid Code Signature, Sub-technique T1036.001 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1036/001/ 1/4Thank you to Tidal Cyber and SOC Prime for becoming ATT&CK's ﬁrst Benefactors. To join the cohort, or learn more about this program visit our
Benefactors page.3/22/24, 3:43 PM Masquerading: Invalid Code Signature, Sub-technique T1036.001 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1036/001/ 2/4Home>Techniques>Enterprise>Masquerading>Invalid Code Signature3/22/24, 3:43 PM Masquerading: Invalid Code Signature, Sub-technique T1036.001 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1036/001/ 3/4Masquerading: Invalid Code Signature
Procedure Examples
ID Name Description
G0067 APT37 APT37 has signed its malware with an invalid digital certiﬁcates listed as "Tencent Technology (Shenzhen)
Company Limited."
S0128 BADNEWS BADNEWS is sometimes signed with an invalid Authenticode certiﬁcate in an apparent effort to make it look
more legitimate.
S0666 Gelsemium Gelsemium has used unveriﬁed signatures on malicious DLLs.
S0198 NETWIRE The NETWIRE client has been signed by fake and invalid digital certiﬁcates.
S1050 PcShare PcShare has used an invalid certiﬁcate in attempt to appear legitimate.
S0019 Regin Regin stage 1 modules for 64-bit systems have been found to be signed with fake certiﬁcates masquerading as
originating from Microsoft Corporation and Broadcom Corporation.
G0112 Windshift Windshift has used revoked certiﬁcates to sign malware.
S0466 WindTail WindTail has been incompletely signed with revoked certiﬁcates.
Mitigations
ID Mitigation Description
M1045 Code Signing Require signed binaries.Adversaries may attempt to mimic features of valid code signatures to increase the chance of deceiving a user, analyst, or tool. Code signing
provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. Adversaries can
copy the metadata and signature information from a signed program, then use it as a template for an unsigned program. Files with invalid
code signatures will fail digital signature validation checks, but they may appear more legitimate to users and security tools may improperly
handle these ﬁles.
Unlike Code Signing, this activity will not result in a valid signature.Other sub-techniques of Masquerading (9)
[1]
Version PermalinkID: T1036.001
Sub-technique of:  T1036

Tactic: Defense Evasion

Platforms: Windows, macOS
Version: 1.0
Created: 10 February 2020
Last Modiﬁed: 10 February 2020
[2]
[3]
[4]
[5]
[6]
[7]
[8][9]
[8]3/22/24, 3:43 PM Masquerading: Invalid Code Signature, Sub-technique T1036.001 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1036/001/ 4/4Detection
ID Data SourceData ComponentDetects
DS0022 File File Metadata Collect and analyze signing certiﬁcate metadata and check signature validity on software that
executes within the environment, look for invalid signatures as well as unusual certiﬁcate
characteristics and outliers.
References
1. Vest, J. (2017, October 9). Borrowing Microsoft MetaData and
Signatures to Hide Binary Payloads. Retrieved September 10,
2019.
2. Raiu, C., and Ivanov, A. (2016, June 17). Operation Daybreak.
Retrieved February 15, 2018.
3. Lunghi, D., et al. (2017, December). Untangling the Patchwork
Cyberespionage Group. Retrieved July 10, 2018.
4. Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved
November 30, 2021.
5. McAfee. (2015, March 2). Netwire RAT Behind Recent Targeted
Attacks. Retrieved February 15, 2018.. Vrabie, V. (2020, November). Dissecting a Chinese APT
Targeting South Eastern Asian Government Institutions.
Retrieved September 19, 2022.
7. Kaspersky Lab's Global Research and Analysis Team. (2014,
November 24). THE REGIN PLATFORM NATION-STATE
OWNAGE OF GSM NETWORKS. Retrieved December 1, 2014.
. Wardle, Patrick. (2018, December 20). Middle East Cyber-
Espionage analyzing WindShift's implant: OSX.WindTail (part
1). Retrieved October 3, 2019.
9. Karim, T. (2018, August). TRAILS OF WINDSHIFT. Retrieved
June 25, 2020.