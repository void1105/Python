questions = ("How many elements are there in the periodic table?: ",
            "Which animal lays the largest egg?: ",
            "Which is the most abundant gas in Earth's atmosphere; ",
            "How many bones are there in the human body?: ",
            "Which planet is the hottest planet in the solar system?: "
    )

options =   (("A. 116", "B. 117", "C. 118", "D. 119"),
            ("A. Whale", "B.Crocodile ", "C. Elephant", "D. Ostrich"),
            ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
            ("A. 206", "B. 207", "C. 208", "D. 209"),
            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []

scores = 0

question_nums = 0


for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_nums]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    while guess not in ("A","B", "C", "D"):
            print("Invalid input!")
            guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_nums]:
        scores += 1
        print("CORRECT!")   
    else:
        print("WRONG!") 
        print(f"The correct answer is {answers[question_nums]}")    
        


    question_nums += 1

print("-------------------------------")
print("           RESULLTS            ")
print("-------------------------------")

print("Answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()

for guess in guesses:
    print(guess, end = " ")

print()
scores = int(scores / len(questions) * 100)
print(f"Your score is {scores}%.")
