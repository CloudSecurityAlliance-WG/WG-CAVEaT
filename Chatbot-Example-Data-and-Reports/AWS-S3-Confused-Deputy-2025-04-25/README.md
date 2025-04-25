# AWS S3 Confused Deputy Vulnerability - STIX Documentation

This directory contains STIX 2.1 formatted data about the AWS S3 "Confused Deputy" vulnerability pattern.

## Files Included

1. `attack-pattern.json` - STIX Attack Pattern object describing the confused deputy vulnerability
2. `vulnerability.json` - STIX Vulnerability object with details about the security issue
3. `course-of-action.json` - STIX Course of Action object describing mitigation strategies
4. `relationship.json` - STIX Relationship objects connecting the different STIX objects
5. `identity.json` - STIX Identity object for AWS (as the affected platform)
6. `indicator.json` - STIX Indicator object with detection pattern for vulnerable configurations

## Overview

The "confused deputy" problem is a specific type of security vulnerability where a service (the "deputy") with legitimate permissions can be manipulated by a third party to access resources in unintended ways. In AWS S3, this commonly occurs in cross-account scenarios where bucket policies are not properly restricted with context-checking condition keys such as `aws:SourceArn` and `aws:SourceAccount`.

## Date

Created: April 25, 2025
