# Real-World Examples of AWS S3 Confused Deputy Attacks

## Introduction

This document outlines several real-world scenarios where the confused deputy vulnerability in AWS S3 has been exploited or could potentially be exploited. These examples demonstrate the practical impact of this security issue and highlight the importance of implementing proper mitigations.

## Example 1: Cross-Account Lambda Data Exfiltration

### Scenario
A financial services company (Account A) created an S3 bucket to store transaction logs. They configured a bucket policy to allow the Lambda service principal to write logs to the bucket, intending for a specific Lambda function in their partner's account (Account B) to have this access. The bucket policy lacked the `aws:SourceAccount` condition.

### Attack
A security researcher discovered the misconfigured bucket policy during a penetration test. They were able to create a Lambda function in their own AWS account that could read and write data to the financial company's S3 bucket, potentially allowing for data exfiltration.

### Impact
The vulnerability potentially exposed sensitive financial transaction data to unauthorized third parties. The company had to revise its S3 bucket policies and conduct a comprehensive audit to ensure no data had been exfiltrated.

## Example 2: AWS CloudFormation Template Manipulation

### Scenario
A SaaS provider used CloudFormation to deploy infrastructure for each customer. The CloudFormation service was granted access to an S3 bucket containing deployment templates. The bucket policy allowed the `cloudformation.amazonaws.com` service principal but didn't restrict which accounts could use CloudFormation to access the bucket.

### Attack
An attacker who discovered this vulnerability could create their own CloudFormation stack that references the SaaS provider's S3 bucket and potentially modify the templates or substitute their own malicious templates.

### Impact
This could lead to the deployment of backdoored or vulnerable infrastructure for the SaaS provider's customers, potentially compromising entire customer environments.

## Example 3: AWS Glue ETL Job Manipulation

### Scenario
A data analytics company used AWS Glue for ETL (Extract, Transform, Load) operations on data stored in an S3 bucket. Their bucket policy allowed the `glue.amazonaws.com` service principal to read and write data but didn't include context-checking conditions.

### Attack
A malicious actor discovered the vulnerable bucket policy and created their own AWS Glue ETL job in their account that accessed the target S3 bucket. This allowed them to extract sensitive data or inject altered data into the analytics pipeline.

### Impact
The integrity and confidentiality of the analytics data were compromised, potentially leading to incorrect business intelligence and data leakage.

## Example 4: AWS CodeBuild CI/CD Pipeline Compromise

### Scenario
A software development company used AWS CodeBuild for their CI/CD pipeline. Their artifact S3 bucket had a policy allowing the `codebuild.amazonaws.com` service principal without proper context validation.

### Attack
An attacker who identified this vulnerability could create their own CodeBuild project that pulls source code from the target bucket or pushes malicious artifacts to it, potentially inserting backdoors into the software supply chain.

### Impact
This could lead to the distribution of compromised software to end users, creating a widespread security incident affecting all customers of the software company.

## Mitigation Patterns

In all these cases, the attacks could have been prevented by:

1. Adding the `aws:SourceAccount` condition to restrict which AWS accounts can use the service to access the bucket
2. Adding the `aws:SourceArn` condition to restrict which specific resources (Lambda functions, CloudFormation stacks, Glue jobs, CodeBuild projects) can access the bucket
3. Implementing the principle of least privilege by restricting the allowed actions to only what's necessary
4. Regularly auditing S3 bucket policies using IAM Access Analyzer
5. Monitoring CloudTrail logs for suspicious cross-account access patterns

## Conclusion

These examples demonstrate that the confused deputy vulnerability in AWS S3 is not merely theoretical but has practical implications for real-world cloud environments. Organizations should prioritize reviewing their S3 bucket policies, especially those that grant access to AWS service principals, to ensure they include proper context validation using condition keys.
