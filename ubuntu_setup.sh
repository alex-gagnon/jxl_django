#!/usr/bin/env bash

# Run this at the ~/ level for proper installation

echo "This is a shell script"
ls -lah
echo "I am done running ls"
CHAINS='------------'
cd ~/
echo "$CHAINS Changed directory $CHAINS"
sudo apt update
echo "$CHAINS Ran updates $CHAINS"
sudo apt install libpq-dev python-dev python3-dev python3.7-dev
echo "$CHAINS Installed packages required for postgresql $CHAINS"
sudo apt install postgresql postgresql-client
echo "$CHAINS Installed postgresql $CHAINS"
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo netstat -nl | grep postgresql
sudo service postgresql status