import sys
import os

#file_year=["1800_1809", "1820_1829","1830_1839", "1840_1849", "1850_1859", "1860_1869", "1870_1879", "1880_1889"]
file_year=["1890_1899"]
path = "./output/"
import shutil

np= sys.argv[1]

for i in file_year:
	filename=path+"out_"+i
	outfilename=path+"final_"+i+".yml"
	with open(outfilename, 'wb') as outfile:
		for k in range(int(np)):
			filename_f=filename+"_"+str(k)+".yml"
        		with open(filename_f, 'rb') as readfile:
            			shutil.copyfileobj(readfile, outfile)

