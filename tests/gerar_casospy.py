def aztec_iterative(rows, columns, c, r):
    # Initialize DP table
    dp = [[0] * (columns + 1) for _ in range(rows + 1)]
    dp[0][0] = 1  # Base case: one way to fill a 0x0 grid

    # Fill the DP table
    for i in range(rows + 1):
        for j in range(columns + 1):
            if i > 0:
                dp[i][j] += dp[i-1][j]  # Ways to extend from the previous row
            if j > 0:
                dp[i][j] += dp[i][j-1]  # Ways to extend from the previous column

    return dp[rows][columns]

def main():
    T = int(input())
    for _ in range(T):
        columns, rows = map(int, input().split())
        c, r = map(int, input().split())
        result = aztec_iterative(rows, columns, c, r)
        print(result)

if __name__ == "__main__":
    main()
