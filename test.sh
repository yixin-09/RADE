#!/bin/bash
cd benchmark/gsl
./clean.sh
./gen25.sh
cd ../../src
python gen_drivers.py
python RADE_test.py $1 $2
python DEMC_test.py $1 $2
