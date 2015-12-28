apt-get -y update
apt-get -y dist-upgrade

apt-get -y install wget
wget https://dl.dropboxusercontent.com/u/65169988/.tmux.conf
wget https://dl.dropboxusercontent.com/u/65169988/.emacs

apt-get -y install tmux
apt-get -y install emacs24

apt-get -y install python3.4
apt-get -y install python3-pip
apt-get -y install python3-bs4
apt-get -y install python3-requests
pip3 install grequests
apt-get -y install python3-numpy
apt-get -y install python3-scipy
apt-get -y install python3-matplotlib
apt-get -y install python3-pandas

apt-get -y install git