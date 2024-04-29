3/22/24, 3:49 PM Software Discovery, Technique T1518 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1518/ 1/6Thank you to Tidal Cyber and SOC Prime for becoming ATT&CK's ﬁrst Benefactors. To join the cohort, or learn more about this program visit our
Benefactors page.3/22/24, 3:49 PM Software Discovery, Technique T1518 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1518/ 2/6Home>Techniques>Enterprise>Software Discovery3/22/24, 3:49 PM Software Discovery, Technique T1518 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1518/ 3/6Software Discovery
Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment.
Adversaries may use the information from Software Discovery during automated discovery to shape follow-on behaviors, including whether
or not the adversary fully infects the target and/or attempts speciﬁc actions.
Adversaries may attempt to enumerate software for a variety of reasons, such as ﬁguring out what security measures are present or if the
compromised system has a version of software that is vulnerable to Exploitation for Privilege Escalation.Sub-techniques (1)
Version PermalinkID: T1518
Sub-techniques:  T1518.001

Tactic: Discovery

Platforms: Azure AD, Google Workspace, IaaS, Linux, Oﬃce 365, SaaS, Windows, macOS

Permissions Required: Administrator, User
Version: 1.3
Created: 16 September 2019
Last Modiﬁed: 30 March 20233/22/24, 3:49 PM Software Discovery, Technique T1518 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1518/ 4/6Procedure Examples
ID Name Description
S0534 Bazar Bazar can query the Registry for installed applications.
G0060 BRONZE BUTLER BRONZE BUTLER has used tools to enumerate software installed on an infected host.
S0482 Bundlore Bundlore has the ability to enumerate what browser is being used as well as version information for
Safari.
S0674 CharmPower CharmPower can list the installed applications on a compromised host.
S0154 Cobalt Strike The Cobalt Strike System Proﬁler can discover applications through the browser and identify the
version of Java the target has.
S0126 ComRAT ComRAT can check the victim's default browser to determine which process to inject its
communications module into.
S0472 down\_new down\_new has the ability to gather information on installed applications.
S0384 Dridex Dridex has collected a list of installed software on the system.
S0062 DustySky DustySky lists all installed software for the infected machine.
S0024 Dyre Dyre has the ability to identify installed programs on a compromised host.
G1001 HEXANE HEXANE has enumerated programs installed on an infected machine.
S0431 HotCroissant HotCroissant can retrieve a list of applications from the
SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths registry key.
G0100 Inception Inception has enumerated installed software on compromised systems.
S0260 InvisiMole InvisiMole can collect information about installed software used by speciﬁc users, software executed
on user login, and software executed by each system.
S0526 KGH\_SPY KGH\_SPY can collect information on installed applications.
S0652 MarkiRAT MarkiRAT can check for the Telegram installation directory by enumerating the ﬁles on disk.
S0455 Metamorfo Metamorfo has searched the compromised system for banking applications.
G0069 MuddyWater MuddyWater has used a PowerShell backdoor to check for Skype connectivity on the target machine.
G0129 Mustang Panda Mustang Panda has searched the victim system for the InstallUtil.exe program and its version.
C0016 Operation Dust
StormDuring Operation Dust Storm, the threat actors deployed a ﬁle called DeployJava.js to ﬁngerprint
installed software on a victim system prior to exploit delivery.
C0014 Operation Wocao During Operation Wocao, threat actors collected a list of installed software on the infected system.
S0229 Orz Orz can gather the victim's Internet Explorer version.
S0598 P.A.S. Webshell P.A.S. Webshell can list PHP server conﬁguration details.
S0650 QakBot QakBot can enumerate a list of installed programs.[1]
[2]
[3]
[4]
[5]
[6]
[2]
[7]
[8]
[9]
[10]
[11]
[12]
[13][14]
[15]
[16]
[17][18]
[19]
[20]
[21]
[22]
[23]
[24]
[25]3/22/24, 3:49 PM Software Discovery, Technique T1518 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1518/ 5/6ID Name Description
S0148 RTM RTM can scan victim drives to look for speciﬁc banking software on the machine to determine next
actions.
S0445 ShimRatReporter ShimRatReporter gathered a list of installed software on the infected host.
G1008 SideCopy SideCopy has collected browser information from a compromised host.
G0121 Sidewinder Sidewinder has used tools to enumerate software installed on an infected host.
S0623 Siloscape Siloscape searches for the kubectl binary.
S0646 SpicyOmelette SpicyOmelette can enumerate running software on a targeted system.
S1042 SUGARDUMP SUGARDUMP can identify Chrome, Opera, Edge Chromium, and Firefox browsers, including version
number, on a compromised host.
S1064 SVCReady SVCReady can collect a list of installed software from an infected host.
S0467 TajMahal TajMahal has the ability to identify the Internet Explorer (IE) version on an infected host.
G0081 Tropic Trooper Tropic Trooper's backdoor could list the infected system's installed software.
G1017 Volt Typhoon Volt Typhoon has queried the Registry on compromised systems for information on installed software.
G0124 Windigo Windigo has used a script to detect installed software on targeted systems.
G0112 Windshift Windshift has used malware to identify installed software.
G0102 Wizard Spider Wizard Spider has utilized the PowerShell script Get-DataInfo.ps1 to collect installed backup
software information from a compromised machine.
S1065 Woody RAT Woody RAT can collect .NET, PowerShell, and Python information from an infected host.
S0658 XCSSET XCSSET uses ps aux with the grep command to enumerate common browsers and system
processes potentially impacting XCSSET's exﬁltration capabilities.
Mitigations
This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of system features.
Detection
ID Data SourceData Component Detects
DS0017 Command Command
ExecutionMonitor executed commands and arguments that may attempt to get a listing of software
and software versions that are installed on a system or in a cloud environment.
DS0018 Firewall Firewall
EnumerationMonitor for an extracted list of available ﬁrewalls and/or their associated settings/rules (ex:
Azure Network Firewall CLI Show commands)
Firewall
MetadataMonitor for contextual data about a ﬁrewall and activity around it such as name, policy, or
status
DS0009 Process OS API Execution Monitor for API calls that may attempt to get a listing of software and software versions
that are installed on a system or in a cloud environment.
Process Creation Monitor newly executed processes that may attempt to get a listing of software and
software versions that are installed on a system or in a cloud environment.[26]
[27]
[28]
[29][30]
[31]
[32]
[33]
[34]
[35]
[36]
[37]
[38]
[39]
[40]
[41]
[42]3/22/24, 3:49 PM Software Discovery, Technique T1518 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1518/ 6/6References
1. Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS:
FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved
November 18, 2020.
2. Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s
Multi-Stage Backdoors for Attacking Industries and Stealing
Classiﬁed Data. Retrieved June 9, 2020.
3. Sushko, O. (2019, April 17). macOS Bundlore: Mac Virus
Bypassing macOS Security Features. Retrieved June 30, 2020.
4. Check Point. (2022, January 11). APT35 exploits Log4j
vulnerability to distribute new modular PowerShell toolkit.
Retrieved January 24, 2022.
5. Strategic Cyber LLC. (2020, November 5). Cobalt Strike:
Advanced Threat Tactics for Penetration Testers. Retrieved
April 13, 2021.
. Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-
year journey. Retrieved June 15, 2020.
7. Check Point Research. (2021, January 4). Stopping Serial
Killer: Catching the Next Strike. Retrieved September 7, 2021.
. GReAT. (2019, April 10). Gaza Cybergang Group1, operation
SneakyPastes. Retrieved May 13, 2020.
9. hasherezade. (2015, November 4). A Technical Look At
Dyreza. Retrieved June 15, 2020.
10. Kayal, A. et al. (2021, October). LYCEUM REBORN:
COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved
June 14, 2022.
11. Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat
Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.
12. Symantec. (2018, March 14). Inception Framework: Alive and
Well, and Hiding Behind Proxies. Retrieved May 8, 2020.
13. Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly
equipped spyware, undercover since 2013. Retrieved July 10,
2018.
14. Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE:
THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.
15. Dahan, A. et al. (2020, November 2). Back to the Future: Inside
the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.
1. GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert
Surveillance in Iran. Retrieved September 22, 2021.
17. Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns
Targeting Brazilian Users. Retrieved July 30, 2020.
1. ESET Research. (2019, October 3). Casbaneiro: peculiarities of
this banking Trojan that affects Brazil and Mexico. Retrieved
September 23, 2021.
19. Peretz, A. and Theck, E. (2021, March 5). Earth Vetala –
MuddyWater Continues to Target Organizations in the Middle
East. Retrieved March 18, 2021.
20. Anomali Threat Research. (2019, October 7). China-Based APT
Mustang Panda Targets Minority Groups, Public and Private
Sector Organizations. Retrieved April 12, 2021.
21. Gross, J. (2016, February 23). Operation Dust Storm. Retrieved
December 22, 2021.22. Dantzig, M. v., Schamper, E. (2019, December 19). Operation
Wocao: Shining a light on one of China’s hidden hacking
groups. Retrieved October 8, 2020.
23. Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor
spearphishes maritime and defense targets. Retrieved
February 15, 2018.
24. ANSSI. (2021, January 27). SANDWORM INTRUSION SET
CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved
March 30, 2021.
25. Group IB. (2020, September). LOCK LIKE A PRO. Retrieved
September 27, 2021.
2. Faou, M. and Boutin, J. (2017, February). Read The Manual: A
Guide to the RTM Banking Trojan. Retrieved March 9, 2017.
27. Yonathan Klijnsma. (2016, May 17). Mofang: A politically
motivated information stealing adversary. Retrieved May 12,
2020.
2. Threat Intelligence Team. (2021, December 2). SideCopy APT:
Connecting lures victims, payloads to infrastructure. Retrieved
June 13, 2022.
29. Hegel, T. (2021, January 13). A Global Perspective of the
SideWinder APT. Retrieved January 27, 2021.
30. Rewterz. (2020, April 20). Sidewinder APT Group Campaign
Analysis. Retrieved January 29, 2021.
31. Prizmant, D. (2021, June 7). Siloscape: First Known Malware
Targeting Windows Containers to Compromise Cloud
Environments. Retrieved June 9, 2021.
32. CTU. (2018, September 27). Cybercriminals Increasingly
Trying to Ensnare the Big Financial Fish. Retrieved September
20, 2021.
33. Mandiant Israel Research Team. (2022, August 17). Suspected
Iranian Actor Targeting Israeli Shipping, Healthcare,
Government and Energy Sectors. Retrieved September 21,
2022.
34. Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready.
Retrieved December 13, 2022.
35. GReAT. (2019, April 10). Project TajMahal – a sophisticated
new APT framework. Retrieved October 14, 2019.
3. Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry
Attack Targets Air gapped Environments. Retrieved May 20,
2020.
37. NSA et al. (2023, May 24). People's Republic of China State-
Sponsored Cyber Actor Living off the Land to Evade Detection.
Retrieved July 27, 2023.
3. Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1).
THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH
backdoors. Retrieved July 16, 2020.
39. The BlackBerry Research & Intelligence Team. (2020, October).
BAHAMUT: Hack-for-Hire Masters of Phishing, Fake News, and
Fake Apps. Retrieved February 8, 2021.
40. Shilko, J., et al. (2021, October 7). FIN12: The Proliﬁc
Ransomware Intrusion Threat Actor That Has Aggressively
Pursued Healthcare Targets. Retrieved June 15, 2023.
41. MalwareBytes Threat Intelligence Team. (2022, August 3).
Woody RAT: A new feature-rich malware spotted in the wild.
Retrieved December 6, 2022.
42. Mac Threat Response, Mobile Research Team. (2020, August
13). The XCSSET Malware: Inserts Malicious Code Into Xcode
Projects, Performs UXSS Backdoor Planting in Safari, and
Leverages Two Zero-day Exploits. Retrieved October 5, 2021.