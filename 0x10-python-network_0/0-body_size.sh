#!/bin/bash
#displays size of the body of the response
Curl -sI $1 | grep "content length" | 
