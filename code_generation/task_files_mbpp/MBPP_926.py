# MBPP/926
### Completion
def rencontres_number(n, k):
    # Create a 2D list to store the rencontres numbers
    R = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case
    R[0][0] = 1  # R(0, 0) = 1
    
    # Fill the table using the recursive formula
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            R[i][j] = j * R[i - 1][j - 1] + (i - j) * R[i - 1][j]
    
    return R[n][k]

# Test the function with the provided assertion
assert rencontres_number(7, 2) == 924
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rencontres_number(7, 2) == 924
    assert rencontres_number(3, 0) == 2
    assert rencontres_number(3, 1) == 3
