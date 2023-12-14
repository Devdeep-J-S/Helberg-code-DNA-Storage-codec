#!/bin/bash

# Run the Python script with arguments n, q, s

rm output.txt
touch output.txt

for i in {3..7}; do
    for j in {5..5}; do
        for k in {2..2}; do
            py 'helberg copy 2.py' $i $j $k
        done
    done
done
