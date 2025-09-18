# MBPP/270
### Completion
def sum_even_and_even_index(numbers, n):
    # Initialize the sum
    total_sum = 0
    
    # Iterate through the list using index
    for index in range(n):
        # Check if the index is even and the number at that index is even
        if index % 2 == 0 and numbers[index] % 2 == 0:
            total_sum += numbers[index]
    
    return total_sum

# Test the function with the provided assertion
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8], 6) == 30
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8],6) == 30
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18],10) == 26
    assert sum_even_and_even_index([5, 6, 12, 1],4) == 12
