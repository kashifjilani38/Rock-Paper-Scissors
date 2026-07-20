import random

# Dictionary of choices
choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

print("===== Rock Paper Scissors Game =====")

while True:
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("Press any other key to Exit")

    choice = input("Enter your choice (1-3): ")

    # Exit if input is not 1, 2, or 3
    if choice not in ["1", "2", "3"]:
        print("\nThanks for playing!")
        break

    user = choices[int(choice)]

    # Computer randomly selects 1, 2, or 3
    computer = random.randint(1, 3)
    computer_choice = choices[computer]

    print("\nYou chose:", user)
    print("Computer chose:", computer_choice)

    # Determine the winner
    if user == computer_choice:
        print("Result: It's a Tie!")
    elif (user == "Rock" and computer_choice == "Scissors") or \
         (user == "Paper" and computer_choice == "Rock") or \
         (user == "Scissors" and computer_choice == "Paper"):
        print("Result: You Win!")
    else:
        print("Result: Computer Wins!")