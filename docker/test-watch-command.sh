#!/bin/sh
set -e

if [ -n "$TESTMON_DATAFILE" ]; then
	# Create directory for pytest testmon data file
	mkdir -p "$(dirname $TESTMON_DATAFILE)"
fi

# Run Pytest with Testmon and coverage
PYTEST_RUNNER="\
pytest --testmon --cov -vv \
--cov-report term-missing:skip-covered \
--cov-report json:cov.json \
"

# Run Pytest Watch using configured Pytest runner
pytest-watch --runner "$PYTEST_RUNNER"
