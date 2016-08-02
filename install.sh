#!/bin/bash

# Fail on any non-zero exit
set -e

# Detect script location
SRCDIR=$(dirname "$0")

if [ ! -d "$HOME/.themes" ]; then
    echo 'Creating user theme directory...'
    mkdir -p "$HOME/.themes"
fi

echo 'Copying theme files...'
cp -r "$SRCDIR/elegance-orange" "$HOME/.themes"

echo "Theme installed to: $HOME/.themes/elegance-orange"
