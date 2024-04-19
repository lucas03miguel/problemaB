from scipy.special import comb
import numpy as np

def count_configurations(nr, nc, r, c):
    # Initialize DP table
    dp = np.zeros((c+1,) * nc, dtype=int)
    dp[(0,) * nc] = 1  # Base case: no cards placed
    
    # Iterate over each row
    for _ in range(nr):
        next_dp = np.zeros_like(dp)
        # Iterate over all possible column states
        for cols in np.ndindex(dp.shape):
            if dp[cols]:
                # Try placing r cards in this row
                for combination in comb_indices(nc, r):
                    new_cols = list(cols)
                    for i in combination:
                        new_cols[i] += 1
                    if max(new_cols) <= c:  # Ensure no column exceeds c cards
                        next_dp[tuple(new_cols)] += dp[cols]
        dp = next_dp
    return dp[(c,) * nc]

def comb_indices(n, k):
    """ Generate all indices combinations for placing k cards in n columns """
    if k == 0:
        yield ()
    elif n == 0:
        pass
    else:
        for indices in comb_indices(n-1, k):
            yield indices
        for indices in comb_indices(n-1, k-1):
            yield indices + (n-1,)

# Example usage:
nr, nc, r, c = 5, 10, 4, 2
result = count_configurations(nr, nc, r, c)
print("Number of valid configurations:", result)
