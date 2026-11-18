import ascii_art
import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    remaining_letters = len(secret_word)

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < 3 and remaining_letters != 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You must enter ONE letter!")
        elif guess not in guessed_letters:
            guessed_letters.append(guess)

            if guess not in secret_word:
                mistakes += 1
            else:
                remaining_letters = remaining_letters - secret_word.count(guess)
        else:
            print("You already guessed this letter!")

        display_game_state(mistakes, secret_word, guessed_letters)
        print(f"Already guessed letters: {sorted(guessed_letters)}")

    if mistakes == 3:
        print("Oh no, the snowman melted.")
        print("The word was: ", secret_word)
    elif remaining_letters == 0:
        print("Congratulations, you saved the snowman!")

    print("")
    play_again = input("Do you want to play again? (y, n) ")

    if play_again.lower() == "y":
        play_game()