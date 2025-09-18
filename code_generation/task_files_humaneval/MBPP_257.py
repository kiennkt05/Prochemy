# MBPP/257
### Completion
def swap_numbers(a, b):
    """
    Swaps two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    tuple: A tuple containing the second number followed by the first number.
    """
    return (b, a)

# Test case
assert swap_numbers(10, 20) == (20, 10)

# You can add more test cases if needed
assert swap_numbers(1, 2) == (2, 1)
assert swap_numbers(-5, 5) == (5, -5)
assert swap_numbers(0, 0) == (0, 0)

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert swap_numbers(10,20)==(20,10)
    assert swap_numbers(15,17)==(17,15)
    assert swap_numbers(100,200)==(200,100)
