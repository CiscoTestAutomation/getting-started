# pyATS Getting Started Guide

This is the pyATS getting started guide and development guide source code.
The content of this repository, once reviewed and approved, is published on Cisco 
DevNet @ https://developer.cisco.com/docs/pyats-getting-started/

Please note that this repository contains WORK IN PROGRESS. We cannot guarantee that the information is accurate until we publish the content to https://developer.cisco.com.

## Contributions


Everyone can contribute (open a PR) and/or open issues against the  
pyATS documentation in this GitHub repository.

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
