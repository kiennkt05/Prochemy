# MBPP/170
### Completion
def sum_range_list(numbers, start_index, end_index):
    """
    Calculate the sum of numbers in a list between specified indices.

    Parameters:
    numbers (list): A list of numbers.
    start_index (int): The starting index (inclusive).
    end_index (int): The ending index (inclusive).

    Returns:
    int: The sum of the numbers between start_index and end_index.
    """
    # Validate indices
    if start_index < 0 or end_index >= len(numbers) or start_index > end_index:
        raise ValueError("Invalid indices provided.")
    
    # Calculate the sum of the specified range
    return sum(numbers[start_index:end_index + 1])

# Test case
assert sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10) == 29
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],8,10)==29
    assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],5,7)==16
    assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],7,10)==38
