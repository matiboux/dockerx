#!/bin/sh
set -e

if [ -n "$TESTMON_DATAFILE" ]; then
	# Create directory for pytest testmon data file
	mkdir -p "$(dirname $TESTMON_DATAFILE)"
fi

# Run Pytest using Pytest Watch & Testmon with coverage
pytest-watch --runner "pytest --testmon --cov --cov-report term-missing:skip-covered --cov-report json:cov.json -vv"
