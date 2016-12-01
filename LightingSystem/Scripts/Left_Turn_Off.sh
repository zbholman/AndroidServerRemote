#!/bin/bash

kill $(ps aux | grep '[T]urn_Signal_On.py' | awk '{print $2}')
kill $(ps aux | grep '[L]eft_Turn_On.py' | awk '{print $2}')

python /home/pi/PSUABFA16IST440/LightingSystem/LedBarLights/Left_Turn_Off.py
python /home/pi/PSUABFA16IST440/LightingSystem/Scroll_phat/Leds_Off.py
