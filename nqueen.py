# --------------------------
#   Author: Subhashis Suara
#   Roll No.: UCSE19012
# --------------------------

# Ask user for the number of queens
num_of_queens = int(input("Enter the Number of Queens: "))

# Chessboard initialized with no pieces on it
chessboard = [[0] * num_of_queens for _ in range(num_of_queens)]

def is_vulnerable(i, j):
    """
    Check if the queen at square/position(i, j) is vulnerable to attacks
    """
    for m in range(0, num_of_queens):
        if chessboard[i][m] == 1 or chessboard[m][j] == 1:
            return True
    
    for m in range(0, num_of_queens):
        for n in range(0, num_of_queens):
            if (m + n == i + j) or (m - n == i - j):
                if chessboard[m][n] == 1:
                    return True

    return False

def solve_n_queen(num_of_unplaced_queens):
    """
    Solve the n-queen problem using backtracking
    """
    # If num_of_unplaced_queens is 0, we have solved the problem
    if num_of_unplaced_queens == 0:
        return True

    for i in range(0, num_of_queens):
        for j in range(0, num_of_queens):
            # Place queen if square is not vulnerable and not occupied
            if (not(is_vulnerable(i, j))) and (chessboard[i][j] != 1):
                chessboard[i][j] = 1
                
                # Recursively call the function to place the remaining unplaced queens
                if solve_n_queen(num_of_unplaced_queens - 1) == True:
                    return True
                
                # Backtracking
                chessboard[i][j] = 0

    return False

if __name__ == "__main__":
    if solve_n_queen(num_of_queens) == True:
        print ("Solution Found!")
        for i in range(0, num_of_queens):
            for j in range(0, num_of_queens):
                if chessboard[i][j] == 1:
                    print ("Q", end=" ")
                else:
                    print ("#", end=" ")
            print()
    else:
        print ("Solution Not Found!")