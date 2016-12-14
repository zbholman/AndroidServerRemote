#!/bin/bash

kill $(ps aux | grep '[b]raking_off.py' | awk '{print $2}')

python /home/pi/PSUABFA16IST440/BrakingSystem/absbraking.py
