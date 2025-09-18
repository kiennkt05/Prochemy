# MBPP/817
### Completion
def div_of_nums(numbers, m, n):
    """
    This function returns a list of numbers from the input list that are divisible by either m or n.
    
    :param numbers: List of integers to be checked.
    :param m: First divisor.
    :param n: Second divisor.
    :return: List of integers that are divisible by m or n.
    """
    # Use filter with a lambda function to find numbers divisible by m or n
    return list(filter(lambda x: x % m == 0 or x % n == 0, numbers))

# Test case
assert div_of_nums([19, 65, 57, 39, 152, 639, 121, 44, 90, 190], 19, 13) == [19, 65, 57, 39, 152, 190]

# If you want to see the output for the test case, you can uncomment the following line:
# print(div_of_nums([19, 65, 57, 39, 152, 639, 121, 44, 90, 190], 19, 13))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert div_of_nums([19, 65, 57, 39, 152, 639, 121, 44, 90, 190],19,13)==[19, 65, 57, 39, 152, 190]
    assert div_of_nums([1, 2, 3, 5, 7, 8, 10],2,5)==[2, 5, 8, 10]
    assert div_of_nums([10,15,14,13,18,12,20],10,5)==[10, 15, 20]
