#!/bin/sh

# DockerX Version Bumper
# Wrapper for running docker programs & docker shell environments.
# https://github.com/matiboux/dockerx
# MIT License
# Copyright (c) 2024 Matiboux
# This project is not affiliated with Docker, Inc.

ERROR_CODE=''
DOCKERX_PARSE_ARGUMENTS='true'

# Parse options arguments
while [ "$DOCKERX_PARSE_ARGUMENTS" = 'true' ] && [ "$#" -gt 0 ]; do

	case "$1" in

		'--help' | '-h' )
			DOCKERX_PRINT_HELP='true'
			shift
			;;

		'--disable-git' | '-n' )
			DOCKERX_DISABLE_GIT='true'
			shift
			;;

		* )
			# Unknown option, maybe first argument
			# Stop parsing options
			break
			;;

	esac

done

if [ "$DOCKERX_PARSE_ARGUMENTS" = 'true' ]; then
	# Parse positional arguments

	# Parse version argument
	if [ "$#" -le 0 ] || [ -z "$1" ]; then
		echo 'Error: No version specified.' >&2
		DOCKERX_PRINT_HELP='true'
		ERROR_CODE=1
	fi
	DOCKERX_VERSION="$1"
	shift

fi

if [ "$DOCKERX_PRINT_HELP" = 'true' ]; then
	# Print help & exit
	echo "Usage: $0 [options] <version>"
	echo ''
	echo 'Options:'
	echo '  --help, -h         Display this help message'
	echo '  --disable-git, -n  Disable git'
	echo ''
	echo 'Arguments:'
	echo '  version  New version (e.g. 1.1.0)'
	exit ${ERROR_CODE:-0}
fi

# Get whether to use git
USE_GIT='true'
if [ "$DOCKERX_DISABLE_GIT" = 'true' ]; then
	# Disable git
	USE_GIT='false'
fi

if [ "$USE_GIT" = 'true' ]; then
	if [ ! -d './.git' ]; then
		# Directory is not a git repository
		USE_GIT='false'
	else
		# Check that git is installed
		git --version > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo 'Warning: Git is not installed.' >&2
			USE_GIT='false'
		fi
	fi
fi

# Get version from argument
VERSION="$DOCKERX_VERSION"

# Bump version in dockerx
if [ "$(uname -s)" = 'Darwin' ]; then
	# MacOS
	sed -i '' "3 s/\# DockerX.*/\# DockerX (v$VERSION)/g" ./dockerx
	sed -i '' "10 s/VERSION=.*/VERSION='$VERSION'/g" ./dockerx
else
	# Linux
	sed -i "3 s/\# DockerX.*/\# DockerX (v$VERSION)/g" ./dockerx
	sed -i "10 s/VERSION=.*/VERSION='$VERSION'/g" ./dockerx
fi

if [ "$USE_GIT" = true ]; then
	# Commit changes in git
	git add ./dockerx > /dev/null 2>&1
	git commit -m "Bump version to $VERSION" > /dev/null 2>&1
	if [ $? -ne 0 ]; then
		echo 'Warning: Failed to commit changes.' >&2
	else
		git tag -a "v$VERSION" -m "Bump version to $VERSION"
		echo "Info: Commited changes & tagged 'v$VERSION' in git" >&2
	fi
fi

echo "Version bumped to $VERSION!"
