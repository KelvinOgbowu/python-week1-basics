import random
"""
Topics covered for this day
 1.) if/else statement
 2.) while loops
 3.) for loops

Task: Build a number guessing game where the computer picks from 1-100, and you guess

Additional/bonus task: 
1.) Add limit; Game ends after 7 tries
2.) Add "You are close" if within 5 numbers
3.) Push to your python-week1-basics repo on git

"""

name = input("Hello, please provide your name before you continue this session: ")
print(f"Welcome onboard {name}, we're pleased to have you with us today")
print(f"In this session, we're going to build a number guessing game and in this game, you are meant to guess a number stored in the computer array.")
print(f"If you guess the correct number, you would win a jackpot and if you don't you'll have to try again")
print(f"Note: You have only 7 attempts in one round")

# variable declaration
secret_number = random.randint(1, 100)
first_status = 0
attempts = 0
count = 0
while first_status == 0 and attempts < 7:
    game_status = int(input("If you understand the rules and you'll like to continue, press 1, if you want to terminate, press 0: "))            
    if game_status == 0:
        print(f"Thanks for your time, we hope to see you again")
        first_status += 1
    elif game_status == 1:
            while count == 0 and attempts < 7:
                print("Okay, now you're in the game, let's continue")
                guess_number = int(input("Please input your guess number(From 1 to 100): "))
                if abs(guess_number - secret_number) <= 5 and guess_number != secret_number:
                    print(f"You are close")
                    print(f"The secret number was {secret_number} and your guessed number was {guess_number}")
                    attempts += 1
                elif guess_number != secret_number:
                    print("Your guess was incorrect!!")
                    attempts += 1
                elif guess_number == secret_number:
                    print(f"The secret number was {secret_number} and your guessed number was {guess_number}")
                    print("Congratulations, you just won a jackpot of 5 million dollars")
                    attempts += 1
                    print(f"You guessed the number in {attempts} attempts")

                    count += 1
                    game_status = 0
                    first_status = first_status + 1
                    break

    else:
            print(f"{game_status} is not a valid input")
            print(f"Please enter a valid input to continue")

print("Game - over!!")
print(f"You had {attempts} trials")