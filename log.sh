#!/usr/bin/env bash

LOG_ERROR='/srv/project/.log/error.log'
LOG_INFO='/srv/project/.log/info.log'
CMD='sudo docker exec $(sudo docker ps -q) tail -f'
eb ssh --command "$CMD $LOG_ERROR"
