#!/bin/sh

# DockerX Installer
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

		'--install-dir' | '-i' )
			shift
			# Get installation directory argument
			if [ -z "$1" ]; then
				echo 'Error: Missing installation directory.' >&2
				DOCKERX_PRINT_HELP='true'
				ERROR_CODE=1
				# Stop parsing arguments
				DOCKERX_PARSE_ARGUMENTS='false'
				break
			fi
			DOCKERX_INSTALL_DIR="$1"
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

	# Parse install tag optional argument
	if [ "$#" -gt 0 ]; then
		DOCKERX_INSTALL_TAG="$1"
		shift
	fi

fi

if [ "$DOCKERX_PRINT_HELP" = 'true' ]; then
	# Print help & exit
	echo "Usage: $0 [options] [tag]"
	echo ''
	echo 'Options:'
	echo '  --help, -h         Display this help message'
	echo '  --install-dir, -i  Installation directory (defaults to /usr/local/bin)'
	echo ''
	echo 'Arguments:'
	echo '  tag  DockerX tag/version to install (defaults to HEAD)'
	exit ${ERROR_CODE:-0}
fi

# Get installation directory
INSTALL_DIR='/usr/local/bin' # Default installation directory
if [ -n "$DOCKERX_INSTALL_DIR" ]; then
	# Use from argument or environment variable
	INSTALL_DIR="$DOCKERX_INSTALL_DIR"
fi

# Get install tag
INSTALL_TAG='HEAD' # Default required tag
if [ -n "$DOCKERX_INSTALL_TAG" ]; then
	# Use from argument or environment variable
	INSTALL_TAG="$DOCKERX_INSTALL_TAG"
fi

# Check that docker is installed
docker --help > /dev/null 2>&1
if [ $? -ne 0 ]; then
	echo 'Error: Docker is not installed.' >&2
	exit 1
fi

# Check that docker compose is installed
docker compose --help > /dev/null 2>&1
if [ $? -ne 0 ]; then
	echo 'Error: Docker compose is not installed.' >&2
	exit 1
fi

curl -fsSL "https://raw.githubusercontent.com/matiboux/dockerx/$INSTALL_TAG/dockerx" -o "$INSTALL_DIR/dockerx"
if [ $? -ne 0 ]; then
	echo 'Error: DockerX installation failed.' >&2
	exit 1
fi

chmod +x "$INSTALL_DIR/dockerx"
if [ $? -ne 0 ]; then
	echo 'Error: Failed to add execute permission.' >&2
	exit 1
fi

echo "DockerX ($INSTALL_TAG) installed successfully at '$INSTALL_DIR/dockerx'!"
