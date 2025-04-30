# CAVEaT STIX Generator - Simple File Management

Version: 2025-04-29
Author: Kurt Seifried, kseifried@cloudsecurityalliance.org

## Purpose
Basic guidelines for saving STIX files and managing file size.

## File Saving Basics

1. **Ask User for Directory**
   - Always ask the user where they want to save the STIX files
   - Example: "Where would you like me to save the generated STIX files?"
   - Default to current directory if no preference is given

2. **File Naming**
   - Use descriptive names: `[provider]-[threat]-[date].json`
   - Example: `aws-s3-bucket-vulnerability-2025-04-29.json`
   - Keep filenames clear and specific to the content

3. **File Size Management**
   - Keep files under 500KB when possible
   - Split into separate files if content becomes too large
   - Create separate files for different threat components when appropriate

4. **Separate Files When Needed**
   - Create separate files for different cloud providers
   - Split attack patterns and vulnerabilities if complex
   - Use separate files for different aspects of complex threats

5. **Report Files**
   - Save human-readable reports as markdown (.md) files
   - Use matching names: `[provider]-[threat]-report-[date].md` 
   - Include visualizations in the report files

## Implementation

When ready to save files:
1. Ask: "Where would you like me to save these STIX files?"
2. Create descriptive filenames based on content
3. Write files to the specified location
4. If files would be very large, suggest splitting them
5. Confirm successful file creation with the user
