 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 Deprecated Cloud API’s (version 1.0) 
 
Cloud Service Label: IaaS, PaaS 
 
Description 
Cloud Service Providers (CSPs) are constantly adding services and updating their APIs. 
This situation creates a fair amount of deprecation within the CSP environment. To 
maintain backwards capability, many of these deprecated API’s still work even after 
they are no longer officially documented and maintained. Both Azure and GCP as 
newer more dynamic clouds are especially prone to this phenomenon. Deprecated APIs 
are likely not to be well integrated with new security logging mechanisms and controls. 
This offers an adversary who does some research a potential method of interacting with 
cloud services in a manner that may not be observed or prevented by otherwise strong 
controls. 
 
Examples 
Name Description 
Azure Classic Previous Console and API suite for managing Azure 
resources 2017 and prior. 
 
Mitigations 
Mitigation Description 
Manage log data like other sensitive data 
 Ensure log data is protected and managed like any 
other confidential data source with encryption at rest 
and positive control. 
 
Detection 
Difficult to detect gaps in deprecated API’s. 
(© 2022 The MITRE Corporation All Rights Reserved. Draft Content 
Submission for Consideration by the CAVEAT Working Group) 
 
References 
1. https://docs.microsoft.com/en -us/azure/azure -resource -
manager/management/deployment -models, - Accessed March 5, 2020 