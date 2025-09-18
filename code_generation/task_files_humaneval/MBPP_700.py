# MBPP/700
### Completion
def count_range_in_list(numbers, lower, upper):
    """
    Count the number of elements in the list 'numbers' that are within the range [lower, upper).

    Parameters:
    numbers (list): A list of integers.
    lower (int): The lower bound of the range (inclusive).
    upper (int): The upper bound of the range (exclusive).

    Returns:
    int: The count of elements within the specified range.
    """
    count = 0
    for number in numbers:
        if lower <= number < upper:
            count += 1
    return count

# Test case
assert count_range_in_list([10, 20, 30, 40, 40, 40, 70, 80, 99], 40, 100) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_range_in_list([10,20,30,40,40,40,70,80,99],40,100)==6
    assert count_range_in_list(['a','b','c','d','e','f'],'a','e')==5
    assert count_range_in_list([7,8,9,15,17,19,45],15,20)==3
