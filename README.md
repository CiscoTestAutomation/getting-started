# pyATS User Guide

This is the pyATS development user guide repository. 

## Requirements

Sphinx: https://www.sphinx-doc.org/en/master/


## Installation

```bash
# requires a python3.6+ environment (any virtual environment or system Python)
cd ~/pyats

# clone this repo
git clone ssh://git@bitbucket-eng-sjc1.cisco.com:7999/pyats-core/userguide.git

# install the required dependencies
pip install -r userguide/requirement.txt

```

And you're good to go.

## Directory Structure:

```text

source/             folder where all sources are. 
source/index.rst    main entry point

build/              where the output built HTML is

```


## To Run

```bash

# build html
make html

# open the built files
open ./build/html/index.html

```