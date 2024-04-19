from math import factorial

def binomial(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))

def aztec(rows: int, columns: int, c: int, r: int, i: int, j: int, colCount: list[int], rowCount: list[int], dp: dict[tuple[int, ...], int]) -> int:
    # Casos mais faceis
    if columns == rows == 1:
        return 1
    if columns == rows and c == r and c == 1:
        return factorial(rows)
    if columns != rows and c != r:
        return binomial(rows, c)
    
    # Casos mais dificeis
    if i == rows:
        return int(all(count == c for count in colCount))

    if j == columns:
        if rowCount[i] != r:
            return 0
        return aztec(rows, columns, c, r, i + 1, 0, colCount, rowCount, dp)

    key = tuple(colCount + [i, j])

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

def main():
    T = int(input())

    for _ in range(T):
        columns, rows = map(int, input().split())
        c, r = map(int, input().split())

        if not (1 <= c <= min(rows, 7) and 1 <= r <= min(columns, 7) and 1 <= columns <= 24 and 1 <= rows <= 24):
            print("0")
            continue

        colCount = [0] * columns
        rowCount = [0] * rows
        dp = {}

        result = aztec(rows, columns, c, r, 0, 0, colCount, rowCount, dp)
        print(result)

if __name__ == "__main__":
    main()