
# Battleship Game

This project is a command-line implementation of the popular board game, ["Battleship"](https://en.wikipedia.org/wiki/Battleship_(game)).

## Rules

The game is single-player (e.g. you play against a bot).

Each player takes turns choosing a position to attack on their opponent's board (you pick first).

The outcome of an attack is one of the following scenerios:

* Miss
* Hit
* Sunk
* Victory

The game board is a 10 x 10 square (100 possible positions).

Each player has a fleet of ships of varying sizes that are randomly placed on the board at the start of the game:

* 1 large ship      (size 4)
* 2 medium ships    (size 3)
* 3 small ships     (size 2)
* 4 micro ships     (size 1)

For a total of 10 ships and 20 occupied positions (out of 100 total, or 20% of the board).

The game is over when all the ships on a player's board are destroyed (sunk).

## Getting Started

Simply clone the project to your system and run the "Game.py" file with Python 3 in a command-line window.

```
git clone [project]

cd [project]/src

python Game.py (you might need to use the python3 command on some systems)
```

### Prerequisites

The only requirement to run this game is [Python 3](https://www.python.org/).

I used Python 3.7.2 specifically when writing the code, and, to ensure maximum compatibility, you should try to match this version as closely as possible.

## Authors

* **Gregory C. Sullivan** - [GitHub](https://github.com/connorsullivan)
