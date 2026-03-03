#!/bin/bash
# Setup script for the project

set -e

echo "Setting up the project..."

# Install Python dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

echo "Setup complete."
