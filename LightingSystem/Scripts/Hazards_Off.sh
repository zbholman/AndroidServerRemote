#!/bin/bash

kill $(ps aux | grep '[H]azard_Lights.py' | awk '{print $2}')
kill $(ps aux | grep '[H]azards_On.py' | awk '{print $2}')

python /home/pi/PSUABFA16IST440/LightingSystem/LedBarLights/Hazards_Off.py
python /home/pi/PSUABFA16IST440/LightingSystem/Scroll_phat/Leds_Off.py
