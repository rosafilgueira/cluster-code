import glob
import yaml
import sys
diseases=set([
        'cholera',
        'tuberculosis',
        'consumption',
        'phthisis',
        'typhoid',
        'whooping',
        'measles',
        'typhus',
        'smallpox',
        'diarrhoea',
        'dysentry',
        'diphtheria',
        'cancer'
        ])

inputpath=sys.argv[1]

final_files = sorted([f for f in glob.glob(inputpath+'/final*')])
year_data = {}

for f in final_files:
    with open(f, 'r') as stream:
        try:
            year_data[f]=yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)


d_total={}

for y in year_data:
	for d in diseases:
            try:
	        if d not in d_total:
			d_total[d]=year_data[y][d]
	        else:
			d_total[d].update(year_data[y][d])
            except:
                pass


outputpath=sys.argv[2]

for d in d_total:
	print ("dissease %s: %s\n" %(d,d_total[d]))
	name_file=outputpath+d+".yml"
        with open(name_file, 'w') as outfile:
		outfile.write('%s: ' % d)
                yaml.dump(d_total[d], outfile)
		print "wrote"
