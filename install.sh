#!/bin/sh

# DockerX Installer
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

			'--install-dir' | '-i' )
				shift
				# Check for installation directory argument
				if [ -z "$1" ]; then
					echo 'Error: Missing installation directory.' >&2
					DOCKERX_PRINT_HELP='true'
					ERROR_CODE=1
					break
				fi
				# Set installation directory
				DOCKERX_INSTALL_DIR="$1"
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

	# Check for optional positional arguments
	if [ "$#" -le 0 ]; then
		# No more arguments
		break
	fi

	# Parse first optional positional argument
	# Parse install tag argument
	DOCKERX_INSTALL_TAG="$1"
	shift

	# Stop parsing arguments
	break

done

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

# Get install directory
INSTALL_DIR='/usr/local/bin' # Default installation directory
if [ -n "$DOCKERX_INSTALL_DIR" ]; then
	# Use from argument or environment variable
	INSTALL_DIR="$DOCKERX_INSTALL_DIR"
fi

# Get install tag
INSTALL_TAG='latest'
if [ -n "$DOCKERX_INSTALL_TAG" ]; then
	# Use from argument or environment variable
	if
		[ "$DOCKERX_INSTALL_TAG" = 'HEAD' ] || [ "$DOCKERX_INSTALL_TAG" = 'head' ] ||
		[ "$DOCKERX_INSTALL_TAG" = '.' ] || [ "$DOCKERX_INSTALL_TAG" = '-' ]
	then
		INSTALL_TAG='HEAD'
	else
		INSTALL_TAG="$DOCKERX_INSTALL_TAG"
	fi
fi

if [ ! -d "$INSTALL_DIR" ]; then
	echo "Error: Install directory '$INSTALL_DIR' does not exist." >&2
	exit 1
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
