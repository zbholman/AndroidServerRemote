#!bin/bash
# Turns off light, sends JSON object

# Kill lighting process
pkill -f $1

# Turn off sense hat lights
./turn_off_sense_hat_lights.py

case $1 in
	'Left_Turn_Signal.py')
        message=left_turn_off
        ;;
esac

python -c "import Message; sendMessage()"