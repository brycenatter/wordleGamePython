from wordleGame import Game

# creates new game object for wordle game number 122
newGame = Game(122)

# print correct answer for given game number
print(newGame.getAnswer())
# prints comet

# submitting guess of the word and printing the result
# 0 is equivalent to a grey square, 1 is a yellow square, and 2 is a green square
print(newGame.submitGuess('crowd'))

# guessing the correct word will produce an array of all 2s

print(newGame.submitGuess('comet'))
