# MBPP/67
### Completion
def bell_number(n):
    # Create a 2D array to store Bell numbers
    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # Base case
    bell[0][0] = 1
    
    # Fill the Bell triangle
    for i in range(1, n + 1):
        # Explicitly set the first value of the current row
        bell[i][0] = bell[i - 1][i - 1]
        
        # Fill the rest of the current row
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
    
    # The Bell number for n is found at bell[n][0]
    return bell[n][0]

# Test the function with the provided assertion
assert bell_number(2) == 2

# You can also print the Bell number for other values
print(bell_number(3))  # Output: 5
print(bell_number(4))  # Output: 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300
