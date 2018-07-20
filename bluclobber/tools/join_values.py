'''
Given a directory of YAML documents, each assumed
to be of form:

    INTEGER
    ...

(i.e. a single integer value) and an output file
name, read each file, sum the values and output
the total as a YAML document into the output file
name.

Copyright (c) 2018 The University of Edinburgh.
'''

import os
import os.path
import sys
import yaml

data_dir = sys.argv[1]
output_file = sys.argv[2]

yml_files = os.listdir(data_dir)
yml_files.sort()
total = 0
for yml_file in yml_files:
    print("Reading: %s" % yml_file)
    with open(os.path.join(data_dir, yml_file), "r") as f:
        total += yaml.load(f)
print("Writing: %s" % output_file)
with open(output_file, "w") as f:
    yaml.dump(total, f)
