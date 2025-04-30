# CAVEaT STIX Generator - AWS Courses of Action Module

Version: 2025-04-29
Author: Kurt Seifried, kseifried@cloudsecurityalliance.org

## Purpose

This module provides detailed AWS-specific guidance for implementing mitigations and courses of action for cloud security vulnerabilities. It includes standardized formats for AWS Management Console, CLI, API, and CloudFormation implementations.

## AWS Implementation Standards

When documenting AWS mitigations, follow these standards to ensure consistency and completeness:

### AWS Service Coverage

For each mitigation, identify which AWS services are involved, including:
- Primary service (e.g., S3, EC2, IAM)
- Supporting services (e.g., CloudTrail, CloudWatch, Config)
- Integration points with other services
- Dependencies and prerequisites

### AWS Management Console Instructions

When documenting console-based remediation steps:

1. **Navigation Path**:
   - Start with the service landing page
   - List each navigation step with exact menu names
   - Use ">" to separate navigation steps
   - Example: "AWS Management Console > Services > S3 > [bucket-name]"

2. **UI Element Reference**:
   - Reference UI elements by their exact names
   - Specify tabs, buttons, toggles, and form fields
   - Note context menus or dropdown options
   - Include screenshots if possible (or describe what to look for)

3. **Format Template**:
   ```
   1. Sign in to the AWS Management Console
   2. Navigate to [Service] > [SubMenu] > [SubMenu]
   3. Select [Resource Name or Type]
   4. Click the [Tab/Button/Link Name]
   5. Configure [Setting Name] to [Value]
   6. Click [Save/Apply/Update]
   ```

### AWS CLI Implementation

When documenting AWS CLI commands:

1. **Command Structure**:
   - Provide the complete CLI command with all required parameters
   - Include options with descriptions
   - Show example values for variables
   - Include both the command and its expected output

2. **Prerequisites**:
   - Specify required AWS CLI version
   - Note any required profiles or configurations
   - Include any necessary permissions or roles

3. **Format Template**:
   ```bash
   # Install or update AWS CLI (if needed)
   pip install awscli --upgrade

   # Configure AWS CLI (if needed)
   aws configure

   # Main remediation command
   aws [service] [command] \
     --parameter1 value1 \
     --parameter2 value2 \
     --parameter3 value3

   # Verification command
   aws [service] [verification-command] \
     --resource-id [id]
   ```

### AWS API/SDK Implementation

When documenting AWS API calls:

1. **Multiple Language Support**:
   - Provide examples in at least Python and JavaScript/Node.js
   - Use standard AWS SDK libraries
   - Include import/require statements
   - Show error handling

2. **Code Structure**:
   - Include complete, runnable code samples
   - Document all parameters
   - Show authentication setup
   - Include comments explaining key steps

3. **Format Template (Python Example)**:
   ```python
   # Install dependencies (if needed)
   # pip install boto3

   import boto3
   import json

   # Initialize client
   client = boto3.client('[service]')

   # Main remediation function
   def apply_mitigation(resource_id, parameter1, parameter2):
       response = client.[method_name](
           ResourceId=resource_id,
           Parameter1=parameter1,
           Parameter2=parameter2
       )
       return response

   # Verification function
   def verify_mitigation(resource_id):
       response = client.[verification_method](
           ResourceId=resource_id
       )
       return response['SecurityStatus']

   # Example usage
   if __name__ == "__main__":
       result = apply_mitigation('resource-123', 'value1', 'value2')
       print(json.dumps(result, indent=4))
       
       status = verify_mitigation('resource-123')
       print(f"Verification Status: {status}")
   ```

### AWS CloudFormation Templates

When documenting Infrastructure as Code solutions:

1. **Template Structure**:
   - Provide complete, validated CloudFormation templates
   - Include all required resources and properties
   - Add comments explaining security-relevant settings
   - Include parameters for customization

2. **Secure Defaults**:
   - Ensure templates have secure default values
   - Document security-focused parameters
   - Include constraints and validations
   - Note any required IAM permissions

3. **Format Template**:
   ```yaml
   AWSTemplateFormatVersion: '2010-09-09'
   Description: 'Secure configuration for [Service] to mitigate [Vulnerability]'
   
   Parameters:
     # Define customizable parameters here
     EnvironmentType:
       Description: Environment type
       Type: String
       Default: Production
       AllowedValues:
         - Development
         - Test
         - Production
   
   Resources:
     # Define secure resources here
     SecureResource:
       Type: 'AWS::Service::ResourceType'
       Properties:
         SecurityProperty1: true
         SecurityProperty2: 'secure-value'
         # Additional properties with comments explaining security significance
   
   Outputs:
     # Define outputs to verify secure configuration
     SecurityStatus:
       Description: Security status of the deployed resources
       Value: !GetAtt SecureResource.SecurityStatus
   ```

## AWS Verification Techniques

For each AWS mitigation, include specific verification methods:

### Console Verification
- Specific console pages to check
- Visual indicators of secure configuration
- Dashboard views or status indicators
- Example: "Verify the bucket policy shows 'Public access: Blocked' in the bucket overview"

### CLI Verification Commands
```bash
# Example S3 bucket policy verification
aws s3api get-bucket-policy-status --bucket my-bucket

# Example security group verification
aws ec2 describe-security-groups --group-ids sg-123456 --query 'SecurityGroups[0].IpPermissions'

# Example IAM policy verification
aws iam get-policy-version --policy-arn arn:aws:iam::123456789012:policy/MyPolicy --version-id v1
```

