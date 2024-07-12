#!/bin/bash

cd FIGHT

rm fight.yaml
wget https://fight.mitre.org/fight.yaml

../../../file-utils/convert-YAMLToJSON.py fight.yaml  fight.json

