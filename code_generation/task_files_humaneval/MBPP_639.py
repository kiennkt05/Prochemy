# MBPP/639
### Completion
def sample_nam(names):
    """
    This function takes a list of names and returns the sum of the lengths of the names
    that do not start with a lowercase letter.
    
    Parameters:
    names (list): A list of names (strings).
    
    Returns:
    int: The sum of the lengths of the filtered names.
    """
    # Filter names that start with an uppercase letter
    filtered_names = [name for name in names if name and name[0].isupper()]
    
    # Calculate the sum of lengths of the filtered names
    total_length = sum(len(name) for name in filtered_names)
    
    return total_length

# Test the function with the provided sample case
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16

# Additional test cases
assert sample_nam(['Alice', 'bob', 'Charlie', 'dave']) == 15  # Alice (5) + Charlie (7) = 12
assert sample_nam(['Eve', 'frank', 'Grace']) == 8  # Eve (3) + Grace (5) = 8
assert sample_nam(['Zoe', 'xander', 'Yara']) == 6  # Zoe (3) + Yara (3) = 6
assert sample_nam([]) == 0  # No names, should return 0

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10
    assert sample_nam(["abcd", "Python", "abba", "aba"])==6
