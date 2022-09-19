#!/bin/bash
read -p "Enter the number of Highest-Occupied Band: " vbm
read -p "Enter the number of Highest-Occupied Band: " cbm
mvbm=`(echo 91;echo 912;echo ${vbm})|vaspkit|grep 'K-Path Index'|gawk '{print $(NF-1)}'`
mcbm=`(echo 91;echo 912;echo ${cbm})|vaspkit|grep 'K-Path Index'|gawk '{print $(NF-1)}'`
echo "        m1      m2" >../../mstar.dat
echo "m_vbm:" ${mvbm}>>../../mstar.dat
echo "m_cbm:" ${mcbm}>>../../mstar.dat
