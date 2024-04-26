#!/bin/bash
#usage takes in one parameter
#this will set to block trackers

if [ $# -eq 0 ]
	then
		echo "Usage: $(basename $0) ... (atleast 1 argument)" 1>&2
exit 1
fi

#run the command

if [ $1 = "t" ] || [  $1 = "T" ] || [ $1 = "true" ] [ $1 = "True" ]
	then
		expressvpn preferences set block_trackers true; expressvpn disconnect; expressvpn connect smart
elif [ $1 = "f" ] || [ $1 = "F" ] || [ $1 = "false" ] || [ $1 = "False" ] 
	then 
		expressvpn preferences set block_trackers false; expressvpn disconnect; expressvpn connect smart
fi

