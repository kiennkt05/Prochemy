# MBPP/197
### Completion
def find_exponentio(tuple1, tuple2):
    """
    This function takes two tuples of numbers and returns a tuple where each element
    is the result of raising the corresponding element in the first tuple to the power
    of the corresponding element in the second tuple.

    :param tuple1: A tuple of base numbers.
    :param tuple2: A tuple of exponent numbers.
    :return: A tuple containing the results of the exponentiation.
    """
    # Using a generator expression to compute the power for each pair of elements
    result = tuple(base ** exponent for base, exponent in zip(tuple1, tuple2))
    return result

# Test case
assert find_exponentio((10, 4, 5, 6), (5, 6, 7, 5)) == (100000, 4096, 78125, 7776)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_exponentio((10, 4, 5, 6), (5, 6, 7, 5)) == (100000, 4096, 78125, 7776)
    assert find_exponentio((11, 5, 6, 7), (6, 7, 8, 6)) == (1771561, 78125, 1679616, 117649)
    assert find_exponentio((12, 6, 7, 8), (7, 8, 9, 7)) == (35831808, 1679616, 40353607, 2097152)
