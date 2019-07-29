# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return set(secretWord).issubset(set(lettersGuessed))



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = secretWord
    for x in list(set(secretWord).difference(set(lettersGuessed))):
        result = result.replace(x, '_ ')
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = 'abcdefghijklmnopqrstuvwxyz'
    for letter in lettersGuessed:
        result = result.replace(letter, '')
    return result
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakesMade = 0
    lettersGuessed = []
    print("Welcome to the game, Hangman!")
    template = "I am thinking of a word that is {} letters long."
    print(template.format(len(secretWord)))
    print('-------------')
    while 8 - mistakesMade > 0:
        availableLetters = getAvailableLetters(lettersGuessed)
        template = "You have {} guesses left.\
                    \nAvailable letters: {}\
                    \nPlease guess a letter: "
        guess = input(template.format(8 - mistakesMade, availableLetters))
        guessInLowerCase = guess.lower()
        if guessInLowerCase in lettersGuessed:
            template = "Oops! You've already guessed that letter: {}"
        else:
            lettersGuessed.append(guessInLowerCase)
            if guessInLowerCase in secretWord:
                template = "Good guess: {}"
            else:        
                template = "Oops! That letter is not in my word: {}"
                mistakesMade += 1
        print(template.format(getGuessedWord(secretWord, lettersGuessed)))
        print('-------------')
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
    if mistakesMade == 8:
        template = 'Sorry, you ran out of guesses. The word was {}.'
        print(template.format(secretWord))





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
