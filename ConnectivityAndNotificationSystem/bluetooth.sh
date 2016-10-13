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
	
	#testing
