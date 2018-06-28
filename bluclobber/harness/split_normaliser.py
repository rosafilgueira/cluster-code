import glob
import yaml
import sys

inputpath=sys.argv[1]
outputpath=sys.argv[2]
final_files = sorted([f for f in glob.glob(inputpath+'/final*')])
year_data = {}

for f in final_files:
    with open(f, 'r') as stream:
        try:
            year_data[f]=yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)



for y in year_data:
	print (" year %s \n" %y)
	name_file=outputpath+"normaliser.yml"
        with open(name_file, 'a+') as outfile:
                yaml.dump(year_data[y], outfile)
		print "wrote"
