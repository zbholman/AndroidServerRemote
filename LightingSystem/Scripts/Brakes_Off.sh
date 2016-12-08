#!/bin/bash

kill $(ps aux | grep '[B]rakes_On.py' | awk '{print $2}')

python /home/pi/PSUABFA16IST440/LightingSystem/LedBarLights/Brakes_Off.py
