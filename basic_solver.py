board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def solve(brd):
    empty_space = find_zero(brd)
    if not empty_space:
        return True
    else:
        row, col = empty_space

    for i in range(1, 10):
        if possible(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

        brd[row][col] = 0

    return False


def possible(brd, num, pos):
    # check row
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    # check column
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # check square
    x0 = (pos[1] // 3) * 3
    y0 = (pos[0] // 3) * 3

    for i in range(0, 3):  # only three elements inside each row/column
        for j in range(0, 3):
            if brd[y0 + i][x0 + j] == num:
                return False

    return True


def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print(" | ---------------------------------- |")

        for j in range(len(brd[0])):
            if j % 3 == 0:
                print(" | ", end=" ")

            if j == 8:
                print(str(brd[i][j]) + " | ")
            else:
                print(str(brd[i][j]) + " ", end=" ")


def find_zero(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):

            if brd[i][j] == 0:
                return i, j  # (x,y) position of empty space found

    return None


print_board(board)
solve(board)
print("Sudoku Solved!")
print_board(board)
