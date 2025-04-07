# STIX 2.1 Validation Guide: Best Practices and Tools

## Introduction

Structured Threat Information Expression (STIX) is a standardized language for cyber threat intelligence. Proper validation of STIX files ensures that they conform to the specification and can be correctly interpreted by other systems. This guide covers practical approaches for validating STIX 2.1 files, including examples, common issues, and recommended tools.

## Understanding STIX 2.1 Structure

STIX 2.1 content typically consists of:

1. **STIX Domain Objects (SDOs)**: Attack patterns, vulnerabilities, courses of action, etc.
2. **STIX Relationship Objects (SROs)**: Relationships connecting SDOs
3. **STIX Cyber-observable Objects (SCOs)**: Technical elements like IP addresses, files, etc.
4. **STIX Bundles**: Containers for collecting multiple STIX objects

STIX objects are serialized as JSON, and validation ensures that:
- Required properties are present
- Property values have the correct data types
- Objects conform to structural rules defined in the specification

## Understanding STIX Bundle Structure

A STIX bundle is a container that packages multiple STIX objects together:

```json
{
  "type": "bundle",
  "id": "bundle--uuid-here",
  "spec_version": "2.1",
  "objects": [
    {
      "type": "attack-pattern",
      "spec_version": "2.1",
      "id": "attack-pattern--uuid-here",
      "created": "2025-01-01T00:00:00.000Z",
      "modified": "2025-01-01T00:00:00.000Z",
      // other attack pattern properties
    },
    {
      "type": "vulnerability",
      "spec_version": "2.1",
      "id": "vulnerability--uuid-here",
      "created": "2025-01-01T00:00:00.000Z",
      "modified": "2025-01-01T00:00:00.000Z",
      // other vulnerability properties
    }
    // more objects
  ]
}
```

Key points about bundles:
- A bundle has its own `id` and `spec_version`
- The `objects` array contains individual STIX objects
- Each object within the bundle must be valid according to its own object schema

## Common Validation Issues

### 1. Missing Required Properties

Each STIX object type has required properties. Common missing properties include:

- **For all objects**: `type`, `id`, `spec_version`, `created`, `modified`
- **For specific types**: `name`, `description`, `pattern` (for indicators), etc.

Example of a valid attack pattern:

```json
{
  "type": "attack-pattern",
  "spec_version": "2.1",
  "id": "attack-pattern--0c7b5b88-8ff7-4a4d-aa9d-feb398cd0061",
  "created": "2025-01-01T00:00:00.000Z",
  "modified": "2025-01-01T00:00:00.000Z",
  "name": "Spearphishing Attachment",
  "description": "Adversaries may send spearphishing emails with a malicious attachment."
}
```

### 2. Incorrect Property Types

Properties must have values of the correct data type:

- Timestamps must be valid RFC3339 formatted strings
- IDs must follow the correct format (typically `type--UUID`)
- Lists must be arrays, not single objects
- References must point to valid STIX objects

### 3. Invalid Bundle Structure

Bundles themselves must be validated against the bundle schema:

- The top-level `type` must be "bundle"
- The bundle must have its own `id` (format: `bundle--UUID`)
- The bundle must have a `spec_version` property
- The `objects` property must be an array of STIX objects

### 4. Custom Properties

Custom properties (extensions to the standard) must follow naming conventions:

- Must begin with "x_" followed by a source unique identifier (like `x_caveat_extension`)
- Must contain only allowed characters 
- Should be documented clearly

## Validation Approaches

### 1. Schema-Based Validation

JSON Schema validation checks if STIX objects conform to their defined schemas.

#### Using Python with the `jsonschema` package:

```python
import json
import jsonschema
from jsonschema import validate

# Load a schema
with open("path/to/schemas/common/bundle.json") as schema_file:
    bundle_schema = json.load(schema_file)

# Load STIX content
with open("path/to/your/stix-bundle.json") as stix_file:
    stix_content = json.load(stix_file)

# Validate bundle structure
try:
    validate(instance=stix_content, schema=bundle_schema)
    print("Bundle validation successful")
except jsonschema.exceptions.ValidationError as e:
    print(f"Bundle validation failed: {e}")

# For more detailed validation, extract each object and validate against its type-specific schema
for obj in stix_content.get("objects", []):
    obj_type = obj.get("type")
    if obj_type:
        try:
            with open(f"path/to/schemas/sdos/{obj_type}.json") as obj_schema_file:
                obj_schema = json.load(obj_schema_file)
            validate(instance=obj, schema=obj_schema)
            print(f"Object {obj.get('id')} validation successful")
        except FileNotFoundError:
            print(f"Schema for {obj_type} not found")
        except jsonschema.exceptions.ValidationError as e:
            print(f"Object {obj.get('id')} validation failed: {e}")
```

#### Using `ajv` (Command Line):

```bash
# Install ajv
npm install -g ajv-cli

# Validate bundle
ajv validate -s path/to/schemas/common/bundle.json -d path/to/your/stix-bundle.json

# For more complex validation of objects inside the bundle
jq '.objects[] | select(.type=="attack-pattern")' path/to/your/stix-bundle.json > attack-patterns.json
ajv validate -s path/to/schemas/sdos/attack-pattern.json -d attack-patterns.json
```

### 2. Using Existing Validation Tools

#### Using the `stix2-validator` Python package:

```bash
# Install the validator
pip install stix2-validator

# Basic validation
stix2_validator path/to/your/stix-bundle.json

# With options
stix2_validator --strict --silent path/to/your/stix-bundle.json
```

#### Using custom scripts:

```bash
# Example with a custom validation script
./validate-json-schema.py --input path/to/your/stix-bundle.json --schema path/to/schemas/common/bundle.json
```

## Advanced Validation Techniques

### 1. Two-Stage Validation

For thorough validation, use a two-stage approach:

1. **Structural validation**: Ensure JSON structure and required properties are present
2. **Semantic validation**: Check that values make logical sense (e.g., 'modified' timestamp is not before 'created')

Example script for two-stage validation:

```python
import json
import jsonschema
import datetime

def validate_stix_bundle(bundle_file, schema_dir):
    """Validate a STIX bundle file using a two-stage approach."""
    # Load the bundle
    with open(bundle_file) as f:
        bundle = json.load(f)
    
    # Stage 1: Structural validation
    with open(f"{schema_dir}/common/bundle.json") as f:
        bundle_schema = json.load(f)
    
    try:
        jsonschema.validate(bundle, bundle_schema)
        print("Stage 1: Bundle structure validation passed")
    except jsonschema.exceptions.ValidationError as e:
        print(f"Stage 1: Bundle structure validation failed: {e}")
        return False
    
    # Stage 2: Object-specific validation and semantic checks
    for obj in bundle.get("objects", []):
        obj_type = obj.get("type")
        if obj_type in ["relationship", "sighting"]:
            schema_path = f"{schema_dir}/sros/{obj_type}.json"
        else:
            schema_path = f"{schema_dir}/sdos/{obj_type}.json"
        
        try:
            with open(schema_path) as f:
                obj_schema = json.load(f)
            jsonschema.validate(obj, obj_schema)
            print(f"Stage 2a: {obj.get('id')} structure validation passed")
            
            # Semantic validation checks
            if "created" in obj and "modified" in obj:
                created = datetime.datetime.fromisoformat(obj["created"].replace("Z", "+00:00"))
                modified = datetime.datetime.fromisoformat(obj["modified"].replace("Z", "+00:00"))
                if modified < created:
                    print(f"Stage 2b: Semantic validation failed for {obj.get('id')}: 'modified' is before 'created'")
                    return False
            
            if obj_type == "relationship":
                # Check that source_ref and target_ref exist
                if "source_ref" not in obj or "target_ref" not in obj:
                    print(f"Stage 2b: Semantic validation failed for {obj.get('id')}: missing source_ref or target_ref")
                    return False
                
                # Check circular references
                if obj.get("source_ref") == obj.get("target_ref"):
                    print(f"Stage 2b: Semantic validation failed for {obj.get('id')}: circular reference")
                    return False
            
            print(f"Stage 2b: {obj.get('id')} semantic validation passed")
            
        except FileNotFoundError:
            print(f"Schema for {obj_type} not found at {schema_path}")
            return False
        except jsonschema.exceptions.ValidationError as e:
            print(f"Stage 2a: {obj.get('id')} structure validation failed: {e}")
            return False
    
    return True
```

### 2. Batch Validation

For validating multiple files at once:

