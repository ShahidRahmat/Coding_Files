import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input( " Play rock, paper or scissors with a robot. Choose your move by typing rock, paper or scissors: \n")
game = ['rock', 'paper', 'scissors']
print("You chose " + choice)
if choice == 'rock':
  print(rock)
elif choice == 'paper':
  print(paper)
elif choice == 'scissors':
  print(scissors)
else:
  print("Choice is invalid.")

bot = random.choice(game)
print("The bot chose " + bot)
if bot == 'rock':
  print(rock)
elif bot == 'paper':
  print(paper)
elif bot == 'scissors':
  print(scissors)

if bot == choice:
  print("The game ends in a tie.")
elif bot == 'paper' and choice == 'scissors':
  print("You have won!")
elif bot == 'paper' and choice == 'rock':
  print("You have lost :( ")
elif bot == 'scissors' and choice == 'rock':
  print("You have won!")
elif bot == 'scissors' and choice == 'paper':
  print("You have lost :( ")
elif bot == 'rock' and choice == 'paper':
  print("You won!")
elif bot == 'rock' and choice == 'scissors':
  print("You lost :( ")
else:
  print("Error")