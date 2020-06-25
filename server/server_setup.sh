#!/usr/bin/env bash

# https://www.digitalocean.com/community/tutorials/how-to-set-up-uwsgi-and-nginx-to-serve-python-apps-on-ubuntu-14-04
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-20-04
# https://docs.pylonsproject.org/projects/pyramid-cookbook/en/latest/deployment/uwsgi_cookiecutter_1_nginx.html

# Consider running these two commands separately
# Do a reboot before continuing.
apt update
apt upgrade -y

# Install some OS dependencies:
# (q for quiet, y for automatic say yes to prompts)
sudo apt install -y -q build-essential git
sudo apt install -y -q python3-pip python3-dev python3-venv
sudo apt install -y -q unzip wget
sudo apt install -y -q nginx
# for gzip support in uwsgi
sudo apt-get install --no-install-recommends -y -q libpcre3-dev libz-dev nload
# tree
apt install -y -q tree

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
# everybody gets read, write and execute permissions
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
# httpie: like curl but with colors. glances: look at processes
pip install --upgrade httpie glances
pip install --upgrade uwsgi


# clone the repo:
cd /apps || exit
git clone https://github.com/niekstortenbeker/kultur app_repo/kultur
git clone https://github.com/niekstortenbeker/kulturweb app_repo/kulturweb

#Setup for kultur
apt install firefox-geckodriver

# Setup the web app:
cd /apps/app_repo/kultur || exit
python setup.py develop
cd /apps/app_repo/kulturweb || exit
python setup.py develop

# Copy uWSGI details to systemd and enable the daemon
# daemon allows uWSGI to be active as a background process, also on reboot
cp /apps/app_repo/kulturweb/server/kulturweb.service /etc/systemd/system/

# use sytemcontrol stuff to start the application
systemctl start kulturweb
systemctl status kulturweb
# make sure it also active after reboot
systemctl enable kulturweb

# Setup the public facing server (NGINX)
# remove the default website and give it kulturweb instead
rm /etc/nginx/sites-enabled/default
cp /apps/app_repo/kulturweb/server/kulturweb.nginx /etc/nginx/sites-enabled/kulturweb.nginx
# update nginx to start as a service (and remain active after reboot)
update-rc.d nginx enable
# and start / restart nginx
service nginx restart
