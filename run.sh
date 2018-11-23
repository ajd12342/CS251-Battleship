cd Battleship
redis-server --port 10000 &
python3 manage.py runserver "$1:8000" &
