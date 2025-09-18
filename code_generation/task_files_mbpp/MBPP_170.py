# MBPP/170
### Completion
def sum_range_list(numbers, start_index, end_index):
    # Ensure the indices are within the bounds of the list
    if start_index < 0 or end_index >= len(numbers) or start_index > end_index:
        raise IndexError("Indices are out of bounds or invalid.")
    
    # Calculate the sum of the specified range
    return sum(numbers[start_index:end_index + 1])

# Test the function with the provided assertion
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
