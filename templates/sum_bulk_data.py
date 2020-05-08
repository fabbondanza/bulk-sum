#!/usr/bin/python3

import csv
import glob
import os
import re

phenotype_field_indexes = []
participant_to_phenotypic_value = {}
phenotypic_data_headers = []

with open('$phenotypesFile') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  phenotypic_data_headers = next(reader, None)
  phenotype_field_index = phenotypic_data_headers.index('$phenotypicField')
  for row in reader:
    participant_to_phenotypic_value[row[0]] = float(row[phenotype_field_index])

participants = participant_to_phenotypic_value.keys()

for participant in participants:
  bulkFilesToCheck = glob.glob('./{}_{}.dat'.format(participant, '$bulkField'))
  if len(bulkFilesToCheck) == 0:
    participant_to_phenotypic_value[participant] = [participant_to_phenotypic_value[participant], '-', '-']
  for bulkFile in bulkFilesToCheck:
    readBulkFile = open(bulkFile, 'r')
    bulkFileValue = readBulkFile.readline().rstrip()
    participant_to_phenotypic_value[participant] = [participant_to_phenotypic_value[participant], bulkFileValue, participant_to_phenotypic_value[participant] * float(bulkFileValue)]

resultsFile = open('./bulk_sum.csv', 'w')

resultsFile.write('{}\\n'.format(','.join(['eid','phenotypeFieldValue','bulkFileValue','newValue'])))

for key, value in participant_to_phenotypic_value.items():
  resultsFile.write('{}\\n'.format(','.join([key, str(value[0]), str(value[1]), str(value[2])])))
