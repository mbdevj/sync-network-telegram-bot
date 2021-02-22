#!/bin/bash

while true;do
	pid=$(ps -ef | grep run.py | grep -v grep | awk '{print $2}')
	
	if [[ -n ${pid} ]];then
		echo "Telegram bot is running with pid: ${pid}"
	else
		echo "Telegram bot found to be down, restarting in 60 seconds"
		sleep 60s
		nohup python3 run.py &
	fi
	sleep 60s
done
