# MBPP/773
### Completion
def occurance_substring(main_string, substring):
    """
    Find the occurrence and position of the substring within the main string.

    Parameters:
    main_string (str): The string to search within.
    substring (str): The substring to find.

    Returns:
    tuple: A tuple containing the substring and its starting and ending indices.
           Returns None if the substring is not found.
    """
    # Find the starting index of the substring
    start_index = main_string.find(substring)
    
    # If the substring is not found, return None
    if start_index == -1:
        return None
    
    # Calculate the ending index
    end_index = start_index + len(substring)
    
    # Return the result as a tuple
    return (substring, start_index, end_index)

# Test case
assert occurance_substring('python programming, python language', 'python') == ('python', 0, 6)

# Additional test cases
assert occurance_substring('hello world', 'world') == ('world', 6, 11)
assert occurance_substring('test test test', 'test') == ('test', 0, 4)
assert occurance_substring('no match here', 'match') == ('match', 3, 8)
assert occurance_substring('substring not found', 'notfound') == None

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
