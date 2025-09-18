# MBPP/649
### Completion
def sum_Range_list(numbers, start_index, end_index):
    """
    Calculate the sum of numbers in a list between specified indices.

    Parameters:
    numbers (list): A list of numbers.
    start_index (int): The starting index (inclusive).
    end_index (int): The ending index (inclusive).

    Returns:
    int: The sum of the numbers between the specified indices.
    """
    # Validate indices
    if start_index < 0 or end_index >= len(numbers) or start_index > end_index:
        raise IndexError("Indices are out of bounds or invalid.")

    # Calculate the sum from start_index to end_index (inclusive)
    total_sum = sum(numbers[start_index:end_index + 1])
    return total_sum

# Test case
assert sum_Range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10) == 29
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12],8,10) == 29
    assert sum_Range_list([1,2,3,4,5],1,2) == 5
    assert sum_Range_list([1,0,1,2,5,6],4,5) == 11
