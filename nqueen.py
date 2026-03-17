N = 4

board = [["." for _ in range(N)] for _ in range(N)]

def print_board():
    for row in board:
        print(" ".join(row))
    print()

def aman(row, col):

    # cek kolom
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # cek diagonal kiri
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # cek diagonal kanan
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve(row):

    if row == N:
        print("SOLUSI DITEMUKAN\n")
        print_board()
        return True

    for col in range(N):

        print(f"Coba posisi ({row},{col})")

        if aman(row, col):
            board[row][col] = "Q"
            print("Letakkan Queen")
            print_board()

            if solve(row + 1):
                return True

            board[row][col] = "."
            print("Backtrack")
            print_board()

    return False


solve(0)
