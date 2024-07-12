#!/bin/bash

cd ATLAS

rm ATLAS.yaml
wget https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/ATLAS.yaml

../../../file-utils/convert-YAMLToJSON.py ATLAS.yaml ATLAS.json


