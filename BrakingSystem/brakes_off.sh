#!/bin/bash

kill $(ps aux | grep '[b]raking.py' | awk '{print $2}')

python /home/pi/PSUABFA16IST440/BrakingSystem/braking_off.py
