#!/bin/bash
# Script that takes an URL and displays the body of the response

curl $1 -sX GET -H "X-School-User-Id: 98"
