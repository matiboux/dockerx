#!/bin/sh

# DockerX Installer
# Wrapper for running docker programs & docker shell environments.
# https://github.com/matiboux/dockerx
# MIT License
# Copyright (c) 2024 Matiboux
# This project is not affiliated with Docker, Inc.

if [ "$#" -gt 0 ]; then

	if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
		echo "Usage: install.sh [install_dir] [version]"
		echo "  install_dir: Installation directory (default: /usr/local/bin)"
		echo "  version: Specific version to install (default: HEAD)"
		exit 0
	fi

	if [ "$1" = "--install-dir" ] || [ "$1" = "-i" ]; then
		# Installation directory argument is provided
		shift
		DOCKERX_INSTALL_DIR="$1"
		shift
		if [ -z "$DOCKERX_INSTALL_DIR" ]; then
			echo "Error: Missing installation directory." >&2
			exit 1
		fi
	fi

	if [ -n "$1" ]; then
		# Version argument is provided
		DOCKERX_REQUIRED_TAG="v$1"
		shift
	fi

fi

# Get installation directory
if [ -n "$DOCKERX_INSTALL_DIR" ]; then
	# Use from argument or environment variable
	INSTALL_DIR="$DOCKERX_INSTALL_DIR"
else
	# Default installation directory
	INSTALL_DIR='/usr/local/bin'
fi

# Get required tag to install
if [ -n "$DOCKERX_REQUIRED_TAG" ]; then
	# Use from argument or environment variable
	REQUIRED_TAG="$DOCKERX_REQUIRED_TAG"
else
	# Default required tag
	REQUIRED_TAG="HEAD"
fi

# Check that docker is installed
docker --help > /dev/null 2>&1
if [ $? -ne 0 ]; then
	echo "Error: Docker is not installed." >&2
	exit 1
fi

curl -fsSL https://raw.githubusercontent.com/matiboux/dockerx/$REQUIRED_TAG/dockerx -o "$INSTALL_DIR/dockerx"
if [ $? -ne 0 ]; then
	echo "Error: DockerX installation failed." >&2
	exit 1
fi

chmod +x "$INSTALL_DIR/dockerx"
if [ $? -ne 0 ]; then
	echo "Error: Failed to add execute permission." >&2
	exit 1
fi

echo "DockerX ($REQUIRED_TAG) installed successfully at '$INSTALL_DIR/dockerx'!"
