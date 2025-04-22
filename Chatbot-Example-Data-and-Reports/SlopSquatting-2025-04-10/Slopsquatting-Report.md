# Ghost in the Code Machine: How AI Hallucinations Create New Security Risks in the Cloud

**Date:** April 10, 2025  
**Author:** Kurt Seifried kseifried@cloudsecurityalliance.org

![Banner image illustrating slopsquatting concept](https://placeholder.image/slopsquatting-concept)

## What You Need to Know

AI coding assistants like ChatGPT, GitHub Copilot, and Claude are revolutionizing how developers write code - but they've also introduced a surprising new security risk called "slopsquatting." When these AI tools recommend packages that don't actually exist, attackers can create malicious versions of these hallucinated packages and wait for unsuspecting developers to install them. This report breaks down this emerging threat and what you can do to protect your organization.

## The New Attack in a Nutshell

Imagine asking an AI assistant to help you write some Python code to process images. The AI suggests: "First, install the `fastimageprocessor` package with `pip install fastimageprocessor`." You follow the instructions, the package installs successfully, and you continue coding. 

What you don't realize is that:
1. This package never existed until recently
2. The AI completely made it up (hallucinated it)
3. A malicious actor noticed this same hallucination, created the package, and filled it with malware
4. You've just willingly installed that malware on your system

This is **slopsquatting** - a play on the older term "typosquatting" (where attackers target common typing mistakes). But instead of targeting human error, slopsquatting exploits AI mistakes.

## Why This Matters to Cloud Security

This attack is particularly concerning in cloud environments for several reasons:

- **Scale and Automation**: Cloud CI/CD pipelines might automatically install packages recommended by AI coding assistants
- **Privileged Access**: Compromised cloud functions and containers can access sensitive cloud resources
- **Fast Deployment**: Cloud development often emphasizes speed, which may reduce security scrutiny
- **Widespread Impact**: A single compromised package can affect multiple services across an organization's cloud infrastructure

## The Evidence Is Clear

Recent research from a team of security experts examined 16 different AI code generators across 576,000 code samples and discovered:

- Nearly 20% of recommended packages don't exist
- Over 205,000 unique hallucinated package names were identified
- Commercial models like GPT-4 hallucinate at around 5% rate
- Open-source models hallucinate at much higher rates (over 20%)
- Most concerning: When the AI hallucinates a package name, it will often consistently repeat the same fake package name 

This consistency makes slopsquatting attacks highly viable - attackers don't need to guess what packages to target; they can simply observe what the AI tools consistently hallucinate.

## Real-World Attack Scenario

Here's how this plays out in the real world:

1. **Discovery**: An attacker prompts various AI coding assistants thousands of times, collecting all hallucinated package names
2. **Selection**: They identify package names that are consistently hallucinated and not yet registered
3. **Registration**: The attacker creates these packages on public repositories with embedded malware
4. **Waiting Game**: Legitimate developers using AI tools get the same hallucinated recommendations
5. **Compromise**: Developers install the now-malicious packages in development, CI/CD pipelines, or production environments
6. **Exploitation**: The malware in the package executes, stealing data, establishing persistence, or spreading further

## Warning Signs and Vulnerable Environments

Your organization is at higher risk if:

- Your developers regularly use AI coding assistants
- You employ "vibe coding" (letting AI generate substantial portions of code)
- Your CI/CD pipelines automatically install packages
- You don't use private package repositories with verification
- Your cloud environments lack robust package security controls

## Protection Strategies Anyone Can Implement

### For Individual Developers

1. **Verify Before Installing**: Always check if a package is legitimate before installing it
   - Check the package's popularity (download count, GitHub stars)
   - Verify the package's age (brand new packages deserve extra scrutiny)
   - Look for documentation and an active development community

2. **Use Private Repositories**: Configure npm, pip, or other package managers to use trusted private repositories

3. **Lower the AI Temperature**: When using AI coding tools, set lower "temperature" values (randomness) when possible, which reduces hallucination rates

### For Security Teams

1. **Configure Private Package Repositories**:
   - AWS: Use CodeArtifact
   - Azure: Use Azure Artifacts
   - GCP: Use Artifact Registry
   - Configure these as proxies for public repositories with additional validation

2. **Implement Pipeline Controls**:
   - Add package verification steps to CI/CD pipelines
   - Create security gates for first-time package installations
   - Generate alerts for suspicious package characteristics

3. **Leverage Cloud Security Tools**:
   - AWS: CodeGuru Security, Amazon Inspector
   - Azure: Microsoft Defender for Cloud
   - GCP: Security Command Center, Binary Authorization

4. **Monitor and Alert**:
   - Create alerts for newly published packages with low download counts
   - Monitor for unusual package installation patterns
   - Track package provenance across your environment

## Future-Proofing Your Organization

Looking beyond immediate fixes, here are long-term strategies:

1. **Developer Training**: Educate your team about AI hallucinations and secure coding practices

2. **Security Champions**: Designate security-focused developers to review AI-generated code

3. **Package Allowlisting**: Create approved package lists and require exceptions for others

4. **AI Auditing Tools**: Deploy tools that can detect potential hallucinations in AI-generated code

5. **Contribute to Community Solutions**: Support initiatives to help package repositories detect and prevent slopsquatting attacks

## The Big Picture

Slopsquatting represents a new frontier in supply chain attacks. As AI code generation becomes more ubiquitous, we'll likely see these attacks increase in sophistication and frequency. The fundamental vulnerability - AI hallucinations - cannot be completely eliminated with current technology.

The good news is that basic security hygiene and a healthy skepticism toward AI outputs can significantly reduce your risk. Verifying packages before installation, using private repositories, and implementing automated controls in your cloud environment will help protect your organization against this emerging threat.

## Key Takeaways

- AI coding assistants regularly hallucinate non-existent packages
- Attackers can exploit these hallucinations to distribute malware
- Cloud environments are particularly vulnerable due to automation and scale
- Simple verification steps can dramatically reduce your risk
- Long-term solutions will require collaboration between developers, security teams, AI companies, and package repositories

## Additional Resources

- [CAVEaT Technical STIX Documentation on Slopsquatting](link-to-technical-report)
- [Cloud Security Alliance Best Practices](https://cloudsecurityalliance.org)
- [We Have a Package for You!: Research on Package Hallucinations](https://arxiv.org/abs/2406.10279)
- [The Rise of Slopsquatting](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks)

---

*This report is provided for informational purposes only and represents the current understanding of the CAVEaT Working Group on this emerging threat. Security practices should be tailored to your organization's specific needs and environment.*
