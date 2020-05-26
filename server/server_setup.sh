#!/usr/bin/env bash

# Consider running these two commands separately
# Do a reboot before continuing.
apt update
apt upgrade -y

# Install some OS dependencies:
sudo apt-get install -y -q build-essential git 
sudo apt-get install -y -q python3-pip python3-dev python3-venv
sudo apt-get install -y -q unzip wget
sudo apt-get install -y -q nginx
# for gzip support in uwsgi
sudo apt-get install --no-install-recommends -y -q libpcre3-dev libz-dev nload
# tree
apt install tree

# Stop the hackers
# block ssh users that try repeatedly to login
sudo apt install fail2ban -y

# only allow ssh, http and https. setup firewall for everything else.
ufw allow 22
ufw allow 80
ufw allow 443
ufw enable

# Basic git setup to cache password
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=720000'

# Be sure to put your info here:
git config --global user.email "you@email.com"
git config --global user.name "Your name"

# Web app file structure
mkdir /apps
chmod 777 /apps
mkdir /apps/logs
mkdir /apps/logs/kulturweb
mkdir /apps/logs/kulturweb/app_log
cd /apps || exit

# Create a virtual env for the app.
cd /apps || exit
python3 -m venv venv
source /apps/venv/bin/activate
pip install --upgrade pip setuptools
# httpie: like curl. glances: look at processes
pip install --upgrade httpie glances
pip install --upgrade uwsgi


# clone the repo:
cd /apps || exit
git clone https://github.com/niekstortenbeker/kultur app_repo/kultur
git clone https://github.com/niekstortenbeker/kulturweb app_repo/kulturweb

# Setup the web app:
cd /apps/app_repo/kultur || exit
python setup.py develop
cd /apps/app_repo/kulturweb || exit
# pip install -r requirements.txt
python setup.py develop

# Copy and enable the daemon
cp /apps/app_repo/kulturweb/server/kulturweb.service /etc/systemd/system/

systemctl start kulturweb
systemctl status kulturweb
systemctl enable kulturweb

# Setup the public facing server (NGINX)
apt install nginx

# CAREFUL HERE. If you are using default, maybe skip this
rm /etc/nginx/sites-enabled/default

cp /apps/app_repo/kulturweb/server/kulturweb.nginx /etc/nginx/sites-enabled/kulturweb.nginx
update-rc.d nginx enable
service nginx restart
