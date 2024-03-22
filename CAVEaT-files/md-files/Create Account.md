 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 Create New Account (version 1.0) 
 
Cloud Service Label: IaaS, PaaS 
 
Description 
Adversaries with a sufficient level of access may create a local system, domain, or 
cloud tenant account. Such accounts may be used for persistence that do not require 
persistent remote access tools to be deployed on the system. 
In cloud environments, adversaries may create accounts that only have access to 
specific services, which can reduce the chance of detection. In Azure these are called 
Service Principal accounts. 
 
Examples 
Name Description 
Nimbostratus AWS open source tool that quickly creates surreptitious accounts to 
maintain access once initial access has been obtained. 
 
Mitigations 
Mitigation Description 
Multi -factor Authentication 
 
 Use multi -factor authentication for user and privileged accounts. Do not 
manage Cloud portals from machines that perform user email and web 
browsing tasks. All users should be required to utilize two factor 
authentication. 
 AWS This can be enforced by first creating a policy that would prohibit actions 
except those that allow a user to change their password or manage 2FA, 
then attaching a policy to a group that includes all user accounts where 
they can be allowed all access if th ey sign in with 2FA. Once these actions 
are completed it should be tested to verify the access is given correctly. To 
see full details on how to complete this view AWS documentation at: 
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users -
self-manage -mfa-and-creds.html. 
 Azure This can be done by creating a MFA registration policy. It can than be 
assigned to all users (with the ability to exclude some if need be, but is not 
recommended). Make sure once the policy is created and added to users 
that it is then being enforced, once enforced it should be tested for 
verification. To see full details on how to complete this view Azure 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 documentation at: https://docs.microsoft.com/en -us/azure/active -
directory/identity -protection/howto -identity -protection -configure -mfa-
policy. 
 GCP This can be done by first enabling it on the current account being used by 
admin to assign the roles, then enable two factor on an instance by 
instance or project by project basis, then assigning the requirements based 
on IAM roles and applying it to all u sers. To see full details on how to 
complete this view Azure documentation at: 
https://cloud.google.com/compute/docs/oslogin/setup -two-factor -
authentication. 
Account Segmentation Consider separating different resources under different administrative 
domains so that credential compromise does not put all assets in danger. 
In the case of Azure, multiple subscriptions can be created with different 
administrators that can only access resources within the subscription. The 
subscriptions can still belong under the same Azure account for overall 
accounting and administration/policy. 
AD Server Configuration 
 Use Cloud provided AD services rather than maintaining AD servers in the 
cloud. These tend to be more integrated into Cloud logs and protections 
Privileged Account Management 
 Do not allow subscription owner accounts to be used for day -to-day 
operations that may expose them to potential adversaries on unprivileged 
systems. 
 AWS To manage the access that privileged accounts have on the AWS cloud 
system to only allow administrators to perform administrative tasks on such 
accounts can be accomplished utilizing limited IAM administrator accounts. 
To configure this the administrator w ould have two accounts; one would 
have administrative rights and no basic access while the other account has 
basic access with no administrative rights. To limit the administrative 
account the IAM limited administrator would be used. This is done by 
creati ng a policy that gives a user admin rights, but disallows the other 
actions using the AWS command line interface. This is outlined at: 
https://aws.amazon.com/blogs/security/how -to-create -a-limited -iam-
administrator -by-using -managed -policies/ . 
 Azure To manage the access that privilege accounts have on the Azure cloud 
system to only allow administrators to perform administrative tasks on such 
accounts can be accomplished utilizing limited IAM administrator accounts. 
To configure this the administrator would have two accounts; one would 
have administrative rights and no basic access while the other account has 
basic access with no administrative rights. To limit the administrative 
account the specific administrative needs can be picked from a number of 
options available (Azure DevOps Administrator, Billing Administrator, Cloud 
Application Administrator, etc.) These different options can be edited to fit 
the needs and limit the basic access. This is outlined at: 
https://docs.microsoft.com/en -us/azure/active -directory/users -
groups -roles/directory -assign -admin -roles . 
 GCP To manage the access that privilege accounts have on the Azure cloud 
system to only allow administrators to perform administrative tasks on such 
accounts can be accomplished utilizing limited IAM administrator accounts. 
To configure this the administrator would have two accounts; one would 
have administrative rights and no basic access while the other account has 
basic access with no administrative rights. To limit the administrative 
account pre -defined administrator accounts can be used (mobile admin, 
Goog le voice admin, help desk admin, etc.). These accounts can be used 
with their pre -defined settings, or modified depending on specific use 
cases. These can limit access to basic functionality needed. This is 
outlined at: https://support.google.com/a/answer/2405986?hl=en. 
 
 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 Detection 
Collect usage logs from cloud administrator accounts to identify unusual activity in the 
creation of new accounts and assignment of roles to those accounts. Monitor for 
accounts assigned to admin roles that go over a certain threshold of known admins. 
 
Detection Description 
Create Log Metric Filters and Alarms for AWS To create a metric filter and alarm: 
1. Create a metric filter that checks for IAM policy 
changes and the 
 
2. Create an SNS topic 
3. Create an SNS subscription to the above topic 
4. Create an alarm associated with the filter and 
SNS topic created in steps 1 and 2 
respectively 
Monitor Activity in AWS Account Various services in AWS offer logging features that 
allow for detection capabilities. These include 
CloudFront, CloudTrail, CloudWatch, Config, and S3. 
Monitor for Suspicious Activity in Azure Azure AD can generate anomaly reports than can be 
run on a daily basis. Azure AD Identity Protection show 
current risks in its dashboard and provides daily email 
summary notifications. Policies can also be configured 
to alert to specific issues. 
Create Log Metric Filters and Alarms for CloudTrail To create a metric filter and alarm: 
1. Create a filter that checks for CloudTrail 
changes and the specific 
 
2. Create an SNS topic that the alarm will notify 
3. Create an SNS subscription to the above topic 
4. Create an alarm associated with the filter from 
step 1 and SNS topic in step 2 
Create Activity Log Alerts in Azure To create log activity alerts for deletion in the Azure 
Console: 
1. Navigate to Monitor’ / ‘Alerts 
2. Select Manage alert rules 
3. Click on the Alert Name where Condition 
contains operationName equals 
Microsoft.Network/networkSecurityGroups/sec
urityRules/delete 
4. Hover a mouse over Condition to ensure it is 
set to Whenever the Administrative Activity 
Log “Delete Security Rule 
(networkSecurityGroups/securityRules)” has 
“any” level with “any” status and event is 
initiated by “any ” 
Create, View, and Manage Activity Alerts in Azure 
Monitor To create a log alert in the Azure portal: 
1. Select Monitor -> Alerts 
2. Select New alert rule of the Alerts window 
3. Provide information in Define alert condition 
4. Provide details in Define alert details 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 5. Specify action group for new alert rule under 
Action group , or create a new action group 
with + New group 
6. Select Yes for the Enable rule upon creation 
option 
7. Select Create alert rule 
 
To view and manage alerts: 
1. Select Monitor -> Alerts -> Manage alert 
rules 
2. Select the rule you want to modify and double -
click to edit the rule options 
3. Click Save 
Azure Resource Manager Templates Azure Resource Manager templates in the format of 
JSON files that can be used to configure metric alerts in 
Azure Monitor. These templates can be used for simple 
static and dynamic threshold metric alerts, availability 
tests, and monitoring multiple resour ces. 
Enable CloudTrail across all regions in AWS To enable CloudTrail across all regions: 
1. Sign into the AWS Management Console and 
open the CloudTrail console 
2. Click on Trails 
3. Set necessary Trails to All option in the I 
column 
4. Click on a trail via the link Name column 
5. Set Logging to ON 
6. Set Apply trail to all regions to Yes 
Configure log profile to capture activity logs for all 
regions in Azure To set up activity logs for all regions: 
1. Navigate to Azure console 
2. Go to Activity log 
3. Select Export 
4. Select Subscription 
5. Check Select all in Regions 
6. Select Save 
 
References 
1. https://andresriancho.github.io/nimbostratus/. Accessed July 1, 2020. 
 
 