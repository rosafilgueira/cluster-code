#!/bin/bash
set -x 

query=$1
NP='16'
name=$2
output='./output_'$name'/'
final='./data_'$name'/'
remote_directory='/mnt/lustre/'$USER'/dch/BritishLibraryBooks'

rm -rf $output
rm -rf $final

mkdir $output
mkdir $final

for i in $remote_directory/*; do
  if [ -d "$i" ]; then
	path=$i
	outputpath=$output
	year=${i##*/}
	outputpath+="out_"$year
        echo $NP $query $path $outputpath
        mrun ./run_query.sh $NP $query $path $outputpath
  fi
done

python join_$name'.py' $output $NP
python result_$name'.py' $output $final
