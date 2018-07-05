#!/bin/bash
set -x 

query=$1
NP='16'
name=$2
output='./output_'$name'/'
final='./data_'$name'/'
remote_directory='/mnt/lustre/rfilguei/dch/BritishLibraryBooks'
local_directory='/mnt/lustre/rfilguei/BritishLibraryBooks'

rm -rf $output
rm -rf $final

mkdir $output
mkdir $final


for i in $remote_directory/15*; do
  if [ -d "$i" ]; then
	year=${i##*/}
	path=$local_directory'/'$year
	rpath=$remote_directory'/'$year'/*'
	mkdir $path
	cp $rpath $path'/.'
	outputpath=$output
	outputpath+="out_"$year
        echo $NP $query $path $outputpath
	mrun ./run_query.sh $NP $query $path $outputpath
	rm -rf $path
    
  fi
done



python join_$name'.py' $output $NP
python result_$name'.py' $output $final
