#!/usr/bin/zsh
gcc -c -I../../GSL/include -fPIC -emit-llvm gslsfdr.c
gcc -O2 -shared -fPIC -lm -o libgslbc.so gslsfdr.o ../../GSL/lib/libgsl.a -Wl,-rpath=.

rm *.o
