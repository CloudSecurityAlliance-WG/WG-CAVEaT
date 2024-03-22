 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 Managed Identities/Service Principals (version 
1.0) 
 
Cloud Service Label: IaaS, PaaS 
 
Description 
Both Azure and AWS employ authentication/authorization accounts that enable user 
access paradigms to be applied to cloud applications and resources. In Azure these 
“service principals” are called Managed Identities and can be assigned to VM’s and 
other Az ure resources rather than embedding access credentials elsewhere within the 
resource that could be stolen. These service principals can be leveraged by any one 
with local command privileges to access cloud resources that the service principal 
object may ha ve rights to. 
In Azure, Automation accounts are required to automate admin tasks and are 
automatically assigned contributor privileges to the subscription. Contributor access on 
the subscription inherently gives you contributor rights on all of the virtual machines in a 
subscription which in turn grants you SYSTEM on Windows and root on Linux VMs. 
 
Examples 
Name Tactic Description 
NetSPI Defense Evasion Users allowed to create work books 
inside an Azure automation account 
can run code with the permissions 
of the automation account which 
often has contributor rights to the 
subscription. 
NetSPI Escalation NetSPI proof of concept that allows 
any user with access to Azure VM 
to retrieve and use tokens from an 
assigned Service Principal to 
escalate privileges. 
NetSPI Persistence NetSPI proof of concept using 
automation account credentials to 
maintain persistence on running 
VM’s (even if initial credentials are 
replaced/revoked?) 
 
Mitigations 
Mitigation Description 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 Least Privilege All access given to users in the cloud environment should be assigned by the 
necessary privileges needed for team members to complete their job 
responsibilities. Ensure that temporary access tokens are issued rather than 
permanent credentials, especially when access is being granted to entities 
outside of the internal security boundary. 
 AWS To implement least privilege in an AWS environment IAM policies will be used. 
This gives the ability to allow users to perform list, read, write, permissions 
management, or tagging actions. AWS suggests utilizing last accessed 
information and A WS CloudTrail event history to get a better understanding of 
privileges that might be needed or reduced based on a specific role. Full 
details can be found at 
https://docs.aws.amazon.com/IAM/latest/UserGuide/best -
practices.html#grant -least -privilege. 
 Azure To implement least privilege in an Azure environment Azure Active Directory 
roles will be used. Azure outlines different tasks and the least privileged role 
that are suggested to be associated with the task. Those details can be found 
at: https://docs.microsoft.com/en -us/azure/active -directory/users -groups -
roles/roles -delegate -by-task. To learn how to assign specific roles it can be 
done via the Azure Active Directory Portal. Instructions on how to assign roles 
can be found here: https://docs.microsoft.com/ en-us/azure/active -
directory/users -groups -roles/directory -manage -roles -portal. 
 GCP To implement least privilege in GCP it is recommended to use predefined 
roles (which allow for granular access permissions) instead of primitive roles 
(roles/owner, roles/editor, and roles/viewer). Full details on the difference 
between types of roles can be found here: 
https://cloud.google.com/iam/docs/understanding -roles. To assign these 
roles IAM service accounts are used and complete details can be found at: 
https://cloud.google.com/iam/docs/using -iam-securely#least\_privilege. 
 
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
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 1. Navigate to Monitor’ / ‘Alerts 
2. Select Manage alert rules 
3. Click on the Alert Name where Condition contains 
operationName equals 
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
 
References 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 1. https://blog.netspi.com/azure -privilege -escalation -using -managed -identities/ . 
Accessed June 1, 2020 
 