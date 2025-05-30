# Silver SAML Attack: Cloud Identity Federation Vulnerability

## Executive Summary

The Silver SAML attack, discovered in early 2024 by Semperis researchers, represents a significant evolution of the previously known Golden SAML attack technique that was used in the SolarWinds breach. While Golden SAML targeted on-premises Active Directory Federation Services (AD FS), Silver SAML specifically targets cloud identity providers like Microsoft Entra ID (formerly Azure AD) and potentially affects AWS and GCP's identity federation capabilities as well.

This attack enables threat actors to forge SAML authentication responses and impersonate any user to any cloud application configured for SAML-based single sign-on. The attack is particularly concerning because it can bypass mitigations put in place specifically to address the original Golden SAML technique.

## Impact Analysis Across Major Cloud Providers

### Microsoft Azure (Entra ID)
- Primary target and confirmed vulnerable platform
- Any application using Entra ID for SAML-based authentication is at risk
- Both SP-initiated and IdP-initiated SAML flows are vulnerable
- High severity impact with potential for complete administrative access to connected applications

### Amazon Web Services (AWS)
- AWS IAM Identity Center (formerly SSO) and direct IAM SAML federation are potentially affected
- Could allow unauthorized access to AWS Management Console and services
- Forged SAML assertions could be used to obtain temporary security credentials

### Google Cloud Platform (GCP)
- GCP Identity Platform and Google Workspace federation capabilities are potentially vulnerable
- Similar to AWS and Azure, relies on SAML certificate validation that could be bypassed
- Could allow unauthorized access to GCP resources

## Key Findings

1. **Attack Vector**: The vulnerability occurs when cloud providers allow importing externally-generated certificates for SAML signing. If attackers obtain the private key of these certificates, they can forge SAML responses.

2. **Widespread Impact**: Due to the prevalence of SAML-based authentication for cloud applications, this attack technique can affect a wide range of organizations and services.

3. **Low Detection Probability**: Silver SAML attacks can be difficult to detect as they appear as legitimate authentications from the perspective of the target application.

4. **Architectural Weakness**: The fundamental issue lies in the SAML protocol design and how cloud providers implement certificate management for federation.

5. **Lack of Vendor Urgency**: Microsoft has assessed this as a "by-design" issue that "does not meet MSRC's bar for immediate servicing" despite the severity.

## Technical Details

### Attack Methodology

1. **Certificate Acquisition**: The attacker obtains the private key of an externally generated certificate used by the cloud identity provider for SAML signing. This could happen through:
   - Theft of certificate PFX files shared through insecure channels
   - Export from client machines where certificates were generated
   - Access to web servers where certificates are stored
   - Exploitation of access controls in key management systems like Azure Key Vault

2. **SAML Response Forgery**: Using tools like SilverSAMLForger, the attacker creates a forged SAML response containing claims for any user they wish to impersonate, including administrators.

3. **Authentication Bypass**:
   - In SP-initiated flows: The attacker intercepts the SAML request and replaces the SAML response with their forged response
   - In IdP-initiated flows: The attacker posts the forged SAML response directly to the application, completely bypassing the identity provider

4. **Access Exploitation**: Once authenticated as the target user, the attacker has access to all resources and capabilities available to that user within the application.

### Key Differences from Golden SAML

- **Target Environment**: Golden SAML targeted on-premises AD FS, while Silver SAML targets cloud identity providers
- **Certificate Source**: Golden SAML required compromising AD FS servers, while Silver SAML exploits externally generated certificates
- **Mitigation Bypass**: Silver SAML bypasses mitigations implemented after SolarWinds to move authentication to the cloud

## Courses of Action

### Immediate Tactical Mitigations

#### For Microsoft Entra ID
- Use only built-in, self-signed certificates generated by Entra ID for SAML signing
- Remove any externally-generated certificates
- Monitor Entra ID audit logs for changes to PreferredTokenSigningKeyThumbprint
- Limit who has ownership over applications in Entra ID

#### For AWS IAM Identity Center
- Use only AWS-managed certificates where possible
- Implement strict IAM policies for users who can manage SAML providers
- Verify certificate management practices for any externally managed identity providers

#### For GCP
- Use Google-generated certificates where possible
- Implement least-privilege access to identity configuration
- Monitor audit logs for unexpected identity provider changes

### Universal Mitigations

1. **Migrate from SAML to OIDC** where supported:
   - OIDC doesn't rely on certificates in the same way SAML does
   - Uses JWT tokens signed with keys that aren't directly exportable

2. **Implement strict monitoring**:
   - Monitor for changes to SAML certificates across all cloud providers
   - Set up alerts for unexpected certificate changes
   - Review service principal/identity provider permissions regularly

3. **Implement proper access controls**:
   - Limit who can manage SAML configurations
   - Apply just-in-time privilege access for identity administration
   - Use privileged access workstations for identity management tasks

4. **For application developers**:
   - Require SP-initiated flows that validate the InResponseTo parameter
   - Enforce strict time validation on SAML responses
   - Consider adding additional authentication factors beyond SAML

## Platform-Level Architectural Solutions

1. **Enhanced Certificate Validation**: Cloud providers should implement stricter validation of certificates used for SAML signing, preventing the use of externally-generated certificates or adding additional verification steps.

2. **Strong Identity Binding**: SAML responses should include additional validation parameters tied to user identity that cannot be easily forged.

3. **Multi-Factor Federation**: Adding required secondary verification channels for federation authentication could prevent Silver SAML attacks.

4. **Next-Generation Federation Protocols**: Development of more secure federation protocols that address the limitations of SAML.

5. **Behavioral Authentication**: Implementing risk-based authentication that considers behavioral patterns alongside SAML assertions.

## Detection Guidance

### Indicators of Compromise

1. **Certificate Changes**:
   - Unexpected or unauthorized changes to SAML signing certificates
   - New certificates being added to service principals
   - Changes to PreferredTokenSigningKeyThumbprint in Entra ID

2. **Authentication Anomalies**:
   - SAML authentications with no corresponding sign-in events in the identity provider's audit logs
   - Unusual patterns of application access via SAML
   - Administrative actions following SAML-based authentications from unusual sources

### Monitoring Recommendations

1. **Implement alerts for certificate changes** in all cloud identity providers
2. **Correlate identity provider and application logs** to detect SAML authentications without corresponding sign-in events
3. **Review certificate properties** to identify non-provider generated certificates
4. **Monitor for unusual access patterns** following SAML authentications

## References

1. Semperis Research: "Meet Silver SAML: Golden SAML in the Cloud" (February 2024)
2. The Hacker News: "New Silver SAML Attack Evades Golden SAML Defenses in Identity Systems" (February 2024)
3. Dark Reading: "Echoes of SolarWinds in New 'Silver SAML' Attack Technique" (February 2024)
4. CyberArk Research: "Golden SAML: Newly Discovered Attack Technique Forges Authentication to Cloud Apps" (Original Golden SAML research)
5. Microsoft Security Response Center: Assessment of Silver SAML (February 26, 2024)
6. GitHub: "SilverSamlForger" - Silver SAML forgery tool

## Conclusion

The Silver SAML attack highlights the ongoing evolution of cloud identity attacks and demonstrates how security mitigations can sometimes lead to new attack vectors. Organizations should implement the recommended mitigations immediately while cloud providers work on more fundamental architectural solutions to address the underlying vulnerabilities in federated authentication systems.

This threat documentation serves as a comprehensive resource for understanding, detecting, and mitigating Silver SAML attacks across major cloud providers.