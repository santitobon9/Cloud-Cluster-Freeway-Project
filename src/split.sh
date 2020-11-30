#!/bin/bash
FNAME=freeway_loopdata.csv
HEADER=$(head -1 $FNAME)
split -b 300m $FNAME sections
n=1
for f in sections*
do
     if [ $n -gt 1 ]; then 
          echo $HEADER > part${n}.csv
     fi
     cat $f >> part${n}.csv
     rm $f
     ((n++))
done
