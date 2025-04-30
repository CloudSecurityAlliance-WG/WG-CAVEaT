# CAVEaT STIX Generator - GCP Courses of Action Module

Version: 2025-04-29
Author: Kurt Seifried, kseifried@cloudsecurityalliance.org

## Purpose

This module provides detailed Google Cloud Platform (GCP) specific guidance for implementing mitigations and courses of action for cloud security vulnerabilities. It includes standardized formats for Google Cloud Console, gcloud CLI, REST API, and Terraform implementations.

## GCP Implementation Standards

When documenting GCP mitigations, follow these standards to ensure consistency and completeness:

### GCP Service Coverage

For each mitigation, identify which GCP services are involved, including:
- Primary service (e.g., Cloud Storage, Compute Engine, IAM)
- Supporting services (e.g., Cloud Logging, Cloud Monitoring, Security Command Center)
- Integration points with other services
- Dependencies and prerequisites

### Google Cloud Console Instructions

When documenting console-based remediation steps:

1. **Navigation Path**:
   - Start from the Google Cloud Console home page
   - List each navigation step with exact menu names
   - Use ">" to separate navigation steps
   - Example: "Google Cloud Console > Cloud Storage > [bucket-name] > Permissions"

2. **UI Element Reference**:
   - Reference UI elements by their exact names
   - Specify tabs, panels, buttons, toggles, and form fields
   - Note context menus or dropdown options
   - Include screenshots if possible (or describe what to look for)

3. **Format Template**:
   ```
   1. Sign in to the Google Cloud Console (https://console.cloud.google.com)
   2. Navigate to [Service] > [SubMenu] > [SubMenu]
   3. Select [Resource Name or Type]
   4. Click the [Tab/Panel/Button/Link Name]
   5. Configure [Setting Name] to [Value]
   6. Click [Save/Apply/Update]
   ```

### gcloud CLI Implementation

When documenting gcloud CLI commands:

1. **Command Structure**:
   - Provide the complete CLI command with all required parameters
   - Include options with descriptions
   - Show example values for variables
   - Include both the command and its expected output

2. **Prerequisites**:
   - Specify required gcloud CLI version
   - Note any required components or extensions
   - Include any necessary permissions or roles

3. **Format Template**:
   ```bash
   # Install or update gcloud CLI (if needed)
   curl https://sdk.cloud.google.com | bash
   gcloud components update

   # Authenticate to GCP (if needed)
   gcloud auth login

   # Set project (if needed)
   gcloud config set project "project-id"

   # Main remediation command
   gcloud [service] [command] \
     --parameter1=value1 \
     --parameter2=value2 \
     --parameter3=value3

   # Verification command
   gcloud [service] [verification-command] \
     --resource=[resource-id]
   ```

### GCP REST API Implementation

When documenting GCP REST API calls:

1. **Multiple Language Support**:
   - Provide examples in at least Python and JavaScript/Node.js
   - Use Google Cloud client libraries when possible
   - Include authentication setup
   - Show error handling

2. **Code Structure**:
   - Include complete, runnable code samples
   - Document all parameters
   - Show authentication setup
   - Include comments explaining key steps

3. **Format Template (Python Example)**:
   ```python
   # Install dependencies (if needed)
   # pip install google-cloud-storage google-auth

   from google.cloud import storage
   from google.oauth2 import service_account

   # Set up authentication (using service account)
   credentials = service_account.Credentials.from_service_account_file(
       'path/to/service-account-key.json')

   # Initialize client
   client = storage.Client(credentials=credentials, project='project-id')

   # Main remediation function
   def apply_mitigation(resource_id, parameter1, parameter2):
       # Get the resource
       resource = client.get_bucket(resource_id)
       
       # Apply security changes
       resource.iam_configuration.uniform_bucket_level_access_enabled = parameter1
       resource.update()
       
       return "Mitigation applied successfully"

   # Verification function
   def verify_mitigation(resource_id):
       resource = client.get_bucket(resource_id)
       return resource.iam_configuration.uniform_bucket_level_access_enabled

   # Example usage
   if __name__ == "__main__":
       result = apply_mitigation('my-bucket', True, 'value2')
       print(result)
       
       status = verify_mitigation('my-bucket')
       print(f"Verification Status: {status}")
   ```

### Terraform Implementation

When documenting Infrastructure as Code solutions:

1. **Template Structure**:
   - Provide complete, validated Terraform templates
   - Include all required resources and properties
   - Add comments explaining security-relevant settings
   - Include variables for customization

2. **Secure Defaults**:
   - Ensure templates have secure default values
   - Document security-focused variables
   - Include validation blocks for variables
   - Note any required IAM permissions

3. **Format Template**:
   ```hcl
   # Provider configuration
   provider "google" {
     project = var.project_id
     region  = var.region
   }

   # Variables
   variable "project_id" {
     description = "The GCP project ID"
     type        = string
   }

   variable "region" {
     description = "The GCP region"
     type        = string
     default     = "us-central1"
   }

   variable "environment" {
     description = "Environment type"
     type        = string
     default     = "production"
     validation {
       condition     = contains(["development", "test", "production"], var.environment)
       error_message = "Environment must be development, test, or production."
     }
   }

   # Local variables for security settings
   locals {
     security_settings = {
       production = {
         secure_property = true
         encryption      = "CMEK"
       }
       development = {
         secure_property = true
         encryption      = "GOOGLE_MANAGED"
       }
       test = {
         secure_property = true
         encryption      = "GOOGLE_MANAGED"
       }
     }
   }

   # Resource with security configuration
   resource "google_storage_bucket" "secure_bucket" {
     name          = "secure-bucket-${var.environment}"
     location      = var.region
     force_destroy = false
     
     # Security settings
     uniform_bucket_level_access = true  # Security best practice
     
     encryption {
       default_kms_key_name = local.security_settings[var.environment].encryption == "CMEK" ? google_kms_crypto_key.key[0].id : null
     }
     
     logging {
       log_bucket        = google_storage_bucket.logging.name
       log_object_prefix = "secure-bucket-logs"
     }
     
     # Additional security settings
     versioning {
       enabled = true  # Enable versioning for data protection
     }
   }

   # Outputs for verification
   output "security_status" {
     description = "Security configuration status"
     value = {
       uniform_bucket_level_access = google_storage_bucket.secure_bucket.uniform_bucket_level_access
       encryption_type             = local.security_settings[var.environment].encryption
       versioning_enabled          = google_storage_bucket.secure_bucket.versioning[0].enabled
     }
   }
   ```

## GCP Verification Techniques

For each GCP mitigation, include specific verification methods:

### Console Verification
- Specific console pages to check
- Visual indicators of secure configuration
- Dashboard views or status indicators
- Example: "Verify that 'Uniform bucket-level access' shows 'Enabled' on the bucket permissions page"

### CLI Verification Commands
```bash
# Example Cloud Storage bucket permission verification
gcloud storage buckets describe gs://my-bucket \
  --format="json(iamConfiguration.uniformBucketLevelAccess)"

# Example Compute Engine firewall verification
gcloud compute firewall-rules describe my-firewall-rule \
  --format="json(sourceRanges,allowed)"

# Example IAM policy verification
gcloud projects get-iam-policy my-project \
  --format="json(bindings)"
```

### API Verification
```python
# Example Cloud Storage bucket permission verification
from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('my-bucket')
print(f"Uniform Bucket-Level Access: {bucket.iam_configuration.uniform_bucket_level_access_enabled}")
```

### Automated Verification
- Security Command Center findings to detect non-compliant resources
- Cloud Monitoring alerts to track security settings
- Cloud Asset Inventory queries
- Example: "Create a Security Command Center custom finding to detect buckets without uniform bucket-level access"

## GCP-Specific Security Services

When appropriate, include guidance on leveraging these GCP security services:

1. **Security Command Center**:
   - Enable standard or premium tier
   - Configure security sources
   - Implement findings export

2. **Binary Authorization**:
   - Configure attestation requirements
   - Set up attestors
   - Implement deploy-time policy enforcement

3. **Cloud Armor**:
   - Create security policies
   - Configure WAF rules
   - Implement DDoS protection

4. **Identity-Aware Proxy (IAP)**:
   - Configure access policies
   - Set up OAuth consent screen
   - Implement context-aware access

5. **VPC Service Controls**:
   - Define service perimeter
   - Configure access levels
   - Implement ingress/egress policies

## GCP Service-Specific Templates

### Cloud Storage Security Template

For Cloud Storage-related vulnerabilities, include:

1. **Uniform Bucket-Level Access**:
   ```bash
   # CLI command
   gcloud storage buckets update gs://my-bucket \
     --uniform-bucket-level-access
   ```

