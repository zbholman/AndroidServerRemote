sudo apt-get update
	if [ "$?" = "1" ]; then
		echo "Cannot update check internet connection" 1>&2
		exit 1
	fi

sudo apt-get upgrade -y
	if [ "$?" = "1" ]; then
		echo "Cannot upgrade repositories something went wrong" 1>&2
		exit 1
	fi
sudo apt-get install
	if [ "$?" = "1" ]; then
		echo "Cannot install repositories something went wrong" 1>&2
		exit 1
	fi
sudo apt-get dist-upgrade -y
	if [ "$?" = "1" ]; then
		echo "Cannot upgrade the distribution" 1>&2
		exit 1
	fi
sudo pi-bluetooth --version | grep 3
	if [ "$?" = "1" ]; then
		sudo apt-get install pi-bluetooth
			if [ "$?" = "1" ]; then
				echo "Cannot install pi-bluetooth" 1>&2
				exit 1
			fi
		exit 1
	fi
sudo bluez --version | grep 3
	if [ "$?" = "1" ]; then
		sudo apt-get install bluez bluez-firmware
			if [ "$?" = "1" ]; then
				echo "Cannot install pi-bluetooth" 1>&2
				exit 1
			fi
		exit 1
	fi
sudo blueman --version | grep 2.1
	if [ "$?" = "1" ]; then
		sudo apt-get install blueman
			if [ "$?" = "1" ]; then
				echo "Cannot install pi-bluetooth" 1>&2
				exit 1
			fi
		exit 1
	fi
sudo usermod -G bluetooth -a pi
	if [ "$?" = "1" ]; then
		echo "Failed to provide permission" 1>&2
		exit 1
	fi
cat /etc/group | grep bluetooth
	if [ "$?" = "1" ]; then
		echo "no bluetooth activity found" 1>&2
		exit 1
	fi



# to check the raspberry pi bluetooth name
sudo hciconfig hci0 name
	if [ "$?" = "1" ]; then
		echo "Couldn't retrieve bluetooth device name" 1>&2
		exit 1
	fi

# to set the bluetooth name
sudo hciconfig hci0 name raspberrypi
	if [ "$?" = "1" ]; then
		echo "Cannot install pi-bluetooth" 1>&2
		exit 1
	fi

# make the raspberry pi discoverable
sudo hciconfig hci0 piscan
	if [ "$?" = "1" ]; then
		echo "Cannot make the pi bluetooth visible" 1>&2
		exit 1
	fi


# setup agent to listen for pairing request
sudo bluetooth-agent 1234
	if [ "$?" = "1" ]; then
		echo "Couldnt listen to the pairing request" 1>&2
		exit 1
	fi


# list currently connected bluetooth devices
sudo bluez-test-device list
	if [ "$?" = "1" ]; then
		echo "Cannot list the connected devices" 1>&2
		exit 1
	fi


# package required for 'pand' command
sudo apt-get install bluez-compat
	if [ "$?" = "1" ]; then
		echo "Cannot install bluez-compat" 1>&2
		exit 1
	fi


