import random
import os
from display import display


def generate_word():
    filepath = r"resources\\countries.txt"

    with open(filepath, "r") as f:
        countries = f.readlines()
    
    chosen_country = random.choice(countries).strip("\n").upper()

    return chosen_country


def print_info(disp, guessed_letters, remaining_letters):

    print(f"{disp}")
    print(f"Guessed letters: {guessed_letters}")
    print(f"Remaining letters {remaining_letters}")


def obtain_valid_input(guessed_letters):
    current_letter = ""
    invalid_guess = True

    # Obtain valid guess
    while invalid_guess:
        current_letter = input("Guess a letter: ").upper()
        invalid_guess = (len(current_letter) != 1) or (not current_letter.isalpha()) or (current_letter in guessed_letters)
            
        if invalid_guess:
            print("Invalid guess!")
    
    return current_letter


def check_winner(guesses):
    
    if guesses == 10:
        return False
    else:
        return True

def main():

    print("Welcome to Hangman")
    input("Press any key to begin!")
    
    target_word = generate_word()
    # Maybe use dict for guessed word using index of char as key for each segment
    guessed_word = "".join([" " if c == " " else "_" for c in target_word])

    remaining_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    guessed_letters = ""

    guesses = 0
    while (guesses < 10):

        # Print game info
        print_info(display[guesses], guessed_letters, remaining_letters)
        print(target_word)
        print(guessed_word)

        # Obtain new guess
        current_letter = obtain_valid_input(guessed_letters)

        # Update guessed letters
        guessed_letters += current_letter

        # Update guessed word
        if current_letter in target_word:

            letter_indexes = [idx for idx, char in enumerate(target_word) if char == current_letter]
            guessed_word = "".join([current_letter if idx in letter_indexes else c for idx, c in enumerate(guessed_word)])

        # Update remaining letters
        remaining_letters = remaining_letters.replace(current_letter, " ")

        # Check winner
        if (guessed_word == target_word):
            break

        guesses += 1
    
    # Check for winner
    if check_winner(guesses):
        print(f"You win! The target word was {target_word}")

    else:
        print(f"You lose! The target word was {target_word}")
        print(display[guesses])


if __name__ == "__main__":
    main()