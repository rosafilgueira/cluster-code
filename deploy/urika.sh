#!/bin/bash
set -x 

NP='4'
query=$1
output='./output/'
remote_directory='/mnt/lustre/rfilguei/dch/BritishLibraryBooks'

for i in $remote_directory/1*; do
  if [ -d "$i" ]; then
	echo $i
	path=$i
	outputpath=$output
	year=${i##*/}
	outputpath+="out_"$year
	echo $outputpath
        ./run_query.sh $NP $query $path $outputpath
    
  fi
done

python join.sh $NP
python split.sh


