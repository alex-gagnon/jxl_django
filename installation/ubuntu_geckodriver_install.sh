#!/usr/bin/env bash

# Firefox geckodriver for selenium
# Download
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
# Extract from zip
tar -xvzf geckodriver*
# Make executable
chmod +x geckodriver
# Move into PATH
sudo mv geckodriver /usr/local/bin