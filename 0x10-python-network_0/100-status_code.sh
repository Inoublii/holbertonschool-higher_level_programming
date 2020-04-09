#!/bin/bash
#displays request code" 
curl -o -I -L -s -w "%{http_code}" $1
