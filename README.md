## Rover
* Raspberry setup 
    * Raspbian Buster install & configure         
    * FTP setup
    * Boot python3 auto start setup
* Antenna setup 
* Appearance setup

### Raspbian stretch install & configure:
You can download image file from [Buster Lite](https://downloads.raspberrypi.org/raspbian_lite_latest)

### Enable SSH Service:
        $sudo systemctl enable ssh
        $sudo systemctl start ssh

### Install FTP Server:
>Install CMD:

        $sudo apt install vsftpd

>Setting File:

        $sudo vi /etc/vsftpd.conf

>Remove one Line '#':

        #write_enable=Yes
        write_enable=Yes
>Enable service:

        $sudo systemctl enable vsftpd

### Auto Start python3 on Boot:
1.  File Location:
        
        Your python3 => /home/pi/test/main.py
        Your systemd File => /lib/systemd/system/python3test.service
        
2.  Wait for Network at Boot Setting:
>setting CMD

        $sudo raspi-config
        
> Raspberry Pi Software Configuration Tool (raspi-config) 
   
        =>3 Boot Options         Configure options for start-up
            =>B2 Wait for Network at Boot Choose whether to wait for network connection

             
3. Add python3test.service for systemd :
>Add python3test.service
        
        sudo vi /lib/systemd/system/python3test.service
        
>Add Lines:

        [Unit]
        Descriptiona=python3test Service
        After=multi-user.target

        [Service]
        Type=idle

        User=pi        
        ExecStart=/usr/bin/python3 /home/pi/test/main.py

        Restart=always
        RestartSec=0

        [Install]
        WantedBy=multi-user.target
        
 >Reload Daemon:
 
        $sudo systemctl daemon-reload
 
 >Enable Service:
 
        $sudo systemctl enable python3test.service

>Reboot to Test:

        $sudo reboot
