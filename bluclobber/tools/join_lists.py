'''
Given a directory of YAML documents, each assumed to be of form:

    [INTEGER, INTEGER]
    ...

(i.e. a list of two integer values) and an output file name, read each
file, pairwise sum each values and output the list of total (a
two-element list) as a YAML document into the output file name.

Copyright (c) 2018 The University of Edinburgh.
'''

import os
import os.path
import sys
import yaml
from operator import add

data_dir = sys.argv[1]
output_file = sys.argv[2]

yml_files = os.listdir(data_dir)
yml_files.sort()
totals = None
for yml_file in yml_files:
    print("Reading: %s" % yml_file)
    with open(os.path.join(data_dir, yml_file), "r") as f:
        values = yaml.load(f)
        if totals == None:
            totals = values
        else:
            totals = list(map(add, totals, values))
print("Writing: %s" % output_file)
with open(output_file, "w") as f:
    yaml.dump(totals, f)
