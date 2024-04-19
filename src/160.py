from sys import stdin, stdout

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

def aztec(rows, columns, c, r, i, j, colCount, rowCount, dp):
    if rows * r != columns * c:
        return 0
    
    if i == rows:
        return all(x == c for x in colCount)

    if j == columns:
        if rowCount[i] != r:
            return 0
        sortedColCount = tuple(sorted(colCount) + [i])
        if sortedColCount in dp:
            return dp[sortedColCount]
        result = aztec(rows, columns, c, r, i + 1, 0, colCount, rowCount, dp)
        dp[sortedColCount] = result
        return result

    count = 0
    if colCount[j] < c and rowCount[i] < r:
        colCount[j] += 1
        rowCount[i] += 1
        count += aztec(rows, columns, c, r, i, j + 1, colCount, rowCount, dp)
        colCount[j] -= 1
        rowCount[i] -= 1

    count += aztec(rows, columns, c, r, i, j + 1, colCount, rowCount, dp)
    return count


def main():
    T = int(readln())

    for _ in range(T):
        columns, rows = map(int, readln().split())
        c, r = map(int, readln().split())

        if c > rows or r > columns or c < 1 or c > 7 or r < 1 or r > 7 or columns < 1 or columns > 24 or rows < 1 or rows > 24:
            outln(0)
            continue

        colCount = [0] * columns
        rowCount = [0] * rows
        dp = {}

        result = aztec(rows, columns, c, r, 0, 0, colCount, rowCount, dp)
        outln(result)


if __name__ == "__main__":
    main()