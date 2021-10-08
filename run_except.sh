#!/bin/bash
source /opt/conda/etc/profile.d/conda.sh


dir='/home/jovyan/python_best_practices/'
script='exceptions_handled.py'
input='counties_data.csv'
col_num='two'

python $dir$script $dir$input $col_num > results.txt 2> results.err

echo Exit Code: $?