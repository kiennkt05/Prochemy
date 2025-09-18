# MBPP/21
### Completion
def multiples_of_num(n, m):
    """
    Generate a list of the first m multiples of n.

    Parameters:
    n (int): The number to find multiples of.
    m (int): The number of multiples to generate.

    Returns:
    list: A list containing the first m multiples of n.
    """
    # Using list comprehension to generate the multiples
    return [n * i for i in range(1, m + 1)]

# Test case
assert multiples_of_num(4, 3) == [4, 8, 12], "Test case failed!"
assert multiples_of_num(3, 4) == [3, 6, 9, 12], "Test case failed!"
assert multiples_of_num(5, 5) == [5, 10, 15, 20, 25], "Test case failed!"
assert multiples_of_num(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Test case failed!"

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiples_of_num(4,3)== [3,6,9,12]
    assert multiples_of_num(2,5)== [5,10]
    assert multiples_of_num(9,2)== [2,4,6,8,10,12,14,16,18]
