### build monitor with raspberry buster lite img ###

##enable ssh service##
systemctl enable ssh
systemctl restart ssh


##chage hostname##
#hostnamectl set-hostname monitor

##change password for pi##
echo pi:rover | chpasswd

##disable onboard wifi bluetooth##
echo "dtoverlay=pi3-disable-wifi" >> /boot/config.txt
echo "dtoverlay=pi3-disable-bt" >> /boot/config.txt
systemctl disable hciuart

##change mirror for raspi##
#http://free.nchc.org.tw/raspbian/raspbian
echo "deb http://free.nchc.org.tw/raspbian/raspbian/ buster main contrib non-free rpi" > /etc/apt/sources.list     

##update for raspi##
apt update

##install vsftpd.service & setting##
apt install vsftpd -y
echo "write_enable=Yes" >> /etc/vsftpd.conf

##install kivy ver.1.11.1##
apt install -y python3-pip

pip3 install pyserial
