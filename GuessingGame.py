import random
sword = str(input("Please enter the word for the player to guess: "))
notries = int(input("How many tries would you like the player to have: "))
hintarray = [""]
hintbool = False
nohints = int(input("How many hints would you like the player to have: "))
hintgiven = 0
while hintgiven < nohints and not hintbool:
  hintarray.append(input("Please enter a hint: "))
  hintgiven += 1
guess = ""
guessc = 0
outofg = False
triesc = notries
com = input("To start the game, please enter 'start' : ")
if com == 'start':
    print("The game is starting in.. \n 5 \n 4 \n 3 \n 2 \n 1 \nGuess the chosen word in " + str(notries) + " tries or you lose!")
    while guess != sword and not outofg :
        if guessc < notries:
            print("Hint: " + random.choice(hintarray))
            guess = input("Enter your guess: ")
            guessc += 1
            print("You have " + str(triesc - 1) + " tries left")
            triesc -= 1
        else:
            if guess != sword:
                outofg = True
                print("You are out of guesses!")
    else:
        if guess == sword:
            print("Congrats, You guessed the word!")

