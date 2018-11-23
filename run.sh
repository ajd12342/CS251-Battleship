#/bin/bash
if [ $# -ne 1 ];
then
  echo "Usage: bash run.sh <server_ip>";
  exit 1;
fi

cd Battleship
redis-server --port 10000 &
python3 manage.py runserver "$1:8000" &
