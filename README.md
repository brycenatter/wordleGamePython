# wordleGamePython
#### A simple implementation of the Wordle game to test my Wordle bot over thousands of games in Python3


## Usage

#### Create a new Game object

Game numbers represent the day of the Wordle and align with the game number in the real Wordle game (before the NYT acquisition).

```python
# creates new game object for wordle game number 122
newGame = Game(122)
```

#### Get correct answer for the Game object

```python
# creates new game object for Wordle game number 122
newGame = Game(122)

# print correct answer for given game number
print(newGame.getAnswer())
# prints "comet"
```

#### Submit guess to Game

Guess must be 5 letters long. The guess is **NOT** checked against a dictionary to determine if it is a real word, any string of 5 characters will be accepted. Returns array with values 0 through 2 to represent the colored square of Wordle.

Green square 🟩 → 2<br>
Yellow square 🟨 → 1<br>
White/black square ⬜️⬛️ → 0<br>

```python
# creates new game object for Wordle game number 122
newGame = Game(122)

# submits guess
newGame.submitGuess('crowd')
# returns [2, 0, 1, 0, 0]
```

