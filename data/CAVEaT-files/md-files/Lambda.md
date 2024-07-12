 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 Creating New FaaS - AWS Lambda/Azure 
Logic Apps (version 1.0) 
 
Cloud Service Label: PaaS 
 
Description 
Both Azure and AWS employ “serverless” code functionality that can be set to 
automatically trigger by other events within the cloud API. Such functionality is often not 
associated with an avenue for persistence However, it is fairly straightforward for 
someone with privileges to set up a trigger and a serverless function. In this way an 
adversary with temporary access could set up a function for example to send a copy of 
access keys to an outside controlled web address every time a new user account is 
created. Thus ensuring continued access even after an initial compromise is 
discovered and remediated. Because serverless code is essentially an ephemeral 
PaaS service, traditional methods to scan code for vulnerabilities before execution are 
not very appli cable currently. 
 
Examples 
Name Description 
Aws\_Pwn Publicly available module that allows creation of AWS lambda function 
triggered by user account creation. 
 
Mitigations 
Mitigation Description 
Audit Frequently check permissions on cloud storage to ensure proper 
permissions are set to deny open or unprivileged access to resources. 
Consider using automated resource checkers such as CloudSploit or 
Divvycloud. Frequently check API logs for lambda/function creation events. 
 AWS To perform an audit via AWS it is suggested to review information such as 
account details (credentials, users, groups, roles, etc), mobile applications, 
EC2 configurations, policies, and account activity. How to audit these 
different factors can be found i n detail at: 
https://docs.aws.amazon.com/general/latest/gr/aws -security -audit -
guide.html. 
 Azure To perform an audit via Azure an administrator can review the audit logs 
that are recorded under Azure’s monitoring for active directory. The audit 
logs allow for filtering, as well as looking at users, groups, and enterprise 
specific information. Full det ails on how to access this information can be 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 found at: https://docs.microsoft.com/en -us/azure/active -
directory/reports -monitoring/concept -audit -logs. 
 GCP To perform an audit via GCP the logs can be reviewed. GCP breaks this 
down into three categories; admin activity, data access, and system 
events. The audit logs can be viewed a few different ways - the console, 
API, or gcloud. Full details on how to view th ese logs, how to export, and 
for how to configure the retention period can be found here: 
https://cloud.google.com/logging/docs/audit. 
Policy In Azure apply policy “Diagnostic logs in Logic Apps should be enabled” to 
the scope of all subscriptions to ensure any created logic apps must create 
and deliver logs to a monitoring solution. 
 
Detection 
CloudTrail or Monitor may record accesses to the cloud API when changes are made to 
functions. 
 
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
Microsoft.Network/networkSecurityGroups/securit
yRules/delete 
4. Hover a mouse over Condition to ensure it is set to 
Whenever the Administrative Activity Log “Delete 
Security Rule 
(networkSecurityGroups/securityRules)” has “any” 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
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
1.https://github.com/dagrz/aws\_pwn/blob/master/persistence/backdoor\_created\_users\_l
ambda/backdoor\_created\_users\_lambda.py. Accessed Feb 20, 2020. 
2. https://github.com/puresec/sas -top-10. Accessed Feb 20, 2020. 
 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 
 
 