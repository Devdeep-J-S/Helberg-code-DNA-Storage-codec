#!/bin/bash

# Run the Python script with arguments n, q, s

rm output.txt
touch output.txt

for i in {4..4}; do
    for j in {2..5}; do
        for k in {1..1}; do
            py helberg.py $i $j $k
        done
    done
done