2. **Bucket IAM Policy**:
   ```bash
   # CLI command to set specific IAM permissions
   gcloud storage buckets add-iam-policy-binding gs://my-bucket \
     --member="user:user@example.com" \
     --role="roles/storage.objectViewer"
   
   # Remove public access
   gcloud storage buckets remove-iam-policy-binding gs://my-bucket \
     --member="allUsers" \
     --role="roles/storage.objectViewer"
   ```

3. **Bucket Encryption**:
   ```bash
   # CLI command for CMEK encryption
   gcloud storage buckets update gs://my-bucket \
     --default-encryption-key=projects/my-project/locations/global/keyRings/my-keyring/cryptoKeys/my-key
   ```

### IAM Security Template

For IAM-related vulnerabilities, include:

1. **Custom Role with Least Privilege**:
   ```bash
   # CLI command to create a custom role
   gcloud iam roles create customRoleName \
     --project=my-project \
     --title="Custom Role Title" \
     --description="Custom role description" \
     --permissions=compute.instances.get,compute.instances.list \
     --stage=GA
   ```

2. **Service Account Key Management**:
   ```bash
   # CLI command to list service account keys
   gcloud iam service-accounts keys list \
     --iam-account=my-service-account@my-project.iam.gserviceaccount.com

   # CLI command to delete a service account key
   gcloud iam service-accounts keys delete \
     --iam-account=my-service-account@my-project.iam.gserviceaccount.com \
     key-id
   ```

3. **Organization Policy Constraint**:
   ```bash
   # CLI command to set domain restricted sharing
   gcloud resource-manager org-policies set-policy \
     --organization=123456789012 policy.yaml

   # Contents of policy.yaml:
   # constraint: constraints/iam.allowedPolicyMemberDomains
   # listPolicy:
   #   allowedValues:
   #   - 'C0xxxxxxx'  # customer ID for your organization
   ```

### Compute Engine Security Template

For Compute Engine-related vulnerabilities, include:

1. **VPC Firewall Rules**:
   ```bash
   # CLI command to create a secure firewall rule
   gcloud compute firewall-rules create allow-https \
     --direction=INGRESS \
     --priority=1000 \
     --network=default \
     --action=ALLOW \
     --rules=tcp:443 \
     --source-ranges=203.0.113.0/24 \
     --target-tags=https-server
   ```

2. **OS Login Configuration**:
   ```bash
   # CLI command to enable OS Login at project level
   gcloud compute project-info add-metadata \
     --metadata enable-oslogin=TRUE
   
   # CLI command to enable OS Login for a specific instance
   gcloud compute instances add-metadata my-instance \
     --metadata enable-oslogin=TRUE
   ```

3. **Shielded VM Configuration**:
   ```bash
   # CLI command to create a Shielded VM
   gcloud compute instances create my-instance \
     --machine-type=e2-medium \
     --subnet=default \
     --shielded-secure-boot \
     --shielded-vtpm \
     --shielded-integrity-monitoring
   ```

## GCP Compliance Context

When relevant, include GCP compliance framework mappings:

1. **GCP Security Foundations Blueprint**:
   - Reference specific sections or controls

2. **Common Compliance Standards**:
   - NIST 800-53 (specify control IDs)
   - PCI DSS (specify requirement numbers)
   - HIPAA (specify relevant controls)
   - ISO 27001 (specify control IDs)

Example compliance mapping:
```
This mitigation addresses:
- GCP Security Foundations Blueprint: Resource Hierarchy, Section 2.2
- NIST 800-53: AC-3, AC-6
- PCI DSS: 7.1, 7.2
- HIPAA: Access Control (§ 164.312(a))
```

## GCP Resource and Service Naming

Use these standardized GCP service and resource naming conventions:

### Service Names
- Google Cloud Storage
- Compute Engine
- Cloud Identity and Access Management (IAM)
- Virtual Private Cloud (VPC)
- Cloud Logging
- Cloud Monitoring
- Security Command Center

### Resource URI Formats
- Storage Buckets: `gs://bucket-name`
- Compute Instances: `projects/project-id/zones/zone/instances/instance-name`
- KMS Keys: `projects/project-id/locations/location/keyRings/keyring-name/cryptoKeys/key-name`
- IAM Roles: `projects/project-id/roles/role-id` or `roles/predefined-role`
- VPC Networks: `projects/project-id/global/networks/network-name`
