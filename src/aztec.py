count = 0

def solve_grid_card_assignments(c, r):
    global count
    grid = [[0 for _ in range(nc)] for _ in range(nr)]
    
    row_totals = [0] * nr
    col_totals = [0] * nc
    
    generate_assignments(grid, row_totals, col_totals, 0, 0, c, r)
    
    return count


def generate_assignments(grid, row_totals, col_totals, row, col, c, r):
    global count
    if row == nr:
        if is_valid_assignment(row_totals, col_totals, c, r):
            count += 1
        return
    
    if col == nc:
        generate_assignments(grid, row_totals, col_totals, row + 1, 0, c, r)
        return
    
    grid[row][col] = 1
    row_totals[row] = row_totals[row] + 1
    col_totals[col] = col_totals[col] + 1
    generate_assignments(grid, row_totals, col_totals, row, col + 1, c, r)
    
    grid[row][col] = 0
    row_totals[row] = row_totals[row] - 1
    col_totals[col] = col_totals[col] - 1
    generate_assignments(grid, row_totals, col_totals, row, col + 1, c, r)


def is_valid_assignment(row_totals, col_totals, c, r):
    for i in range(nr):
        if row_totals[i] != r:
            return False
    
    for j in range(nc):
        if col_totals[j] != c:
            return False
    
    return True


def main():
    global nc, nr
    T = int(input())
    for _ in range(T):
        nc, nr = map(int, input().split())
        c, r = map(int, input().split())

        result = solve_grid_card_assignments(c, r)
        print(result)


if __name__ == "__main__":
    main()
