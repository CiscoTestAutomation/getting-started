# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build/

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help started


start:
	@$(SPHINXBUILD) -M html "start-guide" "build/start-guide/" $(SPHINXOPTS) $(O)

develop:
	@$(SPHINXBUILD) -M html "develop-guide" "build/develop-guide/" $(SPHINXOPTS) $(O)

clean:
	@rm -rf build

html: start develop
	