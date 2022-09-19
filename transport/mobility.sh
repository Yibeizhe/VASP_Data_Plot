#!/bin/bash
#To use it: bash mobility.sh
mkdir mobility-x
cp CONTCAR mobility-x/POSCAR
cp KPOINTS POTCAR INCAR mobility-x
cp Opt2dScfBandv544.bsub mobility-x
cd mobility-x
cat >OPTCELL <<EOF
000
010
000
EOF
x=`gawk 'NR==3{print $1}' POSCAR`            #"x" stands for the lattice constant in x direction
for i in $(seq 0.994 0.002 1.006)                #"i" defines the range of strain
do
mkdir $i
cp OPTCELL POSCAR KPOINTS POTCAR INCAR Opt2dScfBandv544.bsub $i                               #"IS-x" stands for the origin file 
cd $i
sed -i "3s/$x/$(echo "$x*$i"|bc)/g" POSCAR
#bsub Opt2dScfBandv544.bsub
cd ..
done
rm KPOINTS POTCAR INCAR POSCAR OPTCELL Opt2dScfBandv544.bsub
cd ../
mkdir mobility-y
cp CONTCAR mobility-y/POSCAR
cp KPOINTS POTCAR INCAR mobility-y
cp Opt2dScfBandv544.bsub mobility-y
cd mobility-y
cat >OPTCELL <<EOF
100
000
000
EOF
y=`gawk 'NR==4{print $2}' POSCAR`                #"y" stands for the lattice constant in y direction
for j in $(seq 0.994 0.002 1.006)                #"j" defines the range of strain
do
mkdir $j
cp OPTCELL POSCAR KPOINTS POTCAR INCAR Opt2dScfBandv544.bsub $j
cd $j
sed -i "4s/$y/$(echo "$y*$j"|bc)/g" POSCAR
#bsub Opt2dScfBandv544.bsub
cd ..
done
rm KPOINTS POTCAR INCAR POSCAR OPTCELL Opt2dScfBandv544.bsub
cd ..

