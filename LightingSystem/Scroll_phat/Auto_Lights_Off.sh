#!/bin/bash

kill $(ps aux | grep '[A]uto_Lights_On.py' | awk '{print $2}')
