import sys
import os

file_year=["1510_1699", "1700_1799", "1800_1809", "1810_1819", "1820_1829","1830_1839", "1840_1849", "1850_1859", "1860_1869", "1870_1879", "1880_1889", "1890_1899"]
import shutil
path= sys.argv[1]
np= sys.argv[2]
python join.py $output $NP
for i in file_year:
	filename=path+"out_"+i
	outfilename=path+"final_"+i+".yml"
	with open(outfilename, 'wb') as outfile:
		for k in range(int(np)):
			try:
				filename_f=filename+"_"+str(k)+".yml"
        			with open(filename_f, 'rb') as readfile:
            				shutil.copyfileobj(readfile, outfile)
			except:
				pass	

