'''
Elementary comparison of keys and values of a YAML file.

Usage:

    python compare.py \
        results/data_diseases/consumption.yml \
        visualisations/diseases/data/consumption_ucl.yml
'''

import sys
import yaml

def compare_keys(file1, data1, file2, data2):
    keys1 = data1.keys()
    keys2 = data2.keys()
    diff = [key for key in keys1 if key not in keys2]
    if len(diff) != 0:
        print("Key-values in %s only:" % file1)
        for key in diff:
            print("%10s: %10s" % (key, data1[key]))


def compare_values(file1, data1, file2, data2):
    keys1 = data1.keys()
    keys2 = data2.keys()
    for key in keys1:
        if (key not in keys2):
            continue
        if data1[key] != data2[key]:
            print("Different value for key: %10s: %10s %10s" % 
                (key, data1[key], data2[key]))


file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as f:
    data1 = yaml.load(f)
with open(file2, "r") as f:
    data2 = yaml.load(f)

compare_keys(file1, data1, file2, data2)
compare_keys(file2, data2, file1, data1)

keys1 = data1.keys()
keys2 = data2.keys()
for key in keys1:
    if key not in keys2:
        continue
    value1 = data1[key]
    value2 = data2[key]
    if type(value1) is list and type(value2) is list:
        if value1 != value2:
            print("Different value for key: %10s" % key)
            print("%s" % value1)
            print("%s" % value2)
    else:
        keys1 = value1.keys()
        keys2 = value2.keys()
        compare_keys(file1, value1, file2, value2)
        compare_keys(file2, value2, file1, value1)
        compare_values(file1, value1, file2, value2)
