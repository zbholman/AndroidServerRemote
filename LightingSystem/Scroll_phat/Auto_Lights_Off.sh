#!/bin/bash

kill $(ps aux | grep '[A]uto_Lights_On.py' | awk '{print $2}')
python /home/pi/PSUABFA16IST440/LightingSystem/Scroll_phat/Leds_Off.py
