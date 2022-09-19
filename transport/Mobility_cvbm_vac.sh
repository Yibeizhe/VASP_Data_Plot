#!/bin/bash
#------How to use
# Script name potentialConstantE1.sh
# Put this script in your optimizing structure directory
# The mobility-x and mobility-y directories should be 
# under the optimizing structure directory
#-------end
echo "The current directory is: "
pwd
echo "Structure: "
stru=`pwd|gawk -F/ '{print $NF}'`
echo $stru
for z in x y
do
cd mobility-${z}
#Use vaspkit to produce the BAND_GAP file
 for i in [10]*
do echo $i
cd $i/scf/band
(echo 21;echo 211)|vaspkit
cd ../../../
done

# Obtain the band structure of the stained structure
printf "%-12s%-20s%-12s%-12s%-12s\n" strain  energy  vbm  cbm  vacuum-level >../E1_${z}.dat
for i in [10]*
do
cd $i/scf/band
# Obtain VBM and CBM value
vbm=`sed -n '4p' BAND_GAP|gawk '{print $NF}'`
cbm=`sed -n '5p' BAND_GAP|gawk '{print $NF}'`
# Get the Vacuum level from the scf directory
# This need to add LVHAR = .TRUE. to INCAR file
cd ..
vac=`(echo 42;echo 426;echo 3)|vaspkit|grep 'Vacuum-Level (eV)'|gawk -F: '{print $NF}'`
en=`grep entropy OUTCAR | tail -1|gawk '{print $NF}'`
echo "strain  energy  vbm  cbm  vacuum-level"
printf "%-12s%-20s%-12s%-12s%-12s\n" ${i}  ${en}  ${vbm}  ${cbm}  ${vac}
printf "%-12s%-20s%-12s%-12s%-12s\n" ${i}  ${en}  ${vbm}  ${cbm}  ${vac}>>../../../E1_${z}.dat
cd ../..
done
echo "The strain, vbm, cbm and vacuum level values have been written to the E1_${z}.dat file"
echo "And the content of E1_${z}.dat file is as following:"
cat ../E1_${z}.dat 
read -p "Enter 1 to continue plot bandstructure, others quit: " band1
if [ $band1 -eq 1 ]
then
for i in [01]*
do
cd $i/scf/band

BandPlot.py
cp band.png ../../../${stru}_${z}_${i}_band.png
cd ../../..
done

else
echo "Good bye"
fi

cd ..
done
