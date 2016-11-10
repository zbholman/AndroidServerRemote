ls | grep abc.txt
if [ "$?" = "1" ]; then
        echo "Couldn't do annything" 1>&2
        exit 1
fi
if [ "$?" = "0" ]; then
        echo "Ok found the file"
        scp pi@192.168.1.200:/home/pi/media/[somefile.txt] pi@192.168.1.200:/media
        exit 1
fi       