### Automated Verification
- AWS Config rules to detect compliant/non-compliant resources
- CloudWatch alarms to monitor security settings
- AWS Security Hub checks
- Example: "Create an AWS Config rule to verify S3 bucket encryption"

## AWS-Specific Security Services

When appropriate, include guidance on leveraging these AWS security services:

1. **AWS Security Hub**:
   - Enable relevant security standards
   - Configure specific controls
   - Set up findings aggregation

2. **AWS Config**:
   - Deploy managed rules for continuous compliance
   - Create custom rules for specific checks
   - Implement automatic remediation

3. **Amazon GuardDuty**:
   - Enable threat detection
   - Configure findings notifications
   - Implement automatic response

4. **AWS Identity and Access Management (IAM)**:
   - Implement least privilege policies
   - Enable permissions boundaries
   - Configure service control policies

5. **AWS CloudTrail**:
   - Enable logging for relevant services
   - Configure multi-region trails
   - Implement log validation

## AWS Service-Specific Templates

### S3 Security Template

For S3-related vulnerabilities, include:

1. **Bucket Policy Implementation**:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "DenyPublicReadAccess",
         "Effect": "Deny",
         "Principal": "*",
         "Action": ["s3:GetObject"],
         "Resource": ["arn:aws:s3:::example-bucket/*"],
         "Condition": {
           "StringNotEquals": {
             "aws:PrincipalOrgID": "o-exampleorgid"
           }
         }
       }
     ]
   }
   ```

2. **S3 Block Public Access**:
   ```bash
   # CLI command
   aws s3api put-public-access-block \
     --bucket example-bucket \
     --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
   ```

3. **Bucket Encryption Implementation**:
   ```bash
   # CLI command
   aws s3api put-bucket-encryption \
     --bucket example-bucket \
     --server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}'
   ```

### IAM Security Template

For IAM-related vulnerabilities, include:

1. **Secure IAM Policy**:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "LeastPrivilegeAccess",
         "Effect": "Allow",
         "Action": [
           "s3:GetObject",
           "s3:ListBucket"
         ],
         "Resource": [
           "arn:aws:s3:::example-bucket",
           "arn:aws:s3:::example-bucket/*"
         ],
         "Condition": {
           "Bool": {"aws:SecureTransport": "true"}
         }
       }
     ]
   }
   ```

2. **IAM Password Policy**:
   ```bash
   # CLI command
   aws iam update-account-password-policy \
     --minimum-password-length 14 \
     --require-symbols \
     --require-numbers \
     --require-uppercase-characters \
     --require-lowercase-characters \
     --max-password-age 90 \
     --password-reuse-prevention 24
   ```

3. **IAM Access Analyzer Implementation**:
   ```bash
   # CLI command
   aws accessanalyzer create-analyzer \
     --analyzer-name "OrganizationAnalyzer" \
     --type "ORGANIZATION"
   ```

### EC2 Security Template

For EC2-related vulnerabilities, include:

1. **Security Group Rules**:
   ```bash
   # CLI command to create a secure security group
   aws ec2 create-security-group \
     --group-name "SecureWebServerSG" \
     --description "Secure web server security group" \
     --vpc-id "vpc-12345678"
     
   # Add restricted inbound rule
   aws ec2 authorize-security-group-ingress \
     --group-id "sg-12345678" \
     --protocol tcp \
     --port 443 \
     --cidr "10.0.0.0/16"
   ```

2. **Instance Metadata Service Configuration**:
   ```bash
   # CLI command to require IMDSv2
   aws ec2 modify-instance-metadata-options \
     --instance-id i-1234567890abcdef0 \
     --http-tokens required \
     --http-endpoint enabled
   ```

3. **Systems Manager Integration**:
   ```bash
   # CLI command to register an instance with SSM
   aws ssm create-association \
     --name "AWS-UpdateSSMAgent" \
     --targets "Key=instanceids,Values=i-1234567890abcdef0" \
     --schedule-expression "rate(14 days)"
   ```

## AWS Compliance Context

When relevant, include AWS compliance framework mappings:

1. **AWS Well-Architected Framework Pillars**:
   - Security
   - Reliability
   - Performance Efficiency
   - Cost Optimization
   - Operational Excellence
   - Sustainability

2. **Common Compliance Standards**:
   - CIS AWS Foundations Benchmark (specify control numbers)
   - NIST 800-53 (specify control IDs)
   - PCI DSS (specify requirement numbers)
   - HIPAA (specify relevant controls)
   - FedRAMP (specify control IDs)

Example compliance mapping:
```
This mitigation addresses:
- CIS AWS Foundations Benchmark: 2.1.2
- NIST 800-53: AC-6, CM-7
- PCI DSS: 7.1.1, 7.1.2
- AWS Well-Architected Framework: Security Pillar, SEC02-BP04
```

## AWS Resource and Service Naming

Use these standardized AWS service and resource naming conventions:

### Service Names
- Amazon Simple Storage Service (Amazon S3)
- Amazon Elastic Compute Cloud (Amazon EC2)
- AWS Identity and Access Management (IAM)
- Amazon Virtual Private Cloud (Amazon VPC)
- AWS CloudTrail
- Amazon CloudWatch
- AWS Security Hub

### Resource ARN Patterns
- S3 Buckets: `arn:aws:s3:::bucket-name`
- IAM Roles: `arn:aws:iam::account-id:role/role-name`
- EC2 Instances: `arn:aws:ec2:region:account-id:instance/instance-id`
- VPC: `arn:aws:ec2:region:account-id:vpc/vpc-id`
- Security Groups: `arn:aws:ec2:region:account-id:security-group/security-group-id`
