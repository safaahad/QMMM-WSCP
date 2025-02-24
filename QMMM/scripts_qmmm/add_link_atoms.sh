#!/bin/bash
filename=$(echo 2_*_md_*.g96)
number=$(echo $filename | sed -r 's/.*_([0-9]*)\..*/\1/g') 

sed '/  977 ASP   N /i\  1    LA   LA         1    0.000000000    0.000000000    0.000000000' $filename > temp.g96
wait
sed '/ 1709 CLA   MG/i\  2    LA   LA         2    0.000000000    0.000000000    0.000000000' temp.g96 > 3_added_la_md_$number.g96
