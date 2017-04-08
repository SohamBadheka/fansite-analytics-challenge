#!/usr/bin/env bash

# one example of run.sh script for implementing the features using python
# the contents of this script could be replaced with similar files from any major language

# I'll execute my programs, with the input directory log_input and output the files in the directory log_output
python ./src/hosts.py ./log_input/log.txt ./log_output/hosts.txt
python ./src/hours.py ./log_input/log.txt ./log_output/hours.txt
python ./src/resources.py ./log_input/log.txt ./log_output/resources.txt

# 4th feature is not optimized so, I am not uploading that in the code section
# python ./src/blocked.py ./log_input/log.txt ./log_output/blocked.txt
