 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 (rough draft – currently editing) 
Remote Code Execution (version 1.1) 
 
Cloud Service Label: IaaS, PaaS 
 
Description 
Adversaries may be able to utilize remote code execution 
 
Examples 
Name Description 
CVE-2019 -1372 “A remote code execution vulnerability exists when Azure App Service/ Antares 
on Azure Stack fails to check the length of a buffer prior to copying memory to it. 
An attacker who successfully exploited this vulnerability could allow an 
unprivileged function run by the user to execute code in the context of NT 
AUTHORITY \system thereby escaping the Sandbox. The security update 
addresses the vulnerability by ensuring that Azure App Service sanitizes user 
inputs., aka 'Azure App Service Remote Code Execution Vul nerability'.” 
 
Mitigations 
Mitigation Description 
Two Factor Authentication Use multi -factor authentication for user and privileged accounts. Do not manage 
Cloud portals from machines that perform user email and web browsing tasks. 
All users should be required to utilize two factor authentication. 
 AWS This can be enforced by first creating a policy that would prohibit actions except 
those that allow a user to change their password or manage 2FA, then 
attaching a policy to a group that includes all user accounts where they can be 
allowed all access if th ey sign in with 2FA. Once these actions are completed it 
should be tested to verify the access is given correctly. To see full details on 
how to complete this view AWS documentation at: 
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_users -self-
manage -mfa-and-creds.html. 
 Azure This can be done by creating a MFA registration policy. It can than be assigned 
to all users (with the ability to exclude some if need be, but is not 
recommended). Make sure once the policy is created and added to users that it 
is then being enforced, once enforced it should be tested for verification. To see 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 full details on how to complete this view Azure documentation at: 
https://docs.microsoft.com/en -us/azure/active -directory/identity -
protection/howto -identity -protection -configure -mfa-policy. 
 GCP This can be done by first enabling it on the current account being used by 
admin to assign the roles, then enable two factor on an instance by instance or 
project by project basis, then assigning the requirements based on IAM roles 
and applying it to all u sers. To see full details on how to complete this view 
Azure documentation at: 
https://cloud.google.com/compute/docs/oslogin/setup -two-factor -
authentication. 
Enable GKE Metadata Server Consider enabling GKE Metadata Server which improves security and replaces 
Compute Engine VM instances Metadata Server. 
Least Privilege All access given to users in the cloud environment should be assigned by the 
necessary privileges needed for team members to complete their job 
responsibilities. Ensure that temporary access tokens are issued rather than 
permanent credentials, especially when access is being granted to entities 
outside of the internal security boundary . 
 AWS To implement least privilege in an AWS environment IAM policies will be used. 
This gives the ability to allow users to perform list, read, write, permissions 
management, or tagging actions. AWS suggests utilizing last accessed 
information and A WS CloudTrail event history to get a better understanding of 
privileges that might be needed or reduced based on a specific role. Full details 
can be found at https://docs.aws.amazon.com/IAM/latest/UserGuide/best -
practices.html#grant -least -privilege. 
 Azure To implement least privilege in an Azure environment Azure Active Directory 
roles will be used. Azure outlines different tasks and the least privileged role 
that are suggested to be associated with the task. Those details can be found 
at: https://docs.microsoft.com/en -us/azure/active -directory/users -groups -
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
 
References 
1. https://cve.mitre.org/cgi -bin/cvename.cgi?name=CVE -2019 -1372. Accessed July 
2, 2020. 
 