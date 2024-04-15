from collections import defaultdict

# Calcula os fatoriais previamente para evitar repetição de cálculos
factorials = [1]
for i in range(1, 101):
    factorials.append(factorials[-1] * i)

def aztec(rows: int, columns: int, c: int, r: int, i: int, j: int, colCount: tuple[int], rowCount: tuple[int], dp: dict[tuple[int], int]) -> int:
    #Casos mais simples
    if columns == rows and c == r and c == 1:
        return factorials[rows]
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

    key = colCount + (i, j)

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

def binomial(n: int, k: int) -> int:
    return factorials[n] // (factorials[k] * factorials[n - k])

def main() -> None:
    T = int(input())
    for _ in range(T):
        columns, rows = map(int, input().split())
        c, r = map(int, input().split())
        colCount = [0] * columns
        rowCount = [0] * rows
        dp = defaultdict(int)

        result = aztec(rows, columns, c, r, 0, 0, tuple(colCount), tuple(rowCount), dp)
        print(result)


if __name__ == "__main__":
    main()