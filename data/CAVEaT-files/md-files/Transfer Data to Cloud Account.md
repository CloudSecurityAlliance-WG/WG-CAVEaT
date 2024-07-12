 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 Transfer Data to Cloud Account in Same 
CSP (version 1.0) 
 
Cloud Service Label: IaaS, PaaS 
 
Description 
An adversary may exfiltrate data by transferring the data, including backups or 
snapshots of cloud environments, to another cloud account they control on the same 
service to avoid typical file transfers/downloads and network -based exfiltration 
detection. 
A defender who is monitoring for large transfers external to the cloud environment 
through normal file transfers or over command and control channels may not be 
watching for data transfers to another account within the same cloud provider or even to 
anothe r VPC illicitly created within the same account. Such transfers may utilize existing 
cloud provider APIs and the internal address space of the cloud provider to blend into 
normal traffic or avoid data transfers over external network interfaces. 
Incidents have been observed where adversaries have created backups of cloud 
instances and transferred them to separate accounts. 
 
Examples 
Name Description 
Justice Department Indictment This indictment outlines how adversaries created 
backups of a cloud -based system utilizing the cloud 
providers technology. Adversaries then used their own 
accounts on the same cloud service to move the 
backups to. This lead to them effectively stealing the 
data. 
 
Mitigations 
Mitigation Description 
Filter Network Traffic Cloud service providers support IP -based restrictions when accessing 
cloud resources. Consider using IP whitelisting along with user account 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 management to ensure that data access is restricted not only to valid 
users, but only from expected IP ranges to mitigate the use of stolen 
credentials to access data. 
 AWS An AWS environment can be configured with network ACLs (access 
control lists) to allow or deny inbound and outbound traffic. This can be 
accomplished by accessing Amazon VPC and navigating to either 
inbound or outbound rules depending on the rule the user wishes to add 
and they can be added, removed, or edited from that panel. Full details 
about ACLs and how to add rules in AWS can be found here: 
https://docs.aws.amazon.com/vpc/latest/userguide/vpc -network -
acls.html. 
 Azure In Azure storage resources can be tied exclusively to a particular virtual 
network reducing the chances that it can be accessed externally or from 
other cloud assets. This can be done multiple ways including the Azure 
Portal, Azure PowerShell, and Azure CL I (Command Line Interface). 
Depending on the method used to implement this the procedure can vary, 
but will include the need to create a security group, create a network 
security group, associate that network security group with a specific 
subnet and then create security rules that are associated to the inbound 
and outbound rules for that subnet. Full details on how to configure this 
utilizing the various methods can be found below: 
Azure Portal: https://docs.microsoft.com/en -us/azure/virtual -
network/tutorial -filter -network -traffic 
Azure PowerShell: https://docs.microsoft.com/en -us/azure/virtual -
network/tutorial -filter -network -traffic -powershell 
Azure CLI: https://docs.microsoft.com/en -us/azure/virtual -
network/tutorial -filter -network -traffic -cli 
Password Policies Consider rotating access keys within a certain number of days to reduce 
the effectiveness of stolen credentials. 
 AWS Good password practices can be enforced in AWS via the console, AWS 
CLI, and AWS API. These configurations are for IAM accounts only and 
have a range of different characteristics that can be enforced. For 
instance minimum password length, require a range o f characters 
(lowercase, uppercase, number, and non alphanumeric ), allow users to 
change their own password, password expiration, prevent password 
reuse, and require administrator reset after password expiration. All 
details on how to configure these enfo rcement policies with all three 
management systems can be found here: 
https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_credentials\_p
asswords\_account -policy.html. 
 Azure Good password practices can be enforced in Azure only with managed 
domains created using the resource manager deployment. By default 
these accounts have some policies enforced including amount of lockout 
duration, allowed number of logon attempts, Reset failed logon attempts 
count after 30 minutes, and lifetime of password. Other policies that can 
be changed are minimum password length and the ability to enforce the 
concept of ‘passwords must meet complexity requirements’. These 
configurations can b e accomp lished by accessing the Active Directory 
Administrative Center under administrative tools, then editing the rules 
under the settings for the Password Settings Container. Full details on 
how to accomplish this can be found here: 
https://docs.microsoft.com/en -us/azure/active -directory -domain -
services/password -policy. 
Least Privilege All access given to users in the cloud environment should be assigned by 
the necessary privileges needed for team members to complete their job 
responsibilities. Ensure that temporary access tokens are issued rather 
than permanent credentials, especially when access is being granted to 
entities outside of the internal security boundary. 
 AWS To implement least privilege in an AWS environment IAM policies will be 
