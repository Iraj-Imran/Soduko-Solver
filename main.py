grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 2, 8, 0, 1, 0, 0]
        ]


def possibility(num, row, column):
    global grid
    for i in range(9):
        if grid[row][i] == num:   # checks if num present in row, then column
            return False
    for i in range(9):
        if grid[i][column] == num:
            return False

    row_0 = (row // 3) * 3       # gives the top left index positions for square in which num is present
    column_0 = (column // 3) * 3
    for i in range(3):           # iterates through the 3x3 in that small square
        for j in range(3):
            if grid[row_0 + i][column_0 + j] == num:
                return False
    return True


count = 0


def solver():
    global grid
    global count

    for row in range(9):    # checks all 9x9
        for column in range(9):
            if grid[row][column] == 0:
                for num in range(1, 10):
                    if possibility(num, row, column):
                        grid[row][column] = num
                        solver()               # recursion is used, calling solver(), using backtracking to replace
                        grid[row][column] = 0  # wrong solutions with 0
                return

    input("Show solution")
    count += 1

    printer()


def printer():
    for c in range(9):
        print(grid[c], "\n")


solver()
if count == 1:
    print("This Sudoko has ", count, "solution")
else:
    print("This Sudoko has ", count, "solutions")
print("No more solution")
