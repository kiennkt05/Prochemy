# MBPP/755
### Completion
def second_smallest(numbers):
    # Remove duplicates by converting the list to a set
    unique_numbers = list(set(numbers))
    
    # Sort the unique numbers
    unique_numbers.sort()
    
    # Return the second smallest number if it exists
    if len(unique_numbers) >= 2:
        return unique_numbers[1]
    else:
        raise ValueError("List must contain at least two unique numbers.")

# Test the function with the provided assertion
assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
