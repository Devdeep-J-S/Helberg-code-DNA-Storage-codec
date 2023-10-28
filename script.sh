#!/bin/bash

# Run the Python script with arguments n, q, s

rm output.txt
touch output.txt

for i in {4..10}; do
    for j in {2..2}; do
        for k in {2..5}; do
            py helberg.py $i $j $k
        done
    done
done
