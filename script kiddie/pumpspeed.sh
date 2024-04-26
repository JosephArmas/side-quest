#!/bin/bash
#!/bin/bash
#sets the pump speed 

if [ $# -eq 0 ]
	then 
		echo "Usage: $(basename $0)... (takes in at least 1 argument)" 1>&2
		exit 1
fi

sudo liquidctl set pump speed $1
