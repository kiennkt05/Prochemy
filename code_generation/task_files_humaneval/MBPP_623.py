# MBPP/623
### Completion
def nth_nums(numbers, n):
    """
    Calculate the n-th power of each element in the given list of numbers.

    Parameters:
    numbers (list): A list of integers.
    n (int): The power to which each element should be raised.

    Returns:
    list: A list containing the n-th power of each element in the input list.
    """
    return list(map(lambda x: x ** n, numbers))

# Test case
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert nth_nums([10,20,30],3)==([1000, 8000, 27000])
    assert nth_nums([12,15],5)==([248832, 759375])
