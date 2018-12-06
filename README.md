# CS251-Battleship

An online version of the Battleship Game with some additional features for CS-251 Course Project.

## Guide To Run Server

 - Find your ip address by running the following command in a terminal
 
        ifconfig
 - Add your ip address in the file `CS251-Battleship/Battleship/Battleship/settings.py` inside the list `ALLOWED_HOSTS` at line 28
  - Run `build.sh` with `sudo` permissions to install the required dependencies and start the server as:
 
        sudo bash build.sh <server_ip>
  - If all the dependencies are already installed then, run the following to start the server:
  
        bash run.sh <server_ip>
  - Login credentials for Django admin:
      - Username: admin
      - Password: admin
 
 ## Guide to Start Playing
 - Get the ip address of the server `<server_ip>`
 - Head to a browser and go to `<server_ip>:8000/`
 - Login with your existing credentials or create a new account
 - You are now at your profile page. Click on Begin Game to see the list of available players
 
 ## Guide to Play
 - Click on any user to send them a play request
 - Once the player accepts your request, you will be redirected to page where you will have to place your ships.
 - Instructions for placing ships:
    - To place a ship on the board, first click the ship's shape to select it and then click a location on the board. The square marked by an 'X' will be placed at the clicked location.
    - To rotate a ship and place it, first click the ship's shape to select it. Any subsequent clicks on the same shape will rotate it. Place on the board as before.
    - After completing placing of all ships, click the Submit button.
 - Once your opponent finishes placing their ships, both of you will be directed to the game page
 - Each player is given a chance to shoots at their opponent's ships alternatively. Each turn lasts for 20 seconds after which you forfeit you turn and the opponent plays. For a correct move you get another move.
 - Enjoy the game :smiley:
 
 ## Scoring
 - For each correct shot fired in time `t` seconds the player is awarded `20-t` points
 - For each wrong shot fired, no points are awarded or deducted
 - At the end of the game, the winner is awarded points equal the sum of points awarded at each move
  
 ## Dependencies
 - __Linux__
   - Python Dev
   - Redis
   - Net Tools
 - __Python__
   - Django == 2.1.3
   - Django Crispy Forms == 1.7.2
   - Channels == 2.1.5
   - Django Picklefield == 1.1.0
   - Channels-Redis == 2.3.1
 
 
## An Example Placing of Ships
![alt text](https://github.com/ajd12342/CS251-Battleship/blob/master/sample.png)

## An Example Game (Just started playing)
![alt text](https://github.com/ajd12342/CS251-Battleship/blob/master/game.png)

