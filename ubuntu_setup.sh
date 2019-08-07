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
if [ "$(sudo netstat -nl | grep postgresql)" ];
then
  echo "Postgresql running on port 5432. You're good to go!";
else
  echo "$CHAINS $CHAINS"
  echo "Postgresql is not running"
  echo "Please check /etc/postgresql/10/main postgresql.conf and pg_hba.conf for proper settings"
  echo "postgresql.conf - uncomment listen_addresses and set equal to *; make sure port is correct"
  echo "pg_hba.conf - add: local  all  all  192.168.1.0/24  md5"
  echo "sudo systemctl restart postgresql"
  echo "$CHAINS $CHAINS";
fi