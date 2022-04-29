import random
p1 = ""
p2 = ""
botChoice = 0
botChoice = random.randint(0,3)
if botChoice == 1:
  p2 = "rock"
elif botChoice == 2:
  p2 = "paper"
else:
  p2 = "scissors"
playerChoice = input("Rock, paper, or scissors?\n")
if "rock" in playerChoice:
  p1 = "rock"
elif "paper" in playerChoice:
  p1 = "paper"
else:
  p1 = "scissors"
print("The computer chose " + p2)
if p1 == "rock" and p2 == "rock":
  print("It's a tie!")
elif p1 == "rock" and p2 == "paper":
  print("You lost!")
elif p1 == "rock" and p2 == "scissors":
  print("You won!")
elif p1 == "paper" and p2 == "rock":
  print("You won!")
elif p1 == "paper" and p2 == "paper":
  print("It's a tie!")
elif p1 == "paper" and p2 == "scissors":
  print("You lost!")
elif p1 == "scissors" and p2 == "rock":
  print("You lost!")
elif p1 == "scissors" and p2 == "paper":
  print("You won!")
elif p1 == "scissors" and p2 == "scissors":
  print("It's a tie!")

