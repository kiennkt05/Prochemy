# MBPP/568
### Completion
def empty_list(n):
    """
    Create a list of empty dictionaries.

    Parameters:
    n (int): The number of empty dictionaries to create.

    Returns:
    list: A list containing n empty dictionaries.
    """
    return [{} for _ in range(n)]

# Test case
assert empty_list(5) == [{}, {}, {}, {}, {}]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert empty_list(5)==[{},{},{},{},{}]
    assert empty_list(6)==[{},{},{},{},{},{}]
    assert empty_list(7)==[{},{},{},{},{},{},{}]
