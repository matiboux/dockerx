#!/bin/sh

# DockerX Version Bumper
# Wrapper for running docker programs & docker shell environments.
# https://github.com/matiboux/dockerx
# MIT License
# Copyright (c) 2024 Matiboux
# This project is not affiliated with Docker, Inc.

ERROR_CODE=''

# Parse arguments
# Dummy while loop to allow breaking
while true; do

	# Parse options arguments
	while [ "$#" -gt 0 ]; do

		case "$1" in

			'--help' | '-h' )
				# Print help
				DOCKERX_PRINT_HELP='true'
				shift
				;;

			'--disable-git' | '-n' )
				# Disable git support
				DOCKERX_DISABLE_GIT='true'
				shift
				;;

			* )
				break
				;;

		esac

	done

	if [ "$DOCKERX_PRINT_HELP" = 'true' ]; then
		# Stop parsing arguments
		break
	fi

	# Parse mandatory version positional argument
	if [ "$#" -le 0 ] || [ -z "$1" ]; then
		echo 'Error: No version specified.' >&2
		DOCKERX_PRINT_HELP='true'
		ERROR_CODE=1
		break
	fi
	DOCKERX_VERSION="$1"
	shift

	# Stop parsing arguments
	break

done

if [ "$DOCKERX_PRINT_HELP" = 'true' ]; then
	# Print help & exit
	echo "Usage: $0 [options] <version>"
	echo ''
	echo 'Options:'
	echo '  -h, --help         Print this help message'
	echo '  -n, --disable-git  Disable git support'
	echo ''
	echo 'Arguments:'
	echo '  version  Version to bump to (e.g. 1.1.0)'
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
