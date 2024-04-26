#!/bin/bash
#usage takes in @param -> file name
#opens file with xdg-open

if [ $# -eq 0 ]
	then 
		echo: "Usage: $(basename $0) ... (no arguments)" 1>&2
		exit 1
fi

xdg-open $1
