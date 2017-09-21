#!/bin/bash
if [ -z "$1" ];then
  echo -e "\033[31m need 1 arg <start/stop>\033[0m"
  exit
elif [ $1 == "start" ];then
  nohup python3 get_hosts_api.py &
elif [ $1 == "stop" ]; then
  ps aux |grep get_host |grep -v grep | awk '{print $2}' |xargs kill -9
fi
