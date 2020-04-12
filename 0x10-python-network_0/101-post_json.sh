#!/bin/bash
# Bash script that sends a JSON POST
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
