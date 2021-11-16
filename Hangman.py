# Problem Set 2, hangman.py
# Name: Imad Roula
# Collaborators: /
# Time spent: 6 days
# Hangman Game

import os
import random
import string
WORDLIST_FILENAME = "words.txt"
os.system('cls' if os.name == 'nt' else 'clear')


def load_words():
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()

# ---------------------------------
secret_word = choose_word(wordlist)
#secret_word = "tact"
# ---------------------------------

# Secret Word Length & List
sw_length = len(secret_word)
secret_word_inlist = list(secret_word)

# -------------------------GLOBAL VARIABLES ------------------
letters_guessed_sorted = ['yy']
indexx = 0
# Creat a list of underderscore and spaces to start with
word_to_print = []
for ee in range(sw_length):
    word_to_print.append("_ ")
letters_guessed = []
alphabet = string.ascii_lowercase
alphabet_list = list(alphabet)
vowels = ["a", "o", "e", "i"]
# ------------------------------------------------------------

print("secret word = ", secret_word)


def hangman(secret_word):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ", sw_length, " letters long.")
    Guesses_Left = 6
    Warnings_left = 3
    while Guesses_Left > 0:
        print("You Have", Guesses_Left, "Guesses Left!")
        alphabet_string = ""

        for ee in alphabet_list:
            alphabet_string += ee
        print("Letters Available : ", alphabet_string)
        GL = input("enter a letter : ")[0]

        if GL.isalpha() is True:
            GL = GL.lower()

            if GL not in alphabet_list:

                if Warnings_left is not 0:
                    Warnings_left -= 1
                    print("Oops! You've already guessed that letter. You Have",
                          Warnings_left, "Warnings left.")

                else:
                    print(
                        "Oops! You've already guessed that letter. You have no warnings left so you lose one guess")
                    Guesses_Left -= 1

            else:

                if str(GL) in secret_word_inlist:

                    alphabet_list.remove(str(GL))
                    x = secret_word_inlist.count(GL)

                    for y in range(x):
                        letters_guessed.append(GL)
                    indexx = [i for i, n in enumerate(
                        secret_word_inlist) if n == GL]

                    for ee in indexx:
                        word_to_print[ee] = GL
                    print(f"Good Guess : {force_string(word_to_print)}")

                else:
                    print("Oops! that letter is not in my word")
                    alphabet_list.remove(str(GL))
                    Guesses_Left -= 1
                    if str(GL) in vowels:
                        Guesses_Left -= 1
        else:
            if Warnings_left is not 0:
                Warnings_left -= 1
                print("Oops! That is not a valid letter. You Have",
                      Warnings_left, "Warnings left.")

            else:
                print(
                    "Oops! That is not a valid letter. You have no warnings left so you lose one guess")
                Guesses_Left -= 1
        print("---------------------------------------------------------------------------")

        score = len(set(secret_word))*Guesses_Left
        if all(letters in letters_guessed for letters in secret_word):
            print("YOU WON")
            print("You total score for this game is", score)
            break

    if Guesses_Left is 0:
        print("Sorry, you ran out of guesses. The word was else : ", secret_word)


def match_with_gaps(my_word, other_word):
    if len(my_word) == len(other_word):
        if all([item == other_word[index] or item == "_ " for index, item in enumerate(my_word)]):
            return True
        else:
            return False
    else:
        return False


def show_possible_matches(my_word):
    possible_matches_list = []
    for eachword in wordlist:
        if match_with_gaps(my_word, eachword):
            possible_matches_list.append(eachword)
    if len(possible_matches_list) > 0:
        print(f"You have {len(possible_matches_list)} possible word :")
        for ee in possible_matches_list:
            print(ee, ", ", end="")
    else:
        print("No Possible Matches !")


def force_string(thelist):
    strng = ""
    for ee in thelist:
        strng += ee
    return strng


def hangman_with_hints(secret_word):
    print("Welcome to the game Hangman with hints!")
    print("I am thinking of a word that is ", sw_length, " letters long.")
    Guesses_Left = 6
    Warnings_left = 3
    while Guesses_Left > 0:
        print("You Have", Guesses_Left, "Guesses Left!")
        print("You Have", Warnings_left, "Warnings left!")
        alphabet_string = force_string(alphabet_list)
        print("Letters Available : ", alphabet_string)
        GL = input("Please guess a letter : ")[0]
        if GL.isalpha() is True:
            GL = GL.lower()
            if GL not in alphabet_list:
                if Warnings_left is not 0:
                    Warnings_left -= 1
                    print("Oops! You've already guessed that letter. You Have",
                          Warnings_left, "Warnings left: ", word_to_print_string)
                else:
                    print(
                        "Oops! You've already guessed that letter. You have no warnings left so you lose one guess")
                    Guesses_Left -= 1
            else:
                if str(GL) in secret_word_inlist:
                    alphabet_list.remove(str(GL))
                    x = secret_word_inlist.count(GL)
                    for y in range(x):
                        letters_guessed.append(GL)

                    indexx = [i for i, n in enumerate(
                        secret_word_inlist) if n == GL]
                    for ee in indexx:
                        word_to_print[ee] = GL
                    word_to_print_string = ""
                    for ee in word_to_print:
                        word_to_print_string += ee
                    print(f"Good Guess : {word_to_print_string}")
                else:
                    print("Oops! that letter is not in my word")
                    alphabet_list.remove(str(GL))
                    Guesses_Left -= 1
                    if str(GL) in vowels:
                        Guesses_Left -= 1
        else:
            if GL is "*":
                show_possible_matches(word_to_print)
            else:
                if Warnings_left is not 0:
                    Warnings_left -= 1
                    print("Oops! That is not a valid letter. You Have",
                          Warnings_left, "Warnings left.")
                else:
                    print(
                        "Oops! That is not a valid letter. You have no warnings left so you lose one guess")
                    Guesses_Left -= 1
        print("---------------------------------------------------------")

        score = len(set(secret_word))*Guesses_Left
        if all(letters in letters_guessed for letters in secret_word):
            print("YOU WON")
            print("You total score for this game is", score)
            break
    if Guesses_Left is 0:
        print("Sorry, you ran out of guesses. The word was else : ", secret_word)


# hangman_with_hints(secret_word)
hangman(secret_word)
