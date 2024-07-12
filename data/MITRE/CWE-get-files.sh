#!/bin/bash

cd CWE

wget https://cwe.mitre.org/data/csv/699.csv.zip
wget https://cwe.mitre.org/data/csv/1194.csv.zip
wget https://cwe.mitre.org/data/csv/1000.csv.zip

unzip 699.csv.zip
unzip 1194.csv.zip
unzip 1000.csv.zip

rm 699.csv.zip
rm 1194.csv.zip
rm 1000.csv.zip

mv 699.csv CWE-Software-Development-699.csv
mv 1194.csv CWE-Hardware-Design-1194.csv 
mv 1000.csv CWE-Research-Concepts-1000.csv

../../../file-utils/convert-CSVTOJSON.py CWE-Software-Development-699.csv CWE-Software-Development-699.json
../../../file-utils/convert-CSVTOJSON.py CWE-Hardware-Design-1194.csv CWE-Hardware-Design-1194.json
../../../file-utils/convert-CSVTOJSON.py CWE-Research-Concepts-1000.csv CWE-Research-Concepts-1000.json
