3/22/24, 3:45 PM Subvert Trust Controls: Code Signing, Sub-technique T1553.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1553/002/ 1/8Thank you to Tidal Cyber and SOC Prime for becoming ATT&CK's ﬁrst Benefactors. To join the cohort, or learn more about this program visit our
Benefactors page.3/22/24, 3:45 PM Subvert Trust Controls: Code Signing, Sub-technique T1553.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1553/002/ 2/8Home>Techniques>Enterprise>Subvert Trust Controls>Code Signing3/22/24, 3:45 PM Subvert Trust Controls: Code Signing, Sub-technique T1553.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1553/002/ 3/8Subvert Trust Controls: Code Signing
Adversaries may create, acquire, or steal code signing materials to sign their malware or tools. Code signing provides a level of authenticity
on a binary from the developer and a guarantee that the binary has not been tampered with. The certiﬁcates used during an operation may
be created, acquired, or stolen by the adversary. Unlike Invalid Code Signature, this activity will result in a valid signature.
Code signing to verify software on ﬁrst run can be used on modern Windows and macOS systems. It is not used on Linux due to the
decentralized nature of the platform. 
Code signing certiﬁcates may be used to bypass security policies that require signed code to execute on a system.Other sub-techniques of Subvert Trust Controls (6)
[1]
[2][3]
[1][4]
Version PermalinkID: T1553.002
Sub-technique of:  T1553

Tactic: Defense Evasion

Platforms: Windows, macOS

Defense Bypassed: Windows User Account Control
Version: 1.1
Created: 05 February 2020
Last Modiﬁed: 22 September 20223/22/24, 3:45 PM Subvert Trust Controls: Code Signing, Sub-technique T1553.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1553/002/ 4/8Procedure Examples
ID Name Description
S0504 Anchor Anchor has been signed with valid certiﬁcates to evade detection by security tools.
S0584 AppleJeus AppleJeus has used a valid digital signature from Sectigo to appear legitimate.
G0096 APT41 APT41 leveraged code-signing certiﬁcates to sign malware when targeting both gaming and non-
gaming organizations.
S0475 BackConﬁg BackConﬁg has been signed with self signed digital certiﬁcates mimicking a legitimate software
company.
S0234 Bandook Bandook was signed with valid Certum certiﬁcates.
S0534 Bazar Bazar has been signed with fake certiﬁcates including those appearing to be from VB CORPORATE
PTY. LTD.
S1070 Black Basta The Black Basta dropper has been digitally signed with a certiﬁcate issued by Akeo Consulting for
legitimate executables used for creating bootable USB drives.
S0520 BLINDINGCAN BLINDINGCAN has been signed with code-signing certiﬁcates such as CodeRipper.
S0415 BOOS TWRITE BOOS TWRITE has been signed by a valid CA.
C0015 C0015 For C0015, the threat actors used DLL ﬁles that had invalid certiﬁcates.
S0144 ChChes ChChes samples were digitally signed with a certiﬁcate originally used by Hacking Team that was later
leaked and subsequently revoked.
S0611 Clop Clop can use code signing to evade detection.
S0154 Cobalt Strike Cobalt Strike can use self signed Java applets to execute signed applet attacks.
G0052 CopyKittens CopyKittens digitally signed an executable with a stolen certiﬁcate from legitimate company AI
Squared.
S0527 CSPY Downloader CSPY Downloader has come signed with revoked certiﬁcates.
G0012 Darkhotel Darkhotel has used code-signing certiﬁcates on its malware that are either forged due to weak keys or
stolen. Darkhotel has also stolen certiﬁcates and signed backdoors and downloaders with them.
S0187 Daserf Some Daserf samples were signed with a stolen digital certiﬁcate.
S0377 Ebury Ebury has installed a self-signed RPM package mimicking the original system package on RPM based
systems.
S0624 Ecipekac Ecipekac has used a valid, legitimate digital signature to evade detection.
G1003 Ember Bear Ember Bear has used stolen certiﬁcates from Electrum Technologies GmbH to sign payloads.
S0091 Epic Turla has used valid digital certiﬁcates from Sysprint AG to sign its Epic dropper.
G0037 FIN6 FIN6 has used Comodo code-signing certiﬁcates.
G0046 FIN7 FIN7 has signed Carbanak payloads with legally purchased code signing certiﬁcates. FIN7 has also
digitally signed their phishing documents, backdoors and other staging tools to bypass security
controls.[5]
[6]
[7][8]
[9]
[10]
[11]
[12]
[13]
[14]
[15]
[16][17][18]
[19]
[20][21]
[22]
[23]
[24][25]
[26]
[27]
[28]
[29]
[30]
[31]
[32][33]3/22/24, 3:45 PM Subvert Trust Controls: Code Signing, Sub-technique T1553.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1553/002/ 5/8ID Name Description
G0093 GALLIUM GALLIUM has used stolen certiﬁcates to sign its tools including those from Whizzimo LLC.
S0168 Gazer Gazer versions are signed with various valid certiﬁcates; one was likely faked and issued by Comodo
for "Solid Loop Ltd," and another was issued for "Ultimate Computer Support Ltd."
S0342 GreyEnergy GreyEnergy digitally signs the malware with a code-signing certiﬁcate.
S0170 Helminth Helminth samples have been signed with legitimate, compromised code signing certiﬁcates owned by
software company AI Squared.
S0697 HermeticWiper The HermeticWiper executable has been signed with a legitimate certiﬁcate issued to Hermetica Digital
Ltd.
S0698 HermeticWizard HermeticWizard has been signed by valid certiﬁcates assigned to Hermetica Digital.
S0163 Janicab Janicab used a valid AppleDeveloperID to sign the code to get past security restrictions.
G0094 Kimsuky Kimsuky has signed ﬁles with the name EGIS CO,. Ltd..
G0032 Lazarus Group Lazarus Group has digitally signed malware and utilities to evade detection.
G0065 Leviathan Leviathan has used stolen code signing certiﬁcates to sign malware.
S0372 LockerGoga LockerGoga has been signed with stolen certiﬁcates in order to make it look more legitimate.
G1014 LuminousMoth LuminousMoth has signed their malware with a valid digital signature.
G0045 menuPass menuPass has resized and added data to the certiﬁcate table to enable the signing of modiﬁed ﬁles
with legitimate signatures.
S0455 Metamorfo Metamorfo has digitally signed executables using AVAST Software certiﬁcates.
G0021 Molerats Molerats has used forged Microsoft code-signing certiﬁcates on malware.
S0284 More\_eggs More\_eggs has used a signed binary shellcode loader and a signed Dynamic Link Library (DLL) to
create a reverse shell.
G1009 Moses Staff Moses Staff has used signed drivers from an open source tool called DiskCryptor to evade detection.
S0210 Nerex Nerex drops a signed Microsoft DLL to disk.
C0022 Operation Dream
JobDuring Operation Dream Job, Lazarus Group digitally signed their own malware to evade detection.
C0006 Operation
HoneybeeDuring Operation Honeybee, the threat actors deployed the MaoCheng dropper with a stolen Adobe
Systems digital signature.
G0040 Patchwork Patchwork has signed malware with self-signed certiﬁcates from ﬁctitious and spoofed legitimate
software companies.
S0501 PipeMon PipeMon, its installer, and tools are signed with stolen code-signing certiﬁcates.
G0056 PROMETHIUM PROMETHIUM has signed code with self-signed certiﬁcates.
S0650 QakBot QakBot can use signed loaders to evade detection.
S0262 QuasarRAT A QuasarRAT .dll ﬁle is digitally signed by a certiﬁcate from AirVPN.[34]
[35][36]
[37]
[38]
[39][40][41][42]
[43]
[44]
[45]
[46]
[47][48]
[49]
[50]
[28]
[51]
[52]
[31]
[53]
[54]
[55]
[56]
[9]
[57]
[58]
[59][60]
[61]3/22/24, 3:45 PM Subvert Trust Controls: Code Signing, Sub-technique T1553.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1553/002/ 6/8ID Name Description
S0148 RTM RTM samples have been signed with a code-signing certiﬁcates.
G1015 Scattered Spider Scattered Spider has used self-signed and stolen certiﬁcates originally issued to NVIDIA and Global
Software LLC.
G0091 Silence Silence has used a valid certiﬁcate to sign their primary loader Silence.Downloader (aka TrueBot).
C0024 SolarWinds
CompromiseDuring the SolarWinds Compromise, APT29 was able to get SUNBURST signed by SolarWinds code
signing certiﬁcates by injecting the malware into the SolarWinds Orion software lifecycle.
S0646 SpicyOmelette SpicyOmelette has been signed with valid digital certiﬁcates.
S0491 StrongPity StrongPity has been signed with self-signed certiﬁcates.
S0603 Stuxnet Stuxnet used a digitally signed driver with a compromised Realtek certiﬁcate.
G0039 Suckﬂy Suckﬂy has used stolen certiﬁcates to sign its malware.
S0559 SUNBURST SUNBURST was digitally signed by SolarWinds from March - May 2020.
S0663 SysUpdate SysUpdate has been signed with stolen digital certiﬁcates.
G0092 TA505 TA505 has signed payloads with code signing certiﬁcates from Thawte and Sectigo.
S0266 TrickBot TrickBot has come with a signed downloader component.
G0044 Winnti Group Winnti Group used stolen certiﬁcates to sign its malware.
G0102 Wizard Spider Wizard Spider has used Digicert code-signing certiﬁcates for some of its malware.
Mitigations
This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of system features.
Detection
ID Data SourceData ComponentDetects
DS0022 File File Metadata Collect and analyze signing certiﬁcate metadata on software that executes within the
environment to look for unusual certiﬁcate characteristics and outliers.[62]
[63]
[64]
[65]
[66]
[58]
[67]
[68]
[65]
[69]
[70][71][72]
[5]
[73]
[74]3/22/24, 3:45 PM Subvert Trust Controls: Code Signing, Sub-technique T1553.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1553/002/ 7/8References
1. Wikipedia. (2015, November 10). Code Signing. Retrieved
March 31, 2016.
2. Ladikov, A. (2015, January 29). Why You Shouldn’t Completely
Trust Files Signed with Digital Certiﬁcates. Retrieved March
31, 2016.
3. Shinotsuka, H. (2013, February 22). How Attackers Steal
Private Keys from Digital Certiﬁcates. Retrieved March 31,
2016.
4. Howard Oakley. (2020, November 16). Checks on executable
code in Catalina and Big Sur: a ﬁrst draft. Retrieved September
21, 2022.
5. Dahan, A. et al. (2019, December 11). DROPPING ANCHOR:
FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE
ANCHOR MALWARE. Retrieved September 10, 2020.
. Cybersecurity and Infrastructure Security Agency. (2021,
February 21). AppleJeus: Analysis of North Korea’s
Cryptocurrency Malware. Retrieved March 1, 2021.
7. Fraser, N., et al. (2019, August 7). Double DragonAPT41, a
dual espionage and cyber crime operation APT41. Retrieved
September 23, 2019.
. Rostovcev, N. (2021, June 10). Big airline heist APT41 likely
behind a third-party attack on Air India. Retrieved August 26,
2021.
9. Hinchliffe, A. and Falcone, R. (2020, May 11). Updated
BackConﬁg Malware Targeting Government and Military
Organizations in South Asia. Retrieved June 17, 2020.
10. Check Point. (2020, November 26). Bandook: Signed &
Delivered. Retrieved May 31, 2021.
11. Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS:
FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved
November 18, 2020.
12. Check Point. (2022, October 20). BLACK BASTA AND THE
UNNOTICED DELIVERY. Retrieved March 8, 2023.
13. US-CERT. (2020, August 19). MAR-10295134-1.v1 – North
Korean Remote Access Trojan: BLINDINGCAN. Retrieved
August 19, 2020.
14. Carr, N, et all. (2019, October 10). Mahalo FIN7: Responding to
the Criminal Operators’ New Tools and Techniques. Retrieved
October 11, 2019.
15. DFIR Report. (2021, November 29). CONTInuing the Bazar
Ransomware Story. Retrieved September 29, 2022.
1. Miller-Osborn, J. and Grunzweig, J.. (2017, February 16).
menuPass Returns with New Malware and New Attacks
Against Japanese Academics and Organizations. Retrieved
March 1, 2017.
17. Nakamura, Y.. (2017, February 17). ChChes - Malware that
Communicates with C&C Servers Using Cookie Headers.
Retrieved March 1, 2017.
1. PwC and BAE Systems. (2017, April). Operation Cloud Hopper:
Technical Annex. Retrieved April 13, 2017.
19. Santos, D. (2021, April 13). Threat Assessment: Clop
Ransomware. Retrieved July 30, 2021.
20. Mavis, N. (2020, September 21). The Art and Science of
Detecting Cobalt Strike. Retrieved April 6, 2021.
21. Strategic Cyber LLC. (2020, November 5). Cobalt Strike:
Advanced Threat Tactics for Penetration Testers. Retrieved
April 13, 2021.
22. ClearSky Cyber Security and Trend Micro. (2017, July).
Operation Wilted Tulip: Exposing a cyber espionage
apparatus. Retrieved August 21, 2017.3. ClearSky Cybersecurity. (2017, January 5). Iranian Threat
Agent OilRig Delivers Digitally Signed Malware, Impersonates
University of Oxford. Retrieved May 3, 2017.
39. Symantec Threat Hunter Team. (2022, February 24). Ukraine:
Disk-wiping Attacks Precede Russian Invasion. Retrieved
March 25, 2022.
40. Thomas, W. et al. (2022, February 25). CrowdStrike Falcon
Protects from New Wiper Malware Used in Ukraine
Cyberattacks. Retrieved March 25, 2022.
41. ESET. (2022, February 24). HermeticWiper: New data wiping
malware hits Ukraine. Retrieved March 25, 2022.
42. Dani, M. (2022, March 1). Ukrainian Targets Hit by
HermeticWiper, New Datawiper Malware. Retrieved March 25,
2022.
43. ESET. (2022, March 1). IsaacWiper and HermeticWizard: New
wiper and worm targetingUkraine. Retrieved April 10, 2022.
44. Thomas. (2013, July 15). New signed malware called Janicab.
Retrieved July 17, 2017.
45. ThreatConnect. (2020, September 28). Kimsuky Phishing
Operations Putting In Work. Retrieved October 30, 2020.
4. Saini, A. and Hossein, J. (2022, January 27). North Korea’s
Lazarus APT leverages Windows Update client, GitHub in
latest campaign. Retrieved January 27, 2022.
47. FireEye. (2018, March 16). Suspected Chinese Cyber
Espionage Group (TEMP.Periscope) Targeting U.S. Engineering
and Maritime Industries. Retrieved April 11, 2018.
4. Plan, F., et al. (2019, March 4). APT40: Examining a China-
Nexus Espionage Actor. Retrieved March 18, 2019.
49. Greenberg, A. (2019, March 25). A Guide to LockerGoga, the
Ransomware Crippling Industrial Firms. Retrieved July 17,
2019.
50. Lechtik, M, and etl. (2021, July 14). LuminousMoth APT:
Sweeping attacks for the chosen few. Retrieved October 20,
2022.
51. Erlich, C. (2020, April 3). The Avast Abuser: Metamorfo
Banking Malware Hides By Abusing Avast Executable.
Retrieved May 26, 2020.
52. Villeneuve, N., Haq, H., Moran, N. (2013, August 23).
OPERATION MOLERATS: MIDDLE EAST CYBER ATTACKS
USING POISON IVY. Retrieved April 1, 2016.
53. Checkpoint Research. (2021, November 15). Uncovering
MosesStaff techniques: Ideology over Money. Retrieved
August 11, 2022.
54. Ladley, F. (2012, May 15). Backdoor.Nerex. Retrieved February
23, 2018.
55. Breitenbacher, D and Osis, K. (2020, June 17). OPERATION
IN(TER)CEPTION: Targeted Attacks Against European
Aerospace and Military Companies. Retrieved December 20,
2021.
5. Sherstobitoff, R. (2018, March 02). McAfee Uncovers
Operation Honeybee, a Malicious Document Campaign
Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.
57. Tartare, M. et al. (2020, May 21). No “Game over” for the
Winnti Group. Retrieved August 24, 2020.
5. Tudorica, R. et al. (2020, June 30). StrongPity APT - Revealing
Trojanized Tools, Working Hours and Infrastructure. Retrieved
July 20, 2020.
59. Morrow, D. (2021, April 15). The rise of QakBot. Retrieved
September 27, 2021.3/22/24, 3:45 PM Subvert Trust Controls: Code Signing, Sub-technique T1553.002 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1553/002/ 8/823. Dahan, A. et al. (2020, November 2). Back to the Future: Inside
the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.
24. Kaspersky Lab's Global Research and Analysis Team. (2014,
November). The Darkhotel APT A Story of Unusual Hospitality.
Retrieved November 12, 2014.
25. Kaspersky Lab's Global Research & Analysis Team. (2015,
August 10). Darkhotel's attacks in 2015. Retrieved November
2, 2018.
2. DiMaggio, J. (2016, April 28). Tick cyberespionage group
zeros in on Japan. Retrieved July 16, 2018.
27. M.Léveillé, M.. (2014, February 21). An In-depth Analysis of
Linux/Ebury. Retrieved April 19, 2019.
2. GREAT. (2021, March 30). APT10: sophisticated multi-layered
loader Ecipekac discovered in A41APT campaign. Retrieved
June 17, 2021.
29. Unit 42. (2022, February 25). Spear Phishing Attacks Target
Organizations in Ukraine, Payloads Include the Document
Stealer OutSteel and the Downloader SaintBot. Retrieved June
9, 2022.
30. Kaspersky Lab's Global Research and Analysis Team. (2014,
August 7). The Epic Turla Operation: Solving some of the
mysteries of Snake/Uroburos. Retrieved December 11, 2014.
31. Villadsen, O.. (2019, August 29). More\_eggs, Anyone? Threat
Actor ITG08 Strikes Again. Retrieved September 16, 2019.
32. Bennett, J., Vengerik, B. (2017, June 12). Behind the
CARBANAK Backdoor. Retrieved June 11, 2018.
33. Carr, N., et al. (2018, August 01). On the Hunt for FIN7:
Pursuing an Enigmatic and Evasive Global Criminal Operation.
Retrieved August 23, 2018.
34. MSTIC. (2019, December 12). GALLIUM: Targeting global
telecom. Retrieved January 13, 2021.
35. ESET. (2017, August). Gazing at Gazer: Turla’s new second
stage backdoor. Retrieved September 14, 2017.
3. Kaspersky Lab's Global Research & Analysis Team. (2017,
August 30). Introducing WhiteBear. Retrieved September 21,
2017.
37. Cherepanov, A. (2018, October). GREYENERGY A successor to
BlackEnergy. Retrieved November 15, 2018.0. Vilkomir-Preisman, S. (2022, August 18). Beating Black Basta
Ransomware. Retrieved March 8, 2023.
1. Meltzer, M, et al. (2018, June 07). Patchwork APT Group
Targets US Think Tanks. Retrieved July 16, 2018.
2. Faou, M. and Boutin, J. (2017, February). Read The Manual: A
Guide to the RTM Banking Trojan. Retrieved March 9, 2017.
3. CrowdStrike. (2023, January 10). SCATTERED SPIDER
Exploits Windows Security Deﬁciencies with Bring-Your-Own-
Vulnerable-Driver Tactic in Attempt to Bypass Endpoint
Security. Retrieved July 5, 2023.
4. Group-IB. (2019, August). Silence 2.0: Going Global. Retrieved
May 5, 2020.
5. FireEye. (2020, December 13). Highly Evasive Attacker
Leverages SolarWinds Supply Chain to Compromise Multiple
Global Victims With SUNBURST Backdoor. Retrieved January
4, 2021.
. CTU. (2018, September 27). Cybercriminals Increasingly
Trying to Ensnare the Big Financial Fish. Retrieved September
20, 2021.
7. Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February
W32.Stuxnet Dossier (Version 1.4) Retrieved. 2017/09/22
. DiMaggio, J. (2016, March 15). Suckﬂy: Revealing the secret
life of your code signing certiﬁcates. Retrieved August 3, 2016.
9. Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate
Reappears, Adds Linux Targeting. Retrieved March 20, 2023.
70. Salem, E. (2019, April 25). Threat Actor TA505 Targets
Financial Enterprises Using LOLBins and a New Backdoor
Malware. Retrieved May 28, 2019.
71. Vilkomir-Preisman, S. (2019, April 2). New ServHelper Variant
Employs Excel 4.0 Macro to Drop Signed Payload. Retrieved
May 28, 2019.
72. Hiroaki, H. and Lu, L. (2019, June 12). Shifting Tactics:
Breaking Down TA505 Group’s Use of HTML, RATs and Other
Techniques in Latest Campaigns. Retrieved May 29, 2020.
73. Kaspersky Lab's Global Research and Analysis Team. (2013,
April 11). Winnti. More than just a game. Retrieved February 8,
2017.
74. The DFIR Report. (2020, November 5). Ryuk Speed Run, 2
Hours to Ransom. Retrieved November 6, 2020.