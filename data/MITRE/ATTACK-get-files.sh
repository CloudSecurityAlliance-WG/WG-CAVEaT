#!/bin/bash

cd ATTACK

echo "Manually check for latest files and update this"
echo "https://github.com/mitre-attack/attack-stix-data/tree/master/enterprise-attack"
echo "https://github.com/mitre-attack/attack-stix-data/tree/master/ics-attack"
echo "https://github.com/mitre-attack/attack-stix-data/tree/master/mobile-attack"


wget https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-15.1.json
wget https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/ics-attack/ics-attack-15.1.json
wget https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/mobile-attack/mobile-attack-15.1.json
