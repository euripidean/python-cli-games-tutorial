# Import the random method from the randint module
from random import randint
import time

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

#functions

#Starting Message
def starting_message():
  print("Get ready to play Bear, Ninja, Cowboy!")
  time.sleep(3)
  instructions = input("Would you like to see some instructions? (y/n?) > ")
  if instructions == "y":
    print("Bear, Ninja, Cowboy is an exciting game of strategy and skill! Pit your wit against the computer! Choose a player: Bear, Ninja, or Cowboy. The computer chooses a player. Bear eats Ninja, Ninja defeats Cowboy and cowboy shoots bear.")
  else:
    print("An old hand! Let's play.")

#Ending Message
def ending_message():
  print("*" *40)
  print("Thanks for playing!")
  print("*" *40)

#Determine Who Wins
def declare_winner(computer, player):
  if computer == player:
      print("DRAW!")
  elif computer == "Cowboy":
      if player == "Bear":
        print("You lose!", computer, "shoots", player)
      else: # computer is cowboy, player is ninja
        print("You win!", player, "defeats", computer)
        declare_winner.score +=1
  elif computer == "Bear":
      if player == "Cowboy":
        print("You win!", player, "shoots", computer)
        declare_winner.score +=1
      else: # computer is bear, player is ninja
        print("You lose!", computer, "eats", player)
  elif computer == "Ninja":
      if player == "Cowboy":
        print("You lose!", computer, "defeats", player)
      else: # computer is ninja, player is bear
        print("You win!", player, "eats", computer)
        declare_winner.score +=1
      player = False
      computer = roles[randint(0,2)]

#start game
starting_message()
declare_winner.score = 0
total_games = 0

#user inputs their choice
player = False

#game play loop
total_games = 0
while player == False:
    # Get player input
    player = input("Bear, Ninja, or Cowboy? > ") 
    while player not in roles:
        print(f" {player} isn't up for the fight! Please enter one of the three options below.")
        player = input("Bear, Ninja, or Cowboy? > ")
        continue
    else:
        declare_winner(computer, player)
        total_games += 1
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
        print(f"Your final score was {declare_winner.score} out of {total_games}!")
        ending_message()
        break