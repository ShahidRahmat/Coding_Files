#Simple Snake Game, fixed starting and ending point

def print_map():
    max_row = len(map)
    max_col = len(map[0])
    print(("+---" * 5) + "+")
    for r in range(max_row):
        for c in range(max_col):
            print("| {}".format(map[r][c]), end=' ')
        print("|")
        print(("+---" * 5) + "+")
map = [[' ', ' ', ' ', ' ', 'A'],\
       [' ', ' ', ' ', ' ', ' '],\
       [' ', ' ', ' ', ' ', ' '],\
       [' ', ' ', ' ', ' ', ' '],\
       ['S', ' ', ' ', ' ', ' ']]
print("Your goal is to navigate the snake(S) to the apple(A) with the commands below.")
print("U:Up\nD:Down\nL:Left\nR:Right")
print_map()
while map[0][-1] == "A":
    for i in map:
        for j in i:
            if j == 'S':
                length = i.index("S")
                height = map.index(i)
    dir = str(input("Enter a direction: "))
    dir = dir.upper()
    if dir == "U":
        if height == 0:
            print("Not a valid command.")
            continue
        else:
            map[height][length] = " "
            map[(height - 1)][length] = "S"
    if dir == "D":
        if height == 4:
            print("Not a valid command.")
            continue
        else:
            map[height][length] = " "
            map[(height +1)][length] = "S"
    if dir == "L":
        if length == 0:
            print("Not a valid command.")
            continue
        else:
            map[height][length] = " "
            map[height][(length-1)] = "S"
    if dir == "R":
        if length == 4:
            print("Not a valid command.")
            continue
        else:
            map[height][length] = " "
            map[height][(length+1)] = "S"
    print_map()
print("The game has ended.")
