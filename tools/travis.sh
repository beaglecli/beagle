#!/bin/bash
#
# Run the build mode specified by the BUILD variable, defined in
# .travis.yml. When the variable is unset, assume we should run the
# standard test suite.

rootdir=$(dirname $(dirname $0))

# Show the commands being run.
set -x

# Exit on any error.
set -e

case "$BUILD" in
    docs)
        python setup.py sdist
        sphinx-build -a -E -W -b html doc/source doc/build/html;;
    linter)
        flake8;;
    *)
        pytest -v \
               --cov=beagle \
               --cov-report term-missing \
               --cov-config $rootdir/.coveragerc \
               $@;;
esac
