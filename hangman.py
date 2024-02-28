
import random

def choose_word():
    # List of words to be used in the game
    words = ["home", "school", "fox", "road", "avenue", "ocean"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with dashes for unguessed letters rather than the letters you have guessed
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '-'
    return displayed_word

#introduce the game
def hangman():
    print("Welcome to the Hangman Game!")
    #choose any random word from the above
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\nAttempts left:", attempts)
        displayed = display_word(word, guessed_letters)
        print(displayed)

        if '-' not in displayed:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

       
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess not in word:
            print("you lost!")
            attempts -= 1
            if attempts == 0:
                print("You're out of attempts. The word was:", word)
                break
        else:
            print("Correct guess!")

hangman()
