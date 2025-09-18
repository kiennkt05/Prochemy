# MBPP/679
### Completion
def access_key(dictionary, index):
    """
    Access a dictionary key's element by index.

    Parameters:
    dictionary (dict): The dictionary from which to access the key.
    index (int): The index of the key to access.

    Returns:
    str: The key at the specified index.
    """
    # Convert the dictionary keys to a list
    keys = list(dictionary.keys())
    
    # Return the key at the specified index
    return keys[index]

# Test case
assert access_key({'physics': 80, 'math': 90, 'chemistry': 86}, 0) == 'physics'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert access_key({'physics': 80, 'math': 90, 'chemistry': 86},0)== 'physics'
    assert access_key({'python':10, 'java': 20, 'C++':30},2)== 'C++'
    assert access_key({'program':15,'computer':45},1)== 'computer'
