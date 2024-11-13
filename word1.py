#!/usr/bin/env bash

get_file_name() {
	read -p "Enter a file_name: " -r FILENAME
	if [ -n "$FILENAME" ]
	then
		MYFILE="$FILENAME"
	else
		return 1
	fi
}
get_log_data() {
	read -p "Enter a log data i.e ipaddress, timestamp, httpmethod, statuscode, or responsesize: " -r LOGDATA
	case "$LOGDATA" in
		ipaddress|timestamp|httpmethod|statuscode|responsesize)
			LOGDATAS="$LOGDATA"
			;;
		*)
			echo "Invalid log data type."
			return 1
			;;
	esac
}
get_exit_choice() {
	read -p "Do you still want to continue 1 for YES or 0 for NO? " -r CHOICE
	if [ "$CHOICE" = "1" ]
	then
		return 0
	elif [ "$CHOICE" = "0" ]
	then
		return 1
	else
		return 2
	fi
}
log_regex_automation() {
	while true
	do
		get_file_name
		file_result=$?
		get_log_data
		log_result=$?
		if [ "$file_result" -ne 0 -a "$log_result" -ne 0 ]
		then
			if ! ./regex.rb "$MYFILE" "$LOGDATAS"; then
				echo "Error: regex.rb script failed to execute."
				exit 1
			fi
		else
			if ! ./regex.rb; then
				echo "Error: regex.rb script failed to execute."
				exit 1
			fi
		fi
		get_exit_choice
		exit_result=$?
		if [ "$exit_result" -eq 0 ]
		then
			true
		elif [ "$exit_result" -eq 1 ]
		then
			exit
		else
			echo "Your choice of exit was $exit_result, so app is still exiting..."
			sleep 3
			exit
		fi
	done
}
log_regex_automation
