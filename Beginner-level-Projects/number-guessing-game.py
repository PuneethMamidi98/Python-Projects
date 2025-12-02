# Number Guessing Game

import random

def NumberGuessGame():
    print("Welcome to Number Guessing Game !!!")
    # levels dict which contains difficulty levels and available attempts 
    levels = {
        "Easy":{"available_attempts":10, "range":15},
        "Medium":{"available_attempts":5, "range":25},
        "Hard":{"available_attempts":3, "range":50},
        "Extreme":{"available_attempts":1, "range":100}
        }
    # User Choose Difficulty Level
    chosen_level = input("Choose the Difficulty Level: Easy / Medium / Hard / Extreme :  ").strip().title()
    # For invalid level input
    while chosen_level not in levels:
        print("Alert!! Enter valid input level")
        chosen_level = input("Choose the Difficulty Level: Easy / Medium / Hard / Extreme :  ").strip().title()
    # Available attempts and range for each difficulty level
    available_attempts = levels[chosen_level]["available_attempts"]
    number_range = levels[chosen_level]["range"]
    print()
    print(f"===== Difficulty Level - {chosen_level} ==> Available attempts: {available_attempts} =====")
    print()
    # Random number in between based on difficulty level
    # If easy - ranges - 1 to 15, medium - 1 to 25, hard - 1 to 50, extreme 1 - 100
    actual_number = random.randint(1,number_range)
    # attempts validity
    attempts = 0
    # winner flag
    winner = False
    remaining_attempts = available_attempts
    while available_attempts > attempts:
        # User guess number
        print(f"Remaining attempts: {remaining_attempts}")
        print()
        guess_number = input(f"Guess the number in between 1 to {number_range}: ")
        print()
        if not guess_number.isdigit():
            print("Alert!!, Invalid input, Enter number only!! ")
            continue
        guess = int(guess_number)
        if guess == actual_number:
            winner = True
            break
        elif guess < actual_number:
            print("OH! OH!, Guess is too low!!!")
        else:
            print("OOPS!!, Guess is too high!!! ")
        attempts += 1        
        remaining_attempts -= 1
        if remaining_attempts == 0:
            break
    if winner:
         print()
         print("Hurray!!! You guessed the number!!")
    else:
        print()
        print(f"Game Over!!!, Out Of Attempts")     

while True:
    NumberGuessGame()
    play_again = input("Play again - yes/no:  ")
    if play_again != "yes":
        break    
