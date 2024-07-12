3/22/24, 3:38 PM Boot or Logon Autostart Execution: Login Items, Sub-technique T1547.015 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1547/015/ 1/4Thank you to Tidal Cyber and SOC Prime for becoming ATT&CK's ﬁrst Benefactors. To join the cohort, or learn more about this program visit our
Benefactors page.3/22/24, 3:38 PM Boot or Logon Autostart Execution: Login Items, Sub-technique T1547.015 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1547/015/ 2/4Home>Techniques>Enterprise>Boot or Logon Autostart Execution>Login Items3/22/24, 3:38 PM Boot or Logon Autostart Execution: Login Items, Sub-technique T1547.015 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1547/015/ 3/4Boot or Logon Autostart Execution: Login Items
Procedure Examples
ID Name Description
S0281 Dok Dok uses AppleScript to install a login Item by sending Apple events to the System Events process.
S0690 Green Lambert Green Lambert can add Login Items to establish persistence.
S0198 NETWIRE NETWIRE can persist via startup options for Login items.
Mitigations
This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of system features.Adversaries may add login items to execute upon user login to gain persistence or escalate privileges. Login items are applications,
documents, folders, or server connections that are automatically launched when a user logs in. Login items can be added via a shared ﬁle
list or Service Management Framework. Shared ﬁle list login items can be set using scripting languages such as AppleScript, whereas the
Service Management Framework uses the API call SMLoginItemSetEnabled .
Login items installed using the Service Management Framework leverage launchd , are not visible in the System Preferences, and can only
be removed by the application that created them. Login items created using a shared ﬁle list are visible in System Preferences, can hide
the application when it launches, and are executed through LaunchServices, not launchd, to open applications, documents, or URLs without
using Finder. Users and applications use login items to conﬁgure their user environment to launch commonly used services or applications,
such as email, chat, and music applications.
Adversaries can utilize AppleScript and Native API calls to create a login item to spawn malicious executables. Prior to version 10.5 on
macOS, adversaries can add login items by using AppleScript to send an Apple events to the "System Events" process, which has an
AppleScript dictionary for manipulating login items. Adversaries can use a command such as tell application "System Events" to
make login item at end with properties /path/to/executable . This command adds the path of the malicious executable to the
login item ﬁle list located in ~/Library/Application Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm .
Adversaries can also use login items to launch executables that can be used to control the victim system remotely or as a means to gain
privilege escalation by prompting for user credentials.Other sub-techniques of Boot or Logon Autostart Execution (14)
[1]
[2]
[2][3]
[4]
[5]
[6]
[7][8][9]
[7]
[10][11][12]
Version PermalinkID: T1547.015
Sub-technique of:  T1547

Tactics: Persistence, Privilege Escalation

Platforms: macOS

Permissions Required: User
Version: 1.0
Created: 05 October 2021
Last Modiﬁed: 18 October 2021
[8]
[13][14]
[15]3/22/24, 3:38 PM Boot or Logon Autostart Execution: Login Items, Sub-technique T1547.015 - Enterprise | MITRE ATT&CK®
https://attack.mitre.org/techniques/T1547/015/ 4/4Detection
ID Data SourceData ComponentDetects
DS0022 File File Creation All login items created via shared ﬁle lists are viewable by using the System Preferences GUI or
in the ~/Library/Application
Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm ﬁle.
These locations should be monitored and audited.
File
ModiﬁcationAll login items created via shared ﬁle lists are viewable by using the System Preferences GUI or
in the ~/Library/Application
Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm ﬁle.
These locations should be monitored and audited.
DS0009 Process Process
CreationMonitor processes that start at login for unusual or unknown applications. Usual applications
for login items could include what users add to conﬁgure their user environment, such as
email, chat, or music applications, or what administrators include for organization settings and
protections. Check for running applications from login items that also have abnormal behavior,
such as establishing network connections.
References[1][7][16][17]
[1][7][16][17]
1. Apple. (n.d.). Open items automatically when you log in on
Mac. Retrieved October 1, 2021.
2. Apple. (2016, September 13). Adding Login Items. Retrieved
July 11, 2017.
3. Tim Schroeder. (2013, April 21). SMLoginItemSetEnabled
Demystiﬁed. Retrieved October 5, 2021.
4. Apple. (n.d.). Launch Services. Retrieved October 5, 2021.
5. hoakley. (2018, May 22). Running at startup: when to use a
Login Item or a LaunchAgent/LaunchDaemon. Retrieved
October 5, 2021.
. Apple. (n.d.). Login Items AE. Retrieved October 4, 2021.
7. hoakley. (2021, September 16). How to run an app or tool at
startup. Retrieved October 5, 2021.
. ﬂuffybunny. (2019, July 9). OSX.Dok Analysis. Retrieved
October 4, 2021.
9. kaloprominat. (2013, July 30). macos: manage add list
remove login items apple script. Retrieved October 5, 2021.10. Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved
September 21, 2018.
11. Ofer Caspi. (2017, May 4). OSX Malware is Catching Up, and it
wants to Read Your HTTPS Traﬃc. Retrieved October 5, 2021.
12. Patrick Wardle. (2019, June 20). Burned by Fire(fox). Retrieved
October 1, 2021.
13. Sandvik, Runa. (2021, October 1). Made In America: Green
Lambert for OS X. Retrieved March 21, 2022.
14. Sandvik, Runa. (2021, October 18). Green Lambert and
ATT&CK. Retrieved March 21, 2022.
15. Lambert, T. (2020, January 29). Intro to Netwire. Retrieved
January 7, 2021.
1. Patrick Wardle. (2018, July 23). Block Blocking Login Items.
Retrieved October 1, 2021.
17. Stokes, Phil. (2019, June 17). HOW MALWARE PERSISTS ON
MACOS. Retrieved September 10, 2019.