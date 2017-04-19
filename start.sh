ear
echo "Update system"

sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install python3-pip python3-dev
sudo pip3  install --upgrade

echo "install Bottle and Virtualenv"

sudo apt-get install python-virtualenv
mkdir ~/projects
cd ~/projects
virtualenv --no-site-packages venv
source venv/bin/activate
cd ~/projects
source venv/bin/activate
deactivate
pip3 install bottle

echo "install tensorflow"

sudo pip3 install tensorflow

