# MBPP/18
### Completion
def remove_dirty_chars(s1, s2):
    """
    Remove characters from the first string (s1) that are present in the second string (s2).
    
    Parameters:
    s1 (str): The original string from which characters will be removed.
    s2 (str): The string containing characters to be removed from s1.
    
    Returns:
    str: A new string with the characters from s2 removed from s1.
    """
    # Create a set of characters to remove for efficient lookup
    chars_to_remove = set(s2)
    
    # Use a list comprehension to filter out unwanted characters
    filtered_chars = [char for char in s1 if char not in chars_to_remove]
    
    # Join the filtered characters back into a string
    return ''.join(filtered_chars)

# Test case
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles' 
