#!/bin/bash
set -x 

query=$1
NP='4'
output='./output/'
final='./data/'
remote_directory='/mnt/lustre/rfilguei/dch/BritishLibraryBooks'

rm -rf $output
rm -rf $final

mkdir $output
mkdir $final

for i in $remote_directory/1*; do
  if [ -d "$i" ]; then
	path=$i
	outputpath=$output
	year=${i##*/}
	outputpath+="out_"$year
        echo $NP $query $path $outputpath
        ./run_query.sh $NP $query $path $outputpath
    
  fi
done

python join.sh $NP
python split.sh $output $final


