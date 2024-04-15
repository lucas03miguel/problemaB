#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

long long binomial(int n, int k) {
    vector<long long> dp(k + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = min(i, k); j > 0; j--) {
            dp[j] = dp[j] + dp[j - 1];
        }
    }
    return dp[k];
}

long long aztec(int n, int m, int x, int y) {
    if (m == n && x == y && x == 1) {
        long long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
    if (m != n && x != y) {
        return binomial(n, x);
    }

    int total_zeros = x * m;
    if (total_zeros != y * n) {
        return 0;
    }

    int matrix_size = n * m;
    vector<int> zero_positions(matrix_size);
    iota(zero_positions.begin(), zero_positions.end(), 0);

    long long valid_combinations = 0;
    do {
        vector<vector<int>> matrix(n, vector<int>(m, 0));
        for (int i = 0; i < total_zeros; i++) {
            int pos = zero_positions[i];
            int row = pos / m;
            int col = pos % m;
            matrix[row][col] = 1;
        }

        bool valid_rows = all_of(matrix.begin(), matrix.end(), [y](const vector<int>& row) {
            return accumulate(row.begin(), row.end(), 0) == y;
        });

        bool valid_cols = true;
        for (int j = 0; j < m; j++) {
            int col_sum = 0;
            for (int i = 0; i < n; i++) {
                col_sum += matrix[i][j];
            }
            if (col_sum != x) {
                valid_cols = false;
                break;
            }
        }

        if (valid_rows && valid_cols) {
            valid_combinations++;
        }
    } while (next_permutation(zero_positions.begin(), zero_positions.end()));

    return valid_combinations;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int columns, rows;
        cin >> columns >> rows;
        int c, r;
        cin >> c >> r;
        vector<vector<int>> G(rows, vector<int>(columns, 0));

        long long result = aztec(rows, columns, c, r);
        cout << result << endl;
    }

    return 0;
}
