 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content Submission 
for Consideration by the CAVEAT Working Group) 
 Abuse Queue Services (version 1.0) 
Cloud Service Label: PaaS 
 
Description 
Both AWS and Azure have “serverless” queuing services that enable developers to 
decouple code elements while enabling a robust and understandable means of passing 
messages between them. The assumption, however, is that messages in the queue 
can be trusted because queues can normally only be accessed by trusted internal apps. 
The Nimbostratus open source tool set has introduced a module that makes it easy to 
inject malicious commands within an AWS SQS queue if an adversary can gain access 
to a process that can access the queue. Depending what other hosts are reading from 
the queue, an adversary could spread laterally or increase his privileges. 
 
Examples 
Name Description 
Celery\_pickle 
 Nimbostratus module demonstrating abuse of SQS 
service. 
 
 
Mitigations 
Mitigation Description 
Coding Practices Check queue input before consuming. Do not trust 
messages coming from queues not to contain 
potentially malicious commands. 
 
 
Detection 
Although it may be possible to log all inputs that enter a queue, the amount of data to 
store and examine make this a potentially impractical solution currently. 
 
Detection of unusual activity after exploit Description 
Create Log Metric Filters and Alarms for AWS To create a metric filter and alarm: 
1. Create a metric filter that checks for IAM policy 
changes and the  
2. Create an SNS topic 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content Submission 
for Consideration by the CAVEAT Working Group) 
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
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content Submission 
for Consideration by the CAVEAT Working Group) 
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
1. http://andresriancho.github.io/nimbostratus/. Accessed Feb 23, 2020 
 
 