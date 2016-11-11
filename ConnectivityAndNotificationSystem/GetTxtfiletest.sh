SFTP_SERVER="192.168.0.101"# the server ip
SFTP_USER="SakifAbu"# the user name for the server
SFTP_PWD="sakifabu"# the password required for the user

mkdir /home/user/Desktop/carfiles/carID100b7# making a directory to do the dump
if [ "$?" = "1" ]; then #checking work status
        echo "Couldn't make a directory" 1>&2# letting the user know if it failed
        exit 1
fi

lftp sftp://$SFTP_USER:$SFTP_PWD@$SFTP_SERVER  -e 'mirror -r /home/sakifabu/PSUABFA16IST440/MonitoringandLogging/logdump ~/home/user/Desktop/carfiles/carID100b7;'#lftp is a command-line file transfer program that supports sftp
#it mirrors anything in that particular folder to the defined directory.
if [ "$?" = "1" ]; then #checking work status
        echo "Couldn't copy the files" 1>&2# letting the user know if it failed
        exit 1
fi



#ls | grep abc.txt
#if [ "$?" = "1" ]; then
     #   echo "Couldn't do annything" 1>&2
    #    exit 1
#fi
#if [ "$?" = "0" ]; then
   #     echo "Ok found the file"
  #      scp pi@192.168.1.200:/home/pi/media/[somefile.txt] pi@192.168.1.200:/media
 #       exit 1
#fi       
