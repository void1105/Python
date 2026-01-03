import random

print("Welcome to Rock, Paper, Scissors Game!")
options = ("rock", "paper", "scissors")

running = True

while running: 
    choice = None
    option = random.choice(options)

    while choice not in options:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if choice == option:
        print("Its a TIE! Both chose", choice)  
    elif choice == "rock" and option == "paper":
        print(f"You chose {choice}, and the computer chose {option}. You LOSE!")
    elif choice == "paper" and option == "rock":
        print(f"You chose {choice}, and the computer chose {option}. You WIN!")
    elif choice == "paper" and option == "scissors":
        print(f"You chose {choice}, and the computer chose {option}. You LOSE!")
    elif choice == "scissors" and option == "paper":
        print(f"You chose {choice}, and the computer chose {option}. You WIN!")

    elif choice == "scissors" and option == "rock":
        print(f"You chose {choice}, and the computer chose {option}. You LOSE!")

    elif choice == "rock" and option == "scissors":
        print(f"You chose {choice}, and the computer chose {option}. You WIN!")

    play_again = input("Do you want to play again?(y/n): ").lower()

    if not play_again == "y":
        running = False

print("Thanks for playing! Goodbye!")

    
   



   
   
   

