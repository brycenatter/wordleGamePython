from answerWords import words as wordleWords


class Game:
    def __init__(self, gameNum):
        # print(wordleWords)
        self.todaysWord = wordleWords[gameNum]

    def getAnswer(self):
        return self.todaysWord

    def submitGuess(self, guessedWord):
        returnVals = []
        correctLetters = []
        try:
            for i in range(len(guessedWord)):
                # green square
                curSubString = guessedWord[i:len(guessedWord)]
                if(self.todaysWord[i] == curSubString[0]):
                    returnVals.append(2)
                    correctLetters.append(curSubString[0])

                # yellowsquare
                elif(self.todaysWord.find(guessedWord[i]) > -1):
                    if guessedWord[i] in correctLetters:
                        returnVals.append(0)
                    else:
                        returnVals.append(1)

                # greysquare
                else:
                    returnVals.append(0)
            return returnVals
        except:
            return 'Guess too long'
