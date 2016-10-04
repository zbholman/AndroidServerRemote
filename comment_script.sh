#!/bin/bash
# This script creates the comment header for python files you've created
# Author: Brian Holman
# Course: IST 440
# Date: 10/02/2016

### Description
printf "\nThis script creates comment headers for your python files\n"
printf "Hopefully it saves you some time\n\n"

### Create variables
printf "Enter your first name:\n"
read firstName
printf "\nEnter your last name:\n"
read lastName
printf "\nEnter your team directory in the git repo, ex: LightingSystem\n"
read teamDirectory
todaysDate=$(date +%m-%d-%Y) # Date format of MM-DD-YYYY

### Create comment format
headerComment="# Author: $firstName $lastName&\n# Course: IST 440&\n# Team: $teamDirectory&\n# Date: $todaysDate&\n&\n"

### Function for adding comment if it doesn't exist
function checkHeader() {

	# Variable to check the first line of the file
	firstChar=$(head -c 1 $1)

	# If the first line starts with '# Author' skip file
	if [[ "$firstLine" != "#" ]]; then

		# If the first line doesn't, ask user if they created it
		printf "\n$f doesn't have a header comment\n"
		read -p "If you created it, would you like to add a header comment? (y/n)" -n 1 -r
		echo

		# If they reply 'y', then create header comment
		if [[ $REPLY =~ ^[Yy]$ ]]; then
			
			# If the user is on mac, use gsed command (requires homebrew and gsed)
			if [ "$(uname)" == "Darwin" ]; then
				# Enter header comment into the top of the file
    			gsed -i "1s/^/$headerComment/" $1
	
    		# If the user is on linux, used normal sed command
			elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
				sed -i "1s/^/$headerComment/" $1
			fi
		fi
	fi
}

### Navigate to team directory
cd $teamDirectory

### Set internal file seperator to recognize spaces in filenames
IFS=$'\n'

### Find all python files in team directory, and run header function
for f in $(find . -name '*.py'); do
  checkHeader $f
done