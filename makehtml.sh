#!/bin/bash
rm -r build
make html
cp theme.css build/html/_static/css
cp custom.css build/html/_static/css
