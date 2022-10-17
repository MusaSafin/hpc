#!/bin/bash
#organize FOR loop printing the elements of array

arr=(0 1 2 3 4 5 6 7 8 9)
for i in `seq 1 ${#arr[@]}`; do
    echo ${arr[$i-1]}
done
