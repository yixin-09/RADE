#!/usr/bin/zsh
rm -rf GSL
rm -rf gsl-2.5
tar -xf gsl-2.5.tar.gz
cd gsl-2.5
make clean
./configure --prefix=/home/projects/RADE/benchmark/gsl/GSL25 CFLAGS="-g -O2"
make -j4
make install
cd ..
mv GSL25 GSL
cp -r driver_template driver_functions

