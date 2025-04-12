import random

def play_round(player_choice):
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  print(f"You chose {player_choice}, the computer chose {computer_choice}")
  if player_choice == computer_choice:
    return "It's a tie!"
  elif (player_choice == "rock" and computer_choice == "scissors") or \
    (player_choice == "paper" and computer_choice == "rock") or \
    (player_choice == "scissors" and computer_choice == "paper"):
    return "You win!"
  else:
    return "You lose!"
while True:
            player_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ")
            if player_choice.lower() == "quit":
                break
            elif player_choice.lower() in ["rock", "paper", "scissors"]:
                print(play_round(player_choice.lower()))
            else:
                print("Invalid choice. Please try again.")