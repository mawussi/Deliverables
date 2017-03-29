#!/bin/bash                                                                                                                                             
#change txt extension by csv
for f in *.txt; do
    mv -- "$f" "${f%.txt}.csv"
done

find . -type f -name '*.csv' | while read FILE ; do
    #replace all spaces by a single  comma txt 2 cvs
    sed -e 's/\s\s*/,/g' ${FILE} > tmp1 ;
    #delete all white spaces
    grep '[^[:blank:]]' < tmp1 > tmp2
    # cut useful column Second and GFLOPS
    cut -d',' -f4,5  tmp2 > ${FILE}
done 
