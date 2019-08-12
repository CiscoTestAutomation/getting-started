#!/bin/bash
rm -r build
make html
cp theme.css source/build/html/_static/css
cp custom.css source/build/html/_static/css
