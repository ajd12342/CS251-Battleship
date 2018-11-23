sudo apt install python-dev
sudo apt install python3-pip
sudo apt install redis-server
sudo apt install net-tools
pip3 install -U django
pip3 install -U django-crispy-forms
pip3 install -U channels
pip3 install -U channels-redis
pip3 install -U django-picklefield

if [ $# -eq 0 ];
then
  echo "Usage: sudo bash begin.sh <server_ip>";
  exit 1;
fi
  
bash run.sh "$1"
