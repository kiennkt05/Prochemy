# MBPP/844
### Completion
def get_Number(k, n):
    # Generate the first n odd numbers
    odds = [i for i in range(1, 2*n, 2)]
    # Generate the first n even numbers
    evens = [i for i in range(0, 2*n, 2)]
    # Combine odds and evens
    combined = odds + evens
    # Return the k-th element (1-based index)
    return combined[k - 1]

# Test the function with the provided assertion
assert get_Number(8, 5) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Number(8,5) == 2
    assert get_Number(7,2) == 3
    assert get_Number(5,2) == 3
