import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

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
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for char in secret_word: # string is naturally iterable
        if char not in letters_guessed: ##
            return False
    return True

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    temp_str=""
    for l in secret_word:
        if l in letters_guessed:
            temp_str+=l
        else:
            temp_str+='*'
    return temp_str


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    temp_str=""
    for l in string.ascii_lowercase:
        if l not in letters_guessed:
            temp_str+=l
    return temp_str

def get_hint(secret_word,letters_guessed):
    possible_hints=[]
    for char in secret_word:
        if char not in letters_guessed:
            possible_hints.append(char)
    # Can use list comprehension to elegantly create the list!
    # possible_hints=[char for char in secret_word if char not in letters_guessed]
    
    if possible_hints: # a pythonic way, equivalent to possible_hints.empty()
        return random.choice(possible_hints)
    else:
        return None

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # Initialization
    guesses_left=10
    letters_guessed=[]
    vowels=['a','e','i','o','u']

    # Welcome
    print("\nWelcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")

    # Game loop
    while guesses_left>0:
        print("-------")
        print(f"You have {guesses_left} guesses left")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        # Getting input
        prompt_text="Please guess a letter: "
        if with_help:
            prompt_text="Please guess a letter (enter '!' for help): "
        
        # Case sensitivity
        guess=input(prompt_text).lower()

        # Help
        if with_help and guess=='!':
            if guesses_left>=3:
                guesses_left-=3
                hint=get_hint(secret_word,letters_guessed)
                print(f"Hint: The letter '{hint}' is in the word!")
                letters_guessed.append(hint)
                if has_player_won(secret_word,letters_guessed):
                    print("------")
                    print("Congratulations, you won!")
                    print(f"The word was: {secret_word}")
                    return
            else:
                print("Oops! Not enough guesses left for a hint")
            continue

        # Validation check
        if not guess.isalpha() or len(guess)!=1:
            print(f"Oops! That's not a valid letter!")
            continue # Assume that invalid guess doesn't waste chances
        
        # Duplication
        if guess in letters_guessed:
            print(f"Oops! You've already guessed that letter!")
            continue # Assume that duplication doesn't waste chances

        # Normal situation
        letters_guessed.append(guess)
        if guess in secret_word:
            print(f"Good guess: {get_word_progress(secret_word,letters_guessed)}")
            if has_player_won(secret_word,letters_guessed):
                print("------")
                print("Congratulations! You win!")
                return
        
        else:
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word,letters_guessed)}")
            if guess in vowels:
                guesses_left-=2
            else:
                guesses_left-=1
   
    # Iteration ends(Loss)
    print("------")
    print(f"Sorry, you ran out of guesses, the word was {secret_word}")

            
        
        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

