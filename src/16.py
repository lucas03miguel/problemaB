def aztec(G, c, r, rows, columns):
    if columns == rows and c == r and c == 1:
        return factorial(rows)
    if columns != rows and c != r:
        return binomial(rows, c)


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