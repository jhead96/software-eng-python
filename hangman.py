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
    print("Spaces in the target word are denoted by a backslash.")
    input("Press any key to begin!")
    
    target_word = generate_word()
    guessed_word = "".join(["\\ " if c == " " else "_ " for c in target_word])

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
            print(letter_indexes)

        # Update remaining letters
        remaining_letters = remaining_letters.replace(current_letter, " ")

        # Check winner
        if (guessed_word == target_word):
            break

        guesses += 1
    
    # Check for winner
    if check_winner(guesses):
        print("You win!")
    else:
        print(f"You lose! The target word = {target_word}")
        print(display[guesses])


if __name__ == "__main__":
    main()