#!/bin/bash
#displays size of body of the response
curl -sI $1 | grep "Allow" | cut -d " " -f2-
