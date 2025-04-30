# CAVEaT STIX Generator - Azure Courses of Action Module

Version: 2025-04-29
Author: Kurt Seifried, kseifried@cloudsecurityalliance.org

## Purpose

This module provides detailed Azure-specific guidance for implementing mitigations and courses of action for cloud security vulnerabilities. It includes standardized formats for Azure Portal, Azure CLI, PowerShell, Azure REST API, and ARM template implementations.

## Azure Implementation Standards

When documenting Azure mitigations, follow these standards to ensure consistency and completeness:

### Azure Service Coverage

For each mitigation, identify which Azure services are involved, including:
- Primary service (e.g., Storage, Virtual Machines, Azure AD)
- Supporting services (e.g., Monitor, Security Center, Sentinel)
- Integration points with other services
- Dependencies and prerequisites

### Azure Portal Instructions

When documenting portal-based remediation steps:

1. **Navigation Path**:
   - Start from the Azure Portal home page
   - List each navigation step with exact menu names
   - Use ">" to separate navigation steps
   - Example: "Azure Portal > Storage accounts > [storage-account-name] > Security"

2. **UI Element Reference**:
   - Reference UI elements by their exact names
   - Specify tabs, blades, buttons, toggles, and form fields
   - Note context menus or dropdown options
   - Include screenshots if possible (or describe what to look for)

3. **Format Template**:
   ```
   1. Sign in to the Azure Portal (https://portal.azure.com)
   2. Navigate to [Service] > [SubMenu] > [SubMenu]
   3. Select [Resource Name or Type]
   4. Click the [Tab/Blade/Button/Link Name]
   5. Configure [Setting Name] to [Value]
   6. Click [Save/Apply/Update]
   ```

### Azure CLI Implementation

When documenting Azure CLI commands:

1. **Command Structure**:
   - Provide the complete CLI command with all required parameters
   - Include options with descriptions
   - Show example values for variables
   - Include both the command and its expected output

2. **Prerequisites**:
   - Specify required Azure CLI version
   - Note any required extensions
   - Include any necessary permissions or roles

3. **Format Template**:
   ```bash
   # Install or update Azure CLI (if needed)
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

   # Login to Azure (if needed)
   az login

   # Select subscription (if needed)
   az account set --subscription "Subscription Name or ID"

   # Main remediation command
   az [service] [command] \
     --parameter1 value1 \
     --parameter2 value2 \
     --parameter3 value3

   # Verification command
   az [service] [verification-command] \
     --resource-id [id]
   ```

### Azure PowerShell Implementation

When documenting Azure PowerShell cmdlets:

1. **Command Structure**:
   - Provide the complete PowerShell cmdlets with all required parameters
   - Include options with descriptions
   - Show example values for variables
   - Include both the command and its expected output

2. **Prerequisites**:
   - Specify required PowerShell module versions
   - Note any required modules to import
   - Include any necessary permissions or roles

3. **Format Template**:
   ```powershell
   # Install PowerShell modules (if needed)
   Install-Module -Name Az -AllowClobber -Force

   # Login to Azure (if needed)
   Connect-AzAccount

   # Select subscription (if needed)
   Set-AzContext -Subscription "Subscription Name or ID"

   # Main remediation cmdlet
   [Cmdlet-Name] `
     -Parameter1 "value1" `
     -Parameter2 "value2" `
     -Parameter3 "value3"

   # Verification cmdlet
   [Verification-Cmdlet] -ResourceId "[resource-id]"
   ```

### Azure REST API Implementation

When documenting Azure REST API calls:

1. **Multiple Language Support**:
   - Provide examples in at least Python and JavaScript/Node.js
   - Use standard libraries for HTTP requests
   - Include authentication setup using Azure Identity libraries
   - Show error handling

2. **Code Structure**:
   - Include complete, runnable code samples
   - Document all parameters
   - Show authentication setup
   - Include comments explaining key steps

3. **Format Template (Python Example)**:
   ```python
   # Install dependencies (if needed)
   # pip install azure-identity requests

   import requests
   from azure.identity import DefaultAzureCredential

   # Get token for Azure Resource Manager
   credential = DefaultAzureCredential()
   token = credential.get_token("https://management.azure.com/.default")

   # Prepare API request headers
   headers = {
       'Authorization': f'Bearer {token.token}',
       'Content-Type': 'application/json'
   }

   # API endpoint
   subscription_id = "00000000-0000-0000-0000-000000000000"
   resource_group = "resource-group-name"
   resource_name = "resource-name"
   api_version = "2023-01-01"
   
   url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Service/resourceType/{resource_name}?api-version={api_version}"

   # Main remediation function
   def apply_mitigation(parameter1, parameter2):
       payload = {
           "properties": {
               "securityProperty1": parameter1,
               "securityProperty2": parameter2
           }
       }
       
       response = requests.patch(url, headers=headers, json=payload)
       response.raise_for_status()  # Raise exception for HTTP errors
       return response.json()

   # Verification function
   def verify_mitigation():
       response = requests.get(url, headers=headers)
       response.raise_for_status()
       return response.json()['properties']['securityStatus']

   # Example usage
   if __name__ == "__main__":
       result = apply_mitigation("value1", "value2")
       print(result)
       
       status = verify_mitigation()
       print(f"Verification Status: {status}")
   ```

### Azure ARM Templates

When documenting Infrastructure as Code solutions:

1. **Template Structure**:
   - Provide complete, validated ARM templates
   - Include all required resources and properties
   - Add comments explaining security-relevant settings
   - Include parameters for customization

2. **Secure Defaults**:
   - Ensure templates have secure default values
   - Document security-focused parameters
   - Include constraints and validations
   - Note any required RBAC permissions

3. **Format Template**:
   ```json
   {
     "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
     "contentVersion": "1.0.0.0",
     "parameters": {
       "environmentType": {
         "type": "string",
         "defaultValue": "Production",
         "allowedValues": [
           "Development",
           "Test",
           "Production"
         ],
         "metadata": {
           "description": "Environment type"
         }
       }
     },
     "variables": {
       "securitySettings": {
         "Production": {
           "propertyValue": "secure-value"
         },
         "Development": {
           "propertyValue": "dev-value"
         },
         "Test": {
           "propertyValue": "test-value"
         }
       }
     },
     "resources": [
       {
         "type": "Microsoft.Service/resourceType",
         "apiVersion": "2023-01-01",
         "name": "[parameters('resourceName')]",
         "location": "[parameters('location')]",
         "properties": {
           "securityProperty1": true,
           "securityProperty2": "[variables('securitySettings')[parameters('environmentType')].propertyValue]"
         }
       }
     ],
     "outputs": {
       "securityStatus": {
         "type": "string",
         "value": "[reference(parameters('resourceName')).securityStatus]"
       }
     }
   }
   ```

## Azure Verification Techniques

For each Azure mitigation, include specific verification methods:

### Portal Verification
- Specific portal pages to check
- Visual indicators of secure configuration
- Dashboard views or status indicators
- Example: "Verify that 'Secure transfer required' shows 'Enabled' on the storage account overview page"

### CLI Verification Commands
```bash
# Example storage account encryption verification
az storage account show \
  --name mystorageaccount \
  --resource-group myresourcegroup \
  --query 'encryption'

# Example network security group verification
az network nsg show \
  --name mynsg \
  --resource-group myresourcegroup \
  --query 'securityRules'

# Example key vault access policy verification
az keyvault show \
  --name mykeyvault \
  --resource-group myresourcegroup \
  --query 'properties.accessPolicies'
```

### PowerShell Verification Commands
```powershell
# Example storage account encryption verification
Get-AzStorageAccount `
  -Name mystorageaccount `
  -ResourceGroupName myresourcegroup | 
  Select-Object -ExpandProperty Encryption

# Example network security group verification
Get-AzNetworkSecurityGroup `
  -Name mynsg `
  -ResourceGroupName myresourcegroup | 
  Select-Object -ExpandProperty SecurityRules

# Example key vault access policy verification
Get-AzKeyVault `
  -Name mykeyvault `
  -ResourceGroupName myresourcegroup | 
  Select-Object -ExpandProperty AccessPolicies
