#!/bin/bash

NP=$1
query=$2
corpus=$3
output=$4

echo $query
echo $corpus
echo $output

mpirun -np $NP python query.py $query $corpus --outpath=$output