```bash
#!/bin/bash
# Validate all STIX bundles in a directory

SCHEMA_DIR="path/to/schemas"
STIX_DIR="path/to/stix/files"

for file in $STIX_DIR/*.json; do
    echo "Validating $file..."
    
    # Validate bundle structure
    ajv validate -s $SCHEMA_DIR/common/bundle.json -d $file
    if [ $? -ne 0 ]; then
        echo "Bundle validation failed for $file"
        continue
    fi
    
    # Extract and validate objects by type (example for attack patterns)
    jq '.objects[] | select(.type=="attack-pattern")' $file > temp_attack_patterns.json
    if [ -s temp_attack_patterns.json ]; then
        ajv validate -s $SCHEMA_DIR/sdos/attack-pattern.json -d temp_attack_patterns.json
        if [ $? -ne 0 ]; then
            echo "Attack pattern validation failed in $file"
        fi
    fi
    
    # Add similar blocks for other object types
    
    rm temp_*.json
done
```

## Common Errors and Solutions

### Error: 'created' is a required property

This error occurs when validating an object without a required 'created' property.

**Solution**: Add the missing property to each object:

```bash
# Using jq to add created field to objects missing it
jq '.objects = [.objects[] | if .created == null then . + {"created": "2025-04-07T00:00:00.000Z"} else . end]' stix-bundle.json > fixed-bundle.json
```

### Error: 'spec_version' is a required property

This can occur at the bundle level or the object level.

**Solution**: Add the missing spec_version:

```bash
# For the bundle itself
jq '. += {"spec_version": "2.1"}' stix-bundle.json > fixed-bundle.json

# For objects within the bundle
jq '.objects = [.objects[] | if ."spec_version" == null then . + {"spec_version": "2.1"} else . end]' stix-bundle.json > fixed-bundle.json
```

### Error: Invalid ID format

STIX IDs must follow the pattern `type--UUID`.

**Solution**: Fix malformed IDs:

```bash
# Generate a proper UUID-based ID
uuid=$(uuidgen)
jq --arg uuid "$uuid" --arg type "attack-pattern" '.objects[0].id = ($type + "--" + $uuid)' stix-bundle.json > fixed-bundle.json
```

### Error: Invalid timestamp format

STIX timestamps must be in RFC3339 format.

**Solution**: Format timestamps correctly:

```bash
# Fix timestamp format
jq '.objects[0].created = "2025-04-07T00:00:00.000Z"' stix-bundle.json > fixed-bundle.json
```

## Best Practices for STIX Validation

1. **Validate incrementally during development**:
   - Validate individual objects before adding them to bundles
   - Use schema validation early and often in the development cycle

2. **Use multiple validation tools**:
   - Schema-based validation for structure
   - Custom validation for semantic requirements
   - Community tools for comprehensive checks

3. **Document custom extensions**:
   - Clearly document any custom properties (x_* properties)
   - Provide schemas for custom object types

4. **Maintain version consistency**:
   - All objects should use the same STIX spec version
   - Don't mix objects from different STIX versions in the same bundle

5. **Test interoperability**:
   - Validate that your STIX content works with common STIX tools
   - Test exchange of STIX data with partner systems

## Command Line Reference Guide

Here's a quick reference guide for common validation commands:

### Using JSON Schema Validator (ajv)

```bash
# Validate bundle structure
ajv validate -s schemas/common/bundle.json -d your-bundle.json

# Validate specific object types
# First extract objects of a specific type
jq '.objects[] | select(.type=="attack-pattern")' your-bundle.json > temp_ap.json
# Then validate
ajv validate -s schemas/sdos/attack-pattern.json -d temp_ap.json
```

### Using Python jsonschema

```bash
python -c '
import json, jsonschema
with open("schemas/common/bundle.json") as f: schema = json.load(f)
with open("your-bundle.json") as f: data = json.load(f)
jsonschema.validate(data, schema)
print("Validation successful")
'
```

### Using stix2-validator

```bash
# Basic validation
stix2_validator your-bundle.json

# With options
stix2_validator --strict --no-print-json --no-dependencies your-bundle.json
```

### Using jq for Preprocessing

```bash
# Fix common issues
jq '. += {"spec_version": "2.1"} | .objects = [.objects[] | if .created == null then . + {"created": "2025-04-07T00:00:00.000Z", "modified": "2025-04-07T00:00:00.000Z"} else . end]' your-bundle.json > fixed-bundle.json
```

## Conclusion

Proper validation of STIX content ensures interoperability and reliability of threat intelligence data. By using a combination of schema validation and semantic checks, you can ensure that your STIX bundles conform to the specification and will be correctly interpreted by other systems.

Remember that some specification requirements cannot be validated through JSON Schema alone. Implement additional validation logic for temporal relationships, references between objects, and other semantic constraints as needed.

