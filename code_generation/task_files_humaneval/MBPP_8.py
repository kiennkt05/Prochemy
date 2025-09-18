# MBPP/8
### Completion
def square_nums(nums):
    """
    This function takes a list of numbers and returns a list of their squares.
    
    :param nums: List of integers
    :return: List of integers representing the squares of the input numbers
    """
    return list(map(lambda x: x ** 2, nums))

# Test case
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert square_nums([10,20,30])==([100,400,900])
    assert square_nums([12,15])==([144,225])
