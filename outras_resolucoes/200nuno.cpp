#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm> 

using namespace std;

struct VectorHash {
    size_t operator()(const vector<int>& v) const {
        size_t seed = 0;
        for (int i : v) {
            seed = seed * 31 + i; 
        }
        return seed;
    }
};

unsigned long long aztec(int rows, int columns, int c, int r, int i, int j, vector<int>& colCount, vector<int>& rowCount, unordered_map<vector<int>, unsigned long long, VectorHash>& dp) {
    if (i == rows) {
        for (int col = 0; col < columns; col++) {
            if (colCount[col] != c)
                return 0;
        }
        return 1;
    }

    if (j == columns) {
        if (rowCount[i] != r)
            return 0;
        vector<int> sortedColCount = colCount;
        sort(sortedColCount.begin(), sortedColCount.end());
        vector<int> key = sortedColCount;
        key.push_back(i);
        auto it = dp.find(key);
        if (it != dp.end()) {
            return it->second;
        }
        unsigned long long result = aztec(rows, columns, c, r, i + 1, 0, colCount, rowCount, dp);
        dp[key] = result;
        return result;
    }

    unsigned long long count = 0;

    if (colCount[j] < c && rowCount[i] < r) {
        colCount[j]++;
        rowCount[i]++;
        count += aztec(rows, columns, c, r, i, j + 1, colCount, rowCount, dp);
        colCount[j]--;
        rowCount[i]--;
    }

    count += aztec(rows, columns, c, r, i, j + 1, colCount, rowCount, dp);

    return count;
}

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int columns, rows;
        cin >> columns >> rows;

        int c, r;
        cin >> c >> r;

        if (c > rows || r > columns || c < 1 || c > 7 || r < 1 || r > 7 || columns < 1 || columns > 24 || rows < 1 || rows > 24) {
            cout << "0" << endl;
            continue;
        }

        vector<int> colCount(columns, 0);
        vector<int> rowCount(rows, 0);
        unordered_map<vector<int>, unsigned long long, VectorHash> dp;

        unsigned long long result = aztec(rows, columns, c, r, 0, 0, colCount, rowCount, dp);
        cout << result << endl;
    }

    return 0;
}