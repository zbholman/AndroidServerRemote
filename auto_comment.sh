#!/bin/bash
# This script creates the comment header for python files you've created
# Author: Brian Holman
# Date: 10/02/2016

### Description
printf "\nThis script creates comment headers for your python files\n"
printf "Hopefully it saves you some time\n\n"

### Gather input for variables
printf "Enter your first name:\n"
read firstName
printf "\nEnter your last name:\n"
read lastName
printf "\nWhat project is this for?\n"
read projectName
printf "\nWhat file extension are you looking for? ex: py\n"
read fileType

todaysDate=$(date +%m-%d-%Y) # Date format of MM-DD-YYYY

case $fileType in
	'py')
		commentChar='#'
		;;
	'java')
		commentChar='\/\/'
		;;
esac

### Create comment format
headerComment="$commentChar Author: $firstName $lastName&\n$commentChar Project: $projectName&\n$commentChar Date: $todaysDate&\n&\n"

### Function for adding comment if it doesn't exist
function checkHeader() {

	# Variable to check the first line of the file
	firstChar=$(head -c 1 $1)
	firstCommentChar=$(echo -n $2 | tail -c 1)

	# If the first line starts with a comment character skip file
	if [[ "$firstChar" != "$firstCommentChar" ]]; then

		# If the first line doesn't, ask user if they created it
		printf "\n$f doesn't have a header comment\n"
		read -p "If you created it, would you like to add a header comment? (y/n)" -n 1 -r

		# If they reply 'y', then create header comment
		if [[ $REPLY =~ ^[Yy]$ ]]; then
				sed -i "1s/^/$headerComment/" $1
		fi
		echo
	fi
}

### Set internal file seperator to recognize spaces in filenames
IFS=$'\n'

### Find all python files in team directory, and run header function
for f in $(find . -name \*.$fileType); do
  checkHeader $f $commentChar
done

printf "\nEnd of Results\n\n"