from sys import stdin,stdout
from functools import lru_cache


def readln():
  return stdin.readline().rstrip()


def outln(n):
  stdout.write(str(n))
  stdout.write("\n")


binomial_cache = {}
def binomial(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


factorial_cache = {0: 1}
def factorial(n):
    result = 1
    if n in factorial_cache:
        return factorial_cache[n]
    for i in range(1, n + 1):
        result *= i
    return result



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


def main():
    T = int(readln())
    for _ in range(T):
        columns, rows = map(int, readln().split())
        c, r = map(int, readln().split())
        colCount = [0] * columns
        rowCount = [0] * rows
        dp = {}

        result = aztec(rows, columns, c, r, 0, 0, tuple(colCount), tuple(rowCount), dp)
        outln(result)


if __name__ == "__main__":
    main()