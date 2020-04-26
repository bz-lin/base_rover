### build rover with raspberry buster lite img ###

##enable ssh service##
systemctl enable ssh
systemctl restart ssh

##chage hostname##
echo "rover" > /etc/hostname
sed -i 6{s/raspberrypi/rover/g} /etc/hosts
#hostnamectl set-hostname monitor

##set wifi##
cat <<EOT >> /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=TW

network={
        ssid="monitor"
        psk="49937000"
}
EOT

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

##install pip3 & pigpio##
apt install -y python3-pip python3-pigpio

##install pyserial##
pip3 install pyserial

##enable pigpio service##
systemctl enable pigpiod

