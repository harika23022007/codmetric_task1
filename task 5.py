import random
choices = ["rock", "paper", "scissors"]
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
while True:
    print("\n--- Rock, Paper, Scissors ---")
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    play_again = int(input("Play again? \n1.yes\n2.no: "))
    if play_again != 1:
        print("Thanks for playing!")
        break
