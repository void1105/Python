import random

low = 1
high = 100

number = random.randint(low, high)
guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {low} and {high}.")


while is_running:
    guess = input("Make a guess: ")
    

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("This number is out of bounds.")
            print(f"I'm thinking of a number between {low} and {high}.")

        elif guess < number:
            print("Too low! Try again!")

        elif guess > number:
            print("Too high! Try again!")

        else:
            print(f"CONGRATULATIONS! You've guessed the number {number} in {guesses} attempts.")
            is_running = False
    else:
        print("please enter a valid guess")
        print(f"I'm thinking of a number between {low} and {high}.")
       
