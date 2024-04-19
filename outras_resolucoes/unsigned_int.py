from sys import stdin, stdout # Mais rapidos que input() e print()
import ctypes                # Por causa do unsigned int

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

# Calcula os fatoriais previamente para evitar repetição de cálculos
factorials = [ctypes.c_uint(1).value]

for i in range(1, 25):
    factorials.append(ctypes.c_uint(factorials[-1] * i).value)

def aztec(rows, columns, c, r, i, j, colCount, rowCount, dp):
    # Casos mais simples
    if columns == rows == 1:
        return ctypes.c_uint(1).value
    if columns == rows and c == r and c == 1:
        return ctypes.c_uint(factorials[rows]).value
    if columns != rows and c != r:
        return ctypes.c_uint(binomial(rows, c)).value
    
    # Casos mais difíceis
    if i == rows:
        for col in range(columns):
            if colCount[col] != c:
                return ctypes.c_uint(0).value
        return ctypes.c_uint(1).value

    if j == columns:
        if rowCount[i] != r:
            return ctypes.c_uint(0).value
        return aztec(rows, columns, c, r, i + 1, 0, colCount, rowCount, dp)

    key = colCount + (i, j)

    if key in dp:
        return dp[key]

    count = ctypes.c_uint(0).value

    if colCount[j] < c and rowCount[i] < r:
        newColCount = list(colCount)
        newRowCount = list(rowCount)
        newColCount[j] += 1
        newRowCount[i] += 1
        count += aztec(rows, columns, c, r, i, j + 1, tuple(newColCount), tuple(newRowCount), dp)

    count += aztec(rows, columns, c, r, i, j + 1, colCount, rowCount, dp)

    dp[key] = count

    return count

def binomial(n, k):
    return ctypes.c_uint(factorials[n] // (factorials[k] * factorials[n - k])).value

def main():
    T = int(readln())
    for _ in range(T):
        columns, rows = map(int, readln().split())
        c, r = map(int, readln().split())
        colCount = [ctypes.c_uint(0).value] * columns
        rowCount = [ctypes.c_uint(0).value] * rows
        dp = {}

        result = aztec(rows, columns, c, r, 0, 0, tuple(colCount), tuple(rowCount), dp)
        outln(result)

if __name__ == "__main__":
    main()