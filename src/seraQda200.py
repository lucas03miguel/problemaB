from sys import stdin, stdout # Mais rapidos que input() e print()
import ctypes                # Por causa do unsigned int

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

def aztec(rows, columns, c, r, i, j, colCount, rowCount, dp):
    if i == rows:
        return ctypes.c_uint(all(x == c for x in colCount)).value

    if j == columns:
        if rowCount[i] != r:
            return ctypes.c_uint(0).value
        sortedColCount = sorted(colCount)
        key = tuple(sortedColCount + [i])
        if key in dp:
            return dp[key]
        result = aztec(rows, columns, c, r, i + 1, 0, colCount, rowCount, dp)
        dp[key] = result
        return result

    count = ctypes.c_uint(0).value

    if colCount[j] < c and rowCount[i] < r:
        colCount[j] += ctypes.c_uint(1).value
        rowCount[i] += ctypes.c_uint(1).value
        count += aztec(rows, columns, c, r, i, j + 1, colCount, rowCount, dp)
        colCount[j] -= ctypes.c_uint(1).value
        rowCount[i] -= ctypes.c_uint(1).value

    count += aztec(rows, columns, c, r, i, j + 1, colCount, rowCount, dp)

    return count

def main():
    T = int(readln())
    results = []

    for _ in range(T):
        columns, rows = map(int, readln().split())
        c, r = map(int, readln().split())

        if c > rows or r > columns or c < 1 or c > 7 or r < 1 or r > 7 or columns < 1 or columns > 24 or rows < 1 or rows > 24:
            results.append(ctypes.c_uint(0).value)
            continue

        colCount = [ctypes.c_uint(0).value] * columns
        rowCount = [ctypes.c_uint(0).value] * rows
        dp = {}

        result = aztec(rows, columns, c, r, 0, 0, colCount, rowCount, dp)
        results.append(result)

    for result in results:
        outln(result)

if __name__ == "__main__":
    main()