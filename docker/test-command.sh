#!/bin/sh
set -e

# Run Pytest with coverage
pytest --cov -vv \
	--cov-report term-missing:skip-covered \
	--cov-report json:cov.json

# Get Pytest coverage score
COVERAGE=$(jq '.totals.percent_covered' < cov.json)

# Set COVERAGE_THRESHOLD if not set
if [ -z "$COVERAGE_THRESHOLD" ]; then
	COVERAGE_THRESHOLD='75'
fi

# Fail if coverage is below threshold
FAILED=$(awk "BEGIN {print ($COVERAGE < $COVERAGE_THRESHOLD)}")
if [ "$FAILED" = "1" ]; then
	COVERAGE_DISPLAY=$(jq -r '.totals.percent_covered_display' < cov.json)
	echo "Coverage of $COVERAGE_DISPLAY% is below threshold of $COVERAGE_THRESHOLD%" >&2 # stderr
	exit 1
fi
