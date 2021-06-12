print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
cr = input("You come to a cross road. Where do you want to go? Type 'left' or 'right': ")
if cr != 'left':
  print("You fell into a hole. Game over")
elif cr == 'left':
  lake = input("You chose the left road. You now find yourself facing a lake. Do you want to wait for a boat or swim across? Type 'swim' or 'wait': ")
  
  if lake != 'wait':
    print("You have been attacked by a trout. Game Over.")
  elif lake == 'wait':
    door = input("You have crossed the lake safely to another island. Before you stands 3 doors. A red door, a blue door and a yellow door. Which do you want to go through? Type 'red', 'blue' or 'yellow': ")

    if door == 'red':
      print("You open the red door and fire gushed out. You are burned to death. Game Over.")
    elif door == 'blue':
      print("You open the blue door and beasts rush out and swarm you. You are beaten in a couple of seconds. Game Over. ")
    elif door == 'yellow':
      print("You open the yellow door to a bright light. You peer closer and its a treasure chest. You won!")
    else:
      print("Game Over.")
  
