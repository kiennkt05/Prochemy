# MBPP/833
### Completion
def get_key(d):
    """
    This function takes a dictionary as input and returns a list of its keys.

    Parameters:
    d (dict): The input dictionary from which to extract keys.

    Returns:
    list: A list containing the keys of the dictionary.
    """
    return list(d.keys())

# Test case
assert get_key({1: 'python', 2: 'java'}) == [1, 2]

# Additional test cases for verification
assert get_key({'a': 1, 'b': 2}) == ['a', 'b']
assert get_key({}) == []
assert get_key({True: 'yes', False: 'no'}) == [True, False]

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_key({1:'python',2:'java'})==[1,2]
    assert get_key({10:'red',20:'blue',30:'black'})==[10,20,30]
    assert get_key({27:'language',39:'java',44:'little'})==[27,39,44]
