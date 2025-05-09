#!/bin/bash
cd /home/ec2-user/Proj-FN/docker

nohup python3 app.py > /home/ec2-user/app/logs/app.log 2>&1 &

