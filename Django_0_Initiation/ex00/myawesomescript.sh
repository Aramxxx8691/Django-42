#!/bin/sh
if [ -z "$1" ]; then
    echo "Usaage: $0 <bit.ly URL>"
    exit 1
fi

curl -sIl $1 | grep Location | cut -d ' ' -f 2
# curl -si -X GET $1 | grep "href" | cut -d \" -f 2