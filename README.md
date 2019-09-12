# pyATS Getting Started Guide

This is the pyATS getting started guide source code.
The content of this repository is published on Cisco 
DevNet @ https://developer.cisco.com/docs/pyats-getting-started/

## Contributions

Everyone is welcomed to contribute (open PR) and/or open issues against the  
pyATS getting started guide in this GitHub repository.

Your changes will be reviewed, and once merged, the main hosted documentation
will be updated.

## Installation

```bash
# requires a python3.6+ environment (any virtual environment or system Python)
cd ~/pyats

# clone this repo
git clone https://github.com/CiscoTestAutomation/getting-started/

# install the required dependencies
pip install -r getting-started/requirement.txt

```

And you're good to go.

## Directory Structure:

```text

source/             folder where all sources are. 
source/index.rst    main entry point

build/              where the output built HTML is

```


## To Build Local docs

```bash

# build html
make html

# open the built files
open ./build/html/index.html

```
