# Prime Game

## Introduction

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

## Requirements

- Python 3.4.3
- Files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- PEP 8 style (version 1.7.x) must be used
- All files must be executable

## Files

- `prime_game.py`: Contains the main implementation of the Prime Game.
- `README.md`: This file, which provides an overview of the project and how to use it.

## Usage

### Prime Game Function

The main function to determine the winner is `isWinner(x, nums)`.

#### Prototype

```python
def isWinner(x, nums)

