import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column or diagonals
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(N):
    def backtrack(board, row):
        if row == N:
            # Print the solution
            for i in range(N):
                print("".join('.' if board[i] != j else 'Q' for j in range(N)))
            print()
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    board = [-1] * N
    backtrack(board, 0)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

if __name__ == "__main__":
    main()

