def aztec(G, c, r, rows, columns):
    if columns == rows and c == r and c == 1:
        return factorial(rows)
    dp = [[0] * (columns + 1) for _ in range(rows + 1)]
    dp[0][0] = 1

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if i < r or j < c:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j - c] * binomial(j, c) * binomial(i - 1, r - 1)

    return dp[rows][columns]


def binomial(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))


def factorial(number: int) -> int:
    return 1 if number == 0 or number == 1 else number * factorial(number - 1)


def main():
    T = int(input())
    for _ in range(T):
        columns, rows = map(int, input().split())
        c, r = map(int, input().split())
        G = [[0 for _ in range(columns)] for _ in range(rows)]

        result = aztec(G, c, r, rows, columns)
        print(result)


if __name__ == "__main__":
    main()