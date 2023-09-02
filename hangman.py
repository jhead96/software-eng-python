import random
import os
from display import display


def generate_word():
    filepath = r"resources\\countries.txt"

    with open(filepath, "r") as f:
        countries = f.readlines()
    
    chosen_country = random.choice(countries).strip("\n")

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



    return current_letter

def clear_console():
    os.system("cls")

def check_winner(guesses):
    
    if guesses == 10:
        print("You lose!")
    else:
        print("You win!")

def main():

    input("Welcome to Hangman, press any key to begin!")
    
    target_word = generate_word()

    remaining_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    guessed_letters = ""

    
    guesses = 0
    while guesses < 10:

        # Print game info
        print_info(display[guesses], guessed_letters, remaining_letters)

        # Obtain new guess
        current_letter = obtain_valid_input(guessed_letters)

        
        guessed_letters += current_letter
        
        guesses += 1



if __name__ == "__main__":
    main()