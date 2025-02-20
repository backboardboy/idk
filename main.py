board_columns = [["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"]]

def move(player, column):
    for i, v in enumerate(board_columns[column-1]):
        if v == "-": 
            first_open_space = i
            break
    board_columns[column-1][first_open_space] = player

def draw_board():
    for i in range(5,-1,-1):
        row = ""
        for column in board_columns:
            row += column[i]
            row += " "
        print(f"| {row}|")
    print(" --------------- ")
    print("  1 2 3 4 5 6 7  ")

def check_win():
    board_array = []
    for column in board_columns:
        board_array += column
    
    #columns
    streak = 1
    previous = "-"
    for i, v in enumerate(board_array):
        if i%6 == 1 and i != 1:
            streak = 1
            previous = "-"
        if v == previous and v != "-":
            streak += 1
        else:
            streak = 1
        if streak >= 4:
            return v
        previous = v
    
    #rows
    for row in range(6):
        streak = 1
        previous = "-"
        for column in range(7):
            v = board_array[column*6 + row]
            if v == previous and v != "-":
                streak += 1
            else:
                streak = 1
            if streak >= 4:
                return v
            previous = v
    
    #upright
    starting_spots = [1,2,3,7,8,9,13,14,15,19,20,21]
    for starting_spot in starting_spots:
        streak = 0
        previous = "-"
        for i in range(starting_spot, 43, 7):
            v = board_array[i-1]
            if v == previous and v != "-":
                streak += 1
            else:
                streak = 1
            if streak >= 4:
                return v
            previous = v
            if i%6 == 0:
                break
        
    #upleft
    starting_spots = [19,20,21,25,26,27,31,32,33,37,38,39]
    for starting_spot in starting_spots:
        streak = 0
        previous = "-"
        for i in range(starting_spot, 0, -5):
            v = board_array[i-1]
            if v == previous and v != "-":
                streak += 1
            else:
                streak = 1
            if streak >= 4:
                return v
            previous = v
            if i%6 == 0:
                break
    


player = "x"
draw_board()
print()
while True:
    column = int(input(player + " turn: column (1-7): "))
    move(player, column)
    draw_board()
    winner = check_win()
    if winner:
        print(f"{winner} won")
        break
    
    if player == "x":
        player = "o"
    else:
        player = "x"
