# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/jyk08_000/Python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    # FILL IN YOUR CODE HERE...
    for e in secretWord:
        if e in lettersGuessed:
            continue
        else:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ""
    for e in secretWord:
        if e in lettersGuessed:
            result += e
        else:
            result += "_ "
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    examples = "abcdefghijklmnopqrstuvwxyz"
    def removechar(strinput, char):
        newWord = ""
        for num in range(len(strinput)):
            if char == strinput[num]:
                newWord = strinput[:num]
                index = num+1
                if index >= len(strinput):
                    break
                newWord += strinput[index:]
        return newWord
    for e in lettersGuessed:
        examples = removechar(examples, e)
    return examples

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
    # FILL IN YOUR CODE HERE...
    guessed = []
    GuessedWord = getGuessedWord(secretWord, guessed)
    life = 8
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+ str(len(secretWord)) +' letters long.'
    print '-------------'
    while(life > 0):
        print 'You have ' + str(int(round(life))) + ' guesses left.'
        print 'Available letters: ' + getAvailableLetters(guessed)
        char =  raw_input('Please guess a letter: ').lower()
        if char.isalpha():
            if char in guessed:
                print "Oops! You've already guessed that letter: "+ GuessedWord
            else:
                guessed.append(char)
                if char in secretWord:
                    GuessedWord = getGuessedWord(secretWord, guessed)
                    print "Good guess: " + GuessedWord
                else:
                    print "Oops! That letter is not in my word: " + GuessedWord
                    life -= 1 
        print "------------"
        if isWordGuessed(secretWord, guessed):
            life = 0
    if isWordGuessed(secretWord, guessed):
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was " + secretWord+ ". "



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)