#!/bin/bash
cd build/html/_static/css
cp theme.css ../../../../
cp custom.css ../../../../
cd ../../../
rm -rf *
cd ..
make html
cp theme.css build/html/_static/css
cp custom.css build/html/_static/css
