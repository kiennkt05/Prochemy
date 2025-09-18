# MBPP/621
### Completion
def increment_numerics(strings, k):
    """
    Increment numeric values in the given list of strings by k.

    Parameters:
    strings (list of str): The list of strings to process.
    k (int): The value to increment numeric strings by.

    Returns:
    list of str: A new list with numeric strings incremented by k.
    """
    incremented_strings = []
    
    for s in strings:
        if s.isdigit():  # Check if the string is numeric
            incremented_value = str(int(s) + k)  # Increment and convert back to string
            incremented_strings.append(incremented_value)
        else:
            incremented_strings.append(s)  # Keep the non-numeric string unchanged
    
    return incremented_strings

# Test case
assert increment_numerics(["MSM", "234", "is", "98", "123", "best", "4"], 6) == ['MSM', '240', 'is', '104', '129', 'best', '10']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert increment_numerics(["MSM", "234", "is", "98", "123", "best", "4"] , 6) == ['MSM', '240', 'is', '104', '129', 'best', '10']
    assert increment_numerics(["Dart", "356", "is", "88", "169", "Super", "6"] , 12) == ['Dart', '368', 'is', '100', '181', 'Super', '18']
    assert increment_numerics(["Flutter", "451", "is", "44", "96", "Magnificent", "12"] , 33) == ['Flutter', '484', 'is', '77', '129', 'Magnificent', '45']
