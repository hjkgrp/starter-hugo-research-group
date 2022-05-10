#!/bin/sh
mol="MnH"
for mag in 5 7; do
    echo $mol" spin is "$mag
    echo "          1E-40      1.0      2.0     3.0    4.0"
    for J in 1E-40 0.5 1.0 1.5 2.0; do
        printf $J
        for U in 1E-40 1.0 2.0 3.0 4.0; do 
            energy=`grep '! ' $mol.m$mag.U$U.J$J.out | awk '{ print $5 }'`
            if [ "$energy" == "" ]; then
               printf " 100000"
            else
               printf " $energy"
            fi
        done
        echo " "
    done    
done
