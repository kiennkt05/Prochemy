# MBPP/67
### Completion
def factorial(n):
    """Compute the factorial of n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def binomial_coefficient(n, k):
    """Compute the binomial coefficient C(n, k)."""
    if k > n or k < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def bell_number(n):
    """Compute the n-th Bell number."""
    # Create a list to store Bell numbers
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
    
    # The n-th Bell number is in bell[n][0]
    return bell[n][0]

# Test the function with the provided assertion
assert bell_number(2) == 2

# Additional test cases
print(bell_number(0))  # Should return 1
print(bell_number(1))  # Should return 1
print(bell_number(3))  # Should return 5
print(bell_number(4))  # Should return 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300
