from itertools import combinations
from math import factorial

def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def aztec(n, m, x, y):
    if m == n and x == y and x == 1:
        return factorial(n)
    if m != n and x != y:
        return binomial(n, x)
    
    print("bi: ", binomial(n, x))
    print("fac: ", factorial(n))


    total_zeros = x * m
    if total_zeros != y * n:
        return 0

    matrix_size = n * m
    dp = [[0] * (y + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(y + 1):
            for k in range(min(j, m) + 1):
                dp[i][j] += dp[i - 1][j - k] * binomial(m, k)

    print(dp)
    valid_combinations = 0
    for positions in dp:
        matrix = [[0] * m for _ in range(n)]
        for pos in positions:
            row, col = divmod(pos, m)
            matrix[row][col] = 1

        if all(sum(row) == y for row in matrix) and all(sum(col) == x for col in zip(*matrix)):
            valid_combinations += 1
        
    return valid_combinations


def main():
    T = int(input())
    for _ in range(T):
        columns, rows = map(int, input().split())
        c, r = map(int, input().split())
        G = [[0 for _ in range(columns)] for _ in range(rows)]

        result = aztec(rows, columns, c, r)
        print(result)


if __name__ == "__main__":
    main()