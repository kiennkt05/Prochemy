# MBPP/883
### Completion
def div_of_nums(numbers, m, n):
    """
    Find numbers in the list that are divisible by both m and n.

    Parameters:
    numbers (list): A list of integers to check.
    m (int): The first divisor.
    n (int): The second divisor.

    Returns:
    list: A list of integers from the input list that are divisible by both m and n.
    """
    # Use filter with a lambda function to find numbers divisible by both m and n
    result = list(filter(lambda x: x % m == 0 and x % n == 0, numbers))
    return result

# Test case
assert div_of_nums([19, 65, 57, 39, 152, 639, 121, 44, 90, 190], 2, 4) == [152, 44]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert div_of_nums([19, 65, 57, 39, 152, 639, 121, 44, 90, 190],2,4)==[ 152,44]
    assert div_of_nums([1, 2, 3, 5, 7, 8, 10],2,5)==[10]
    assert div_of_nums([10,15,14,13,18,12,20],10,5)==[10,20]
