# MBPP/103
### Completion
def eulerian_num(n, m):
    # Create a table to store the Eulerian numbers
    A = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base cases
    A[0][0] = 1  # A(0, 0) = 1
    
    for i in range(1, n + 1):
        A[i][0] = 1  # A(n, 0) = 1
        A[i][i] = 1  # A(n, n) = 1
        for j in range(1, i):
            A[i][j] = (j + 1) * A[i - 1][j] + (i - j) * A[i - 1][j - 1]
    
    return A[n][m]

# Test the function with the provided assertion
assert eulerian_num(3, 1) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26
