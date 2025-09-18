# MBPP/456
### Completion
def reverse_string_list(string_list):
    """
    Reverses each string in the given list of strings.

    Parameters:
    string_list (list of str): A list containing strings to be reversed.

    Returns:
    list of str: A new list with each string reversed.
    """
    # Using list comprehension to reverse each string in the input list
    return [s[::-1] for s in string_list]

# Test the function with the provided test case
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

# If the assertion passes, the function works as expected.
print("Function works correctly!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
    assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']
