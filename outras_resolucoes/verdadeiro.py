from math import factorial

def aztec(rows, columns, c, r, i, j, colCount, rowCount, dp):
    #Casos mais simples
    if columns == rows and c == r and c == 1:
        return factorial(rows)
    if columns != rows and c != r:
        return binomial(rows, c)
    
    #Casos mais dificeis
    if i == rows:
        for col in range(columns):
            if colCount[col] != c:
                return 0
        return 1

    if j == columns:
        if rowCount[i] != r:
            return 0
        return aztec(rows, columns, c, r, i + 1, 0, colCount, rowCount, dp)

    key = colCount.copy()
    key.append(i)
    key.append(j)
    key = tuple(key)

    if key in dp:
        return dp[key]

    count = 0

    if colCount[j] < c and rowCount[i] < r:
        colCount[j] += 1
        rowCount[i] += 1
        count += aztec(rows, columns, c, r, i, j + 1, colCount, rowCount, dp)
        colCount[j] -= 1
        rowCount[i] -= 1

    count += aztec(rows, columns, c, r, i, j + 1, colCount, rowCount, dp)

    dp[key] = count

    return count

def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def main():
    T = int(input())
    for _ in range(T):
        columns, rows = map(int, input().split())
        c, r = map(int, input().split())
        colCount = [0] * columns
        rowCount = [0] * rows
        dp = {}

        result = aztec(rows, columns, c, r, 0, 0, colCount, rowCount, dp)
        print(result)


if __name__ == "__main__":
    main()