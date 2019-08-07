#!/usr/bin/env bash

# Assists in making echo's visible
CHAINS='------------'

# Change to current user's home directory
cd ~/
echo "$CHAINS Changed to home directory $CHAINS"

# Run update with advanced packaging tool (apt)
sudo apt update
echo "$CHAINS Ran apt updates $CHAINS"

# Install required packages for postgresql
sudo apt install libpq-dev python-dev python3-dev python3.7-dev
echo "$CHAINS Installed packages required for postgresql $CHAINS"

# Install postgresql
sudo apt install postgresql postgresql-client
echo "$CHAINS Installed postgresql $CHAINS"

# Start and enable postgresql
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl is-active --quiet service && echo Service is running

# Check if postgresql is running on port
if [ -z "$(sudo netstat -tupln | grep 5432)" ];
then
  echo "Postgresql is not running"
  echo "Please check /etc/postgresql/10/main postgresql.conf and pg_hba.conf for proper settings";
else
  echo "Postgresql running on port 5432. You're good to go!";
fi