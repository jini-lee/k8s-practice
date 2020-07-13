#!/bin/sh
trap "exit" SIGINT
while :
do
  echo Writing date to /var/htdocs/index.html
  echo $(date) > /var/htdocs/index.html
  sleep 10
done
