#!/bin/bash
#this is a launcher for the game, place this where ever it is most convenient for you and run it to run the python script automaticaly, only works for linux
cd /
DIR=$(find "/home/buddy" -name 'game1.py'|sed 's/.$//'|sed 's/.$//'|sed 's/.$//'|sed 's/.$//'|sed 's/.$//'|sed 's/.$//'|sed 's/.$//'|sed 's/.$//'|sed 's/.$//')
echo "$DIR"
cd "$DIR"
python game1.py
wait
echo "Program exited correctly."
exit
