#!/bin/bash
#This script is for Supervisor to run Gunicorn
#set -e
LOGFILE=/home/ubuntu/viclo/logs/guni.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=2
VIRTUALENV='viclo_env'
# user/group to run as [add in later]
ADDRESS=0.0.0.0:8000
cd /home/ubuntu/viclo
source /usr/local/bin/virtualenvwrapper.sh
workon $VIRTUALENV
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS --bind=$ADDRESS --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE
