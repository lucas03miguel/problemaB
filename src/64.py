from sys import stdin, stdout
import ctypes

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

# Caching for binomial coefficients
binomial_cache = {}
def binomial(n, k):
    if k > n:
        return ctypes.c_uint(0).value
    if k == 0 or k == n:
        return ctypes.c_uint(1).value
    if (n, k) in binomial_cache:
        return binomial_cache[(n, k)]
    result = ctypes.c_uint(binomial(n-1, k-1) + binomial(n-1, k)).value
    binomial_cache[(n, k)] = result
    return result

def factorial(n):
    result = ctypes.c_uint(1).value
    for i in range(1, n + 1):
        result = ctypes.c_uint(result * i).value
    return result

def aztec(rows, columns, c, r, i, j, missingCol, missingRow, dp):
    if i == rows:
        return ctypes.c_uint(all(x == ctypes.c_uint(0).value for x in missingCol)).value

    if j == columns:
        if missingRow[i] == ctypes.c_uint(0).value:
            return aztec(rows, columns, c, r, i + 1, 0, missingCol, missingRow, dp)
        return ctypes.c_uint(0).value

    key = (tuple(missingCol), tuple(missingRow), i, j)
    if key in dp:
        return dp[key]

    count = ctypes.c_uint(0).value

    if missingCol[j] > ctypes.c_uint(0).value and missingRow[i] > ctypes.c_uint(0).value:
        missingCol[j] -= ctypes.c_uint(1).value
        missingRow[i] -= ctypes.c_uint(1).value
        count = ctypes.c_uint(count + aztec(rows, columns, c, r, i, j + 1, missingCol, missingRow, dp)).value
        missingCol[j] += ctypes.c_uint(1).value
        missingRow[i] += ctypes.c_uint(1).value

    count = ctypes.c_uint(count + aztec(rows, columns, c, r, i, j + 1, missingCol, missingRow, dp)).value

    dp[key] = count
    return count

def main():
    T = int(readln())
    for _ in range(T):
        columns, rows = map(int, readln().split())
        c, r = map(int, readln().split())
        missingCol = [ctypes.c_uint(c).value] * columns
        missingRow = [ctypes.c_uint(r).value] * rows
        dp = {}

        result = aztec(rows, columns, c, r, 0, 0, missingCol, missingRow, dp)
        outln(result)

if __name__ == "__main__":
    main()
