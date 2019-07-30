#!/bin/bash
cd build/html
rm -rf !(_static)
cd ../..
make html
