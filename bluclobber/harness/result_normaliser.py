import yaml
import sys

inputpath=sys.argv[1]
inputfile=inputpath+'joined_normaliser.yml'
year_data = {}
myList = []


def pattern_value(value):
	value_s=value.split(",")
	element1=value_s[0].split("[")[1]
	element2=value_s[1]
	element3=value_s[2].split("]")[0]
	return element1,element2,element3


def aggregation_elements(element1, element2):
	return int(element1) + int(element2)

def add_values(value1, value2):
	
	v1_element1, v1_element2, v1_element3 = pattern_value(value1)	
	v2_element1, v2_element2, v2_element3 = pattern_value(value2)
	v3_element1=aggregation_elements(v1_element1, v2_element1)
	v3_element2=aggregation_elements(v1_element2, v2_element2)
	v3_element3=aggregation_elements(v1_element3, v2_element3)
	data= " ["+str(v3_element1)+", "+str(v3_element2)+", "+str(v3_element3)+"]\n"
	return data

with open(inputfile, 'r') as fp:
    for line in fp:
	line_s=line.split(":")
	year=line_s[0]
	value=line_s[1]
	if year not in year_data:
		year_data[year]=value
	else:
		year_data[year]=add_values(year_data[year],value)

outputpath=sys.argv[2]
name_file=outputpath+"./normaliser.yml"
for y in year_data:
        with open(name_file, 'a+') as outfile:
                outfile.write('%s: %s' %(y,year_data[y]))