used. This gives the ability to allow users to perform list, read, write, 
permissions management, or tagging actions. AWS suggests utilizing last 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 accessed information and A WS CloudTrail event history to get a better 
understanding of privileges that might be needed or reduced based on a 
specific role. Full details can be found at 
https://docs.aws.amazon.com/IAM/latest/UserGuide/best -
practices.html#grant -least -privilege. 
 Azure To implement least privilege in an Azure environment Azure Active 
Directory roles will be used. Azure outlines different tasks and the least 
privileged role that are suggested to be associated with the task. Those 
details can be found at: https://docs.microsoft.com/en -us/azure/active -
directory/users -groups -roles/roles -delegate -by-task. To learn how to 
assign specific roles it can be done via the Azure Active Directory Portal. 
Instructions on how to assign roles can be found here: 
https://docs.microsoft.com/ en-us/azure/active -directory/users -
groups -roles/directory -manage -roles -portal. 
 GCP To implement least privilege in GCP it is recommended to use predefined 
roles (which allow for granular access permissions) instead of primitive 
roles (roles/owner, roles/editor, and roles/viewer). Full details on the 
difference between types of roles can be found here: 
https://cloud.google.com/iam/docs/understanding -roles. To assign 
these roles IAM service accounts are used and complete details can be 
found at: https://cloud.google.com/iam/docs/using -iam-
securely#least\_privilege. 
 
Detection 
Detection Description 
Create Log Metric Filters and Alarms for AWS To create a metric filter and alarm: 
1. Create a metric filter that checks for IAM policy 
changes and the  
2. Create an SNS topic 
3. Create an SNS subscription to the above topic 
4. Create an alarm associated with the filter and SNS 
topic created in steps 1 and 2 respectively 
Monitor Activity in AWS Account Various services in AWS offer logging features that allow for 
detection capabilities. These include CloudFront, CloudTrail, 
CloudWatch, Config, and S3. 
Monitor for Suspicious Activity in Azure Azure AD can generate anomaly reports than can be run on 
a daily basis. Azure AD Identity Protection show current risks 
in its dashboard and provides daily email summary 
notifications. Policies can also be configured to alert to 
specific issues. 
Create Log Metric Filters and Alarms for CloudTrail To create a metric filter and alarm: 
1. Create a filter that checks for CloudTrail changes 
and the specific  
2. Create an SNS topic that the alarm will notify 
3. Create an SNS subscription to the above topic 
4. Create an alarm associated with the filter from 
step 1 and SNS topic in step 2 
Create Activity Log Alerts in Azure To create log activity alerts for deletion in the Azure 
Console: 
1. Navigate to Monitor’ / ‘Alerts 
2. Select Manage alert rules 
3. Click on the Alert Name where Condition contains 
operationName equals 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 Microsoft.Network/networkSecurityGroups/securit
yRules/delete 
4. Hover a mouse over Condition to ensure it is set to 
Whenever the Administrative Activity Log “Delete 
Security Rule 
(networkSecurityGroups/securityRules)” has “any” 
level with “any” status and event is initiated by 
“any” 
Create, View, and Manage Activity Alerts in Azure Monitor To create a log alert in the Azure portal: 
1. Select Monitor -> Alerts 
2. Select New alert rule of the Alerts window 
3. Provide information in Define alert condition 
4. Provide details in Define alert details 
5. Specify action group for new alert rule under 
Action group , or create a new action group with + 
New group 
6. Select Yes for the Enable rule upon creation 
option 
7. Select Create alert rule 
 
To view and manage alerts: 
1. Select Monitor -> Alerts -> Manage alert rules 
2. Select the rule you want to modify and double -
click to edit the rule options 
3. Click Save 
Azure Resource Manager Templates Azure Resource Manager templates in the format of JSON 
files that can be used to configure metric alerts in Azure 
Monitor. These templates can be used for simple static and 
dynamic threshold metric alerts, availability tests, and 
monitoring multiple resour ces. 
Enable CloudTrail across all regions in AWS To enable CloudTrail across all regions: 
1. Sign into the AWS Management Console and open 
the CloudTrail console 
2. Click on Trails 
3. Set necessary Trails to All option in the I column 
4. Click on a trail via the link Name column 
5. Set Logging to ON 
6. Set Apply trail to all regions to Yes 
Configure log profile to capture activity logs for all regions in 
Azure To set up activity logs for all regions: 
1. Navigate to Azure console 
2. Go to Activity log 
3. Select Export 
4. Select Subscription 
5. Check Select all in Regions 
6. Select Save 
 
 
 
 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 References 
1. https://www.justice.gov/file/1080281/download. Accessed July 3, 2020. 