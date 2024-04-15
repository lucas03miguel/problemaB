from functools import lru_cache

@lru_cache(maxsize=None)
def binomial(n, k):
    if k == 0 or k == n:
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)

def aztec(rows, columns, c, r, i, j, colCount, rowCount, dp):
    # Casos mais simples
    if columns == rows == 1:
        return 1
    if columns == rows and c == r and c == 1:
        return factorial(rows)
    if columns != rows and c != r:
        return binomial(rows, c)
    
    # Casos mais difíceis
    if i == rows:
        for col in range(columns):
            if colCount[col] != c:
                return 0
        return 1

    if j == columns:
        if rowCount[i] != r:
            return 0
        return aztec(rows, columns, c, r, i + 1, 0, colCount, rowCount, dp)

    key = (tuple(colCount), i, j)

    if key in dp:
        return dp[key]

    count = 0

    if colCount[j] < c and rowCount[i] < r:
        newColCount = list(colCount)
        newRowCount = list(rowCount)
        newColCount[j] += 1
        newRowCount[i] += 1
        count += aztec(rows, columns, c, r, i, j + 1, tuple(newColCount), tuple(newRowCount), dp)

    count += aztec(rows, columns, c, r, i, j + 1, colCount, rowCount, dp)

    dp[key] = count

    return count

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    T = int(input())
    for _ in range(T):
        columns, rows = map(int, input().split())
        c, r = map(int, input().split())
        colCount = [0] * columns
        rowCount = [0] * rows
        dp = {}

        result = aztec(rows, columns, c, r, 0, 0, tuple(colCount), tuple(rowCount), dp)
        print(result)

if __name__ == "__main__":
    main()