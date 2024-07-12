 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 Disable or Modify Security Tools (version 1.0) 
 
Cloud Service Label: IaaS, PaaS 
 
Description 
Adversaries may disable security tools to avoid possible detection of their tools and 
activities. This can take the form of killing security software or event logging processes, 
deleting Registry keys so that tools do not start at run time, or other method s to interfere 
with security tools scanning or reporting information. 
 
Cloud Workload Protection Platforms (CWPPs) are cloud security solutions that reduce 
the impact of malware intrusion in public cloud infrastructure. Companies like Trend 
Micro, Symantec, and Microsoft have their own cloud security products (Trend Micro 
Deep Security, Symantec Cloud Workload Protection, and Azure Security Center 
respectively). 
 
Examples 
Name  Description   
Rocke Group Malware Rocke Group Malware uninstalled cloud security products from vendors Alibaba 
Cloud and Tencent Cloud. It would begin the process by killing the monitoring and 
other agent -based processes, then utilizing public documentation and wget to pull 
down and run uninstall scripts for the cloud security products. 
 
 
 
 
Mitigations 
Mitigation Description   
Restrict File and Directory 
Permissions Users should have limited access to files and directories depending on their need 
for access. The file and directory permissions should be restricted on the basis of 
least privilege. Ensure proper process and file permissions are in place to 
prevent adversaries from disabling or interfering with security/logging services. 
 AWS To manage the files and directory permissions in AWS, IAM policies can be 
used. This can be done by utilizing group policies and policy variables. The 
policy would be created specifying the folder, then the permissions attached to 
that folder (whether the user has access to list out the objects within the 
directory, if they have read permissions, if they have write permissions, etc.), 
lastly the group that it applies to would be specified. The users can that be added 
and removed from that group as needed. F ull details on how this can be done is 
explained here: https://aws.amazon.com/blogs/security/writing -iam-policies -
grant -access -to-user -specific -folders -in-an-amazon -s3-bucket/. 
 Azure To manage the files and directory permissions in an Azure environment basic 
and advanced system defined controls. This will be dependent on the type of 
system being used (Windows, Linux, etc). The permissions will be set individually 
or by group using the system commands or controls needed.. Full details on how 
this can be done is explained here: https://docs.microsoft.com/en -
us/azure/storage/files/storage -files-identity -ad-ds-configure -permissions. 
Least Privilege All access given to users in the cloud environment should be assigned by the 
necessary privileges needed for team members to complete their job 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 responsibilities. Ensure that temporary access tokens are issued rather than 
permanent credentials, especially when access is being granted to entities 
outside of the internal security boundary . Ensure proper user permissions are in 
place to prevent adversaries from disabling or interfering with security/logging 
services. 
 
 AWS To implement least privilege in an AWS environment IAM policies will be used. 
This gives the ability to allow users to perform list, read, write, permissions 
management, or tagging actions. AWS suggests utilizing last accessed 
information and A WS CloudTrail event history to get a better understanding of 
privileges that might be needed or reduced based on a specific role. Full details 
can be found at https://docs.aws.amazon.com/IAM/latest/UserGuide/best -
practices.html#grant -least -privilege. 
 Azure To implement least privilege in an Azure environment Azure Active Directory 
roles will be used. Azure outlines different tasks and the least privileged role that 
are suggested to be associated with the task. Those details can be found at: 
https://docs.microsoft.com/en -us/azure/active -directory/users -groups -
roles/roles -delegate -by-task. To learn how to assign specific roles it can be 
done via the Azure Active Directory Portal. Instructions on how to assign roles 
can be found here: https://docs.microsoft.com/ en-us/azure/active -
directory/users -groups -roles/directory -manage -roles -portal. 
 GCP To implement least privilege in GCP it is recommended to use predefined roles 
(which allow for granular access permissions) instead of primitive roles 
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
 
 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 References 
1. https://unit42.paloaltonetworks.com/malware -used -by-rocke -group -evolves -to-
evade -detection -by-cloud -security -products/ . Accessed July 14, 2020. 
 
 