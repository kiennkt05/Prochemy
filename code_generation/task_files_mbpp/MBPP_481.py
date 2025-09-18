# MBPP/481
### Completion
def is_subset_sum(set, n, sum):
    # Create a 2D array to store the results of subproblems
    subset = [[False for _ in range(sum + 1)] for _ in range(n + 1)]
    
    # If sum is 0, then answer is true (empty subset)
    for i in range(n + 1):
        subset[i][0] = True

    # Fill the subset table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if set[i - 1] > j:
                subset[i][j] = subset[i - 1][j]
            else:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - set[i - 1]]

    return subset[n][sum]

# Example usage
assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9) == True
    assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 30) == False
    assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 15) == True
