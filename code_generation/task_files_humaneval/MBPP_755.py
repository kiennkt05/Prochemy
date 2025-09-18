# MBPP/755
### Completion
def second_smallest(numbers):
    # Remove duplicates by converting the list to a set
    unique_numbers = set(numbers)
    
    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two unique numbers.")
    
    # Convert the set back to a sorted list
    sorted_unique_numbers = sorted(unique_numbers)
    
    # Return the second smallest number
    return sorted_unique_numbers[1]

# Test case
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