```

### Automated Verification
- Azure Policy definitions to audit compliant/non-compliant resources
- Azure Monitor alerts to track security settings
- Microsoft Defender for Cloud recommendations
- Example: "Create an Azure Policy to audit storage accounts not requiring secure transfer"

## Azure-Specific Security Services

When appropriate, include guidance on leveraging these Azure security services:

1. **Microsoft Defender for Cloud**:
   - Enable standard or premium tier
   - Configure security policies
   - Implement recommendations

2. **Azure Policy**:
   - Assign built-in policy definitions
   - Create custom policy definitions
   - Implement remediation tasks

3. **Microsoft Sentinel**:
   - Enable relevant data connectors
   - Deploy analytic rules
   - Configure automated response

4. **Azure Active Directory (Azure AD)**:
   - Implement Conditional Access policies
   - Enable MFA and Privileged Identity Management
   - Configure identity protection

5. **Azure Monitor**:
   - Create activity log alerts
   - Configure diagnostic settings
   - Implement Log Analytics workspaces

## Azure Service-Specific Templates

### Storage Security Template

For Azure Storage-related vulnerabilities, include:

1. **Secure Transfer Configuration**:
   ```bash
   # CLI command
   az storage account update \
     --name mystorageaccount \
     --resource-group myresourcegroup \
     --https-only true
   ```

2. **Blob Container Access Level**:
   ```bash
   # CLI command
   az storage container set-permission \
     --name mycontainer \
     --account-name mystorageaccount \
     --public-access off
   ```

3. **Storage Account Encryption**:
   ```bash
   # CLI command
   az storage account update \
     --name mystorageaccount \
     --resource-group myresourcegroup \
     --encryption-services blob file queue table \
     --encryption-key-source Microsoft.Storage
   ```

### Azure Active Directory Security Template

For Azure AD-related vulnerabilities, include:

1. **Conditional Access Policy**:
   ```powershell
   # PowerShell command
   New-AzureADMSConditionalAccessPolicy `
     -DisplayName "Require MFA for all users" `
     -State "enabled" `
     -Conditions @{
         "ClientAppTypes" = @("all");
         "Applications" = @{
             "IncludeApplications" = @("all")
         };
         "Users" = @{
             "IncludeUsers" = @("all")
         }
     } `
     -GrantControls @{
         "Operator" = "OR";
         "BuiltInControls" = @("mfa")
     }
   ```

2. **Privileged Identity Management**:
   ```bash
   # CLI command to list eligible role assignments
   az rest --method get \
     --uri "https://management.azure.com/providers/Microsoft.Subscription/subscriptions?api-version=2020-01-01" \
     --query "value[].{Name:displayName, Id:subscriptionId}" \
     --output table
   
   # Additional steps would need to be included for complete PIM configuration
   ```

3. **Identity Protection Configuration**:
   ```powershell
   # PowerShell command
   Set-AzureADMSIdentityProtectionPolicy `
     -SignInRiskPolicy @{
         "State" = "enabled";
         "RiskLevelDuringSignIn" = "medium";
         "Action" = "mfa"
     }
   ```

### Virtual Machine Security Template

For Azure VM-related vulnerabilities, include:

1. **Network Security Group Rules**:
   ```bash
   # CLI command to create a secure NSG
   az network nsg create \
     --name SecureWebServerNSG \
     --resource-group myresourcegroup \
     --location eastus
     
   # Add restricted inbound rule
   az network nsg rule create \
     --name AllowHttps \
     --nsg-name SecureWebServerNSG \
     --resource-group myresourcegroup \
     --protocol tcp \
     --direction inbound \
     --source-address-prefix Internet \
     --source-port-range "*" \
     --destination-address-prefix "*" \
     --destination-port-range 443 \
     --access allow \
     --priority 100
   ```

2. **Disk Encryption Configuration**:
   ```bash
   # CLI command to enable disk encryption
   az vm encryption enable \
     --resource-group myresourcegroup \
     --name myvm \
     --disk-encryption-keyvault mykeyvault \
     --volume-type all
   ```

3. **Microsoft Antimalware Extension**:
   ```bash
   # CLI command to add Microsoft Antimalware extension
   az vm extension set \
     --resource-group myresourcegroup \
     --vm-name myvm \
     --name IaaSAntimalware \
     --publisher Microsoft.Azure.Security \
     --settings '{"AntimalwareEnabled": true, "RealtimeProtectionEnabled": true, "ScheduledScanSettings": {"isEnabled": true, "day": 7, "time": 120, "scanType": "Quick"}, "Exclusions": {"Extensions": "", "Paths": "", "Processes": ""}}'
   ```

## Azure Compliance Context

When relevant, include Azure compliance framework mappings:

1. **Azure Well-Architected Framework Pillars**:
   - Security
   - Reliability
   - Performance Efficiency
   - Cost Optimization
   - Operational Excellence

2. **Common Compliance Standards**:
   - Azure Security Benchmark (specify control numbers)
   - NIST 800-53 (specify control IDs)
   - PCI DSS (specify requirement numbers)
   - HIPAA (specify relevant controls)
   - ISO 27001 (specify control IDs)

Example compliance mapping:
```
This mitigation addresses:
- Azure Security Benchmark: NS-1, NS-2
- NIST 800-53: AC-4, SC-7
- PCI DSS: 1.3, 1.3.2
- Azure Well-Architected Framework: Security Pillar, SEC-04
```

## Azure Resource and Service Naming

Use these standardized Azure service and resource naming conventions:

### Service Names
- Azure Blob Storage
- Azure Virtual Machines
- Azure Active Directory (Microsoft Entra ID)
- Azure Virtual Network
- Microsoft Defender for Cloud
- Azure Monitor
- Azure Key Vault

### Resource ARM IDs
- Storage Accounts: `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}`
- Virtual Machines: `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}`
- Network Security Groups: `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{nsgName}`
- Key Vaults: `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}`
- App Services: `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}`
