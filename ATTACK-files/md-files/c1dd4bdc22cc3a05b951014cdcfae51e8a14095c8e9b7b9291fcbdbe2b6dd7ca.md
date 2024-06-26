3/22/24, 3:43 PM Masquerading: Rename System Utilities, Sub-technique T1036.003 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1036/003/ 1/4Thank you to Tidal Cyber and SOC Prime for becoming ATT&CK's ﬁrst Benefactors. To join the cohort, or learn more about this program visit our
Benefactors page.3/22/24, 3:43 PM Masquerading: Rename System Utilities, Sub-technique T1036.003 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1036/003/ 2/4Home>Techniques>Enterprise>Masquerading>Rename System Utilities3/22/24, 3:43 PM Masquerading: Rename System Utilities, Sub-technique T1036.003 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1036/003/ 3/4Masquerading: Rename System Utilities
Procedure Examples
ID Name Description
G0050 APT32 APT32 has moved and renamed pubprn.vbs to a .txt ﬁle to avoid detection.
S0046 CozyCar The CozyCar dropper has masqueraded a copy of the infected system's rundll32.exe executable that was
moved to the malware's install directory and renamed according to a predeﬁned conﬁguration ﬁle.
G0093 GALLIUM GALLIUM used a renamed cmd.exe ﬁle to evade detection.
S1020 Kevin Kevin has renamed an image of cmd.exe with a random name followed by a .tmpl extension.
G0032 Lazarus
GroupLazarus Group has renamed system utilities such as wscript.exe and mshta.exe .
G0045 menuPass menuPass has renamed certutil and moved it to a different location on the system to avoid detection based
on use of the tool.
Mitigations
ID Mitigation Description
M1022 Restrict File and Directory Permissions Use ﬁle system access controls to protect folders such as C:\Windows\System32.Adversaries may rename legitimate system utilities to try to evade security mechanisms concerning the usage of those utilities. Security
monitoring and control mechanisms may be in place for system utilities adversaries are capable of abusing. It may be possible to bypass
those security mechanisms by renaming the utility prior to utilization (ex: rename rundll32.exe ). An alternative case occurs when a
legitimate utility is copied or moved to a different directory and renamed to avoid detections based on system utilities executing from non-
standard paths. Other sub-techniques of Masquerading (9)
[1]
[2]
[3]
Version PermalinkID: T1036.003
Sub-technique of:  T1036

Tactic: Defense Evasion

Platforms: Linux, Windows, macOS
Version: 1.1
Created: 10 February 2020
Last Modiﬁed: 14 September 2023
[4]
[3]
[5]
[6]
[7]
[8]3/22/24, 3:43 PM Masquerading: Rename System Utilities, Sub-technique T1036.003 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1036/003/ 4/4Detection
ID Data SourceData Component Detects
DS0017 Command Command
ExecutionMonitor executed commands and arguments that may rename legitimate system utilities to
try to evade security mechanisms concerning the usage of those utilities.
DS0022 File File Metadata Collecting and comparing disk and resource ﬁlenames for binaries by looking to see if the
InternalName, OriginalFilename, and/or ProductName match what is expected could provide
useful leads, but may not always be indicative of malicious activity.
File
ModiﬁcationMonitor for changes made to ﬁles for unexpected modiﬁcations to ﬁle names that are
mismatched between the ﬁle name on disk and that of the binary's PE metadata. This is a
likely indicator that a binary was renamed after it was compiled.
Note: There are no standard Windows events for ﬁle modiﬁcation. However, Event ID 4663
(An attempt was made to access an object) can be used to audit and alert on attempts to
access system utility binaries; the "Accesses" ﬁeld can be used to ﬁlter by type of access (e.g.,
MODIFY vs DELETE).
DS0009 Process Process
MetadataMonitor for ﬁle names that are mismatched between the ﬁle name on disk and that of the
binary's PE metadata, this is a likely indicator that a binary was renamed after it was
compiled.
References
1. LOLBAS. (n.d.). Living Off The Land Binaries and Scripts (and
also Libraries). Retrieved February 10, 2020.
2. Ewing, P. (2016, October 31). How to Hunt: The Masquerade
Ball. Retrieved October 31, 2016.
3. F-Secure Labs. (2015, April 22). CozyDuke: Malware Analysis.
Retrieved December 10, 2015.
4. Carr, N.. (2017, December 26). Nick Carr Status Update APT32
pubprn. Retrieved April 22, 2019.5. Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A
Worldwide Campaign Against Telecommunications Providers.
Retrieved July 18, 2019.
. Kayal, A. et al. (2021, October). LYCEUM REBORN:
COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved
June 14, 2022.
7. Pradhan, A. (2022, February 8). LolZarus: Lazarus Group
Incorporating Lolbins into Campaigns. Retrieved March 22,
2022.
. Matsuda, A., Muhammad I. (2018, September 13). APT10
Targeting Japanese Corporations Using Updated TTPs.
Retrieved September 17, 2018.