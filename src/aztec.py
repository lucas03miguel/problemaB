def aztec(G, c, r, rows, columns):
    return "oi"






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