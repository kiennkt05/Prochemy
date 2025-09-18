# MBPP/739
### Completion
def find_Index(n):
    # Calculate the minimum value for a number to have n digits
    min_value = 10 ** (n - 1)
    
    k = 1
    while True:
        # Calculate the k-th triangular number
        triangular_number = k * (k + 1) // 2
        
        # Check if it has at least n digits
        if triangular_number >= min_value:
            return k
        
        k += 1

# Test the function with the provided assertion
assert find_Index(2) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45
