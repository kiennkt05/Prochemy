# MBPP/447
### Completion
def cube_nums(numbers):
    """
    This function takes a list of numbers and returns a list of their cubes.
    
    :param numbers: List of integers
    :return: List of cubes of the input integers
    """
    # Using map with a lambda function to calculate the cube of each number
    return list(map(lambda x: x ** 3, numbers))

# Test case
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    assert cube_nums([10,20,30])==([1000, 8000, 27000])
    assert cube_nums([12,15])==([1728, 3375])
