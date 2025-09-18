# MBPP/874
### Completion
def check_Concat(main_str, sub_str):
    """
    Check if the main_str is a concatenation of the sub_str.

    Parameters:
    main_str (str): The string to check.
    sub_str (str): The substring to check against.

    Returns:
    bool: True if main_str is a concatenation of sub_str, False otherwise.
    """
    # Check if the length of main_str is a multiple of the length of sub_str
    if len(main_str) % len(sub_str) != 0:
        return False
    
    # Calculate how many times the sub_str should be repeated
    repeat_count = len(main_str) // len(sub_str)
    
    # Create the concatenated string
    concatenated_str = sub_str * repeat_count
    
    # Check if the concatenated string matches the main string
    return concatenated_str == main_str

# Test case
assert check_Concat("abcabcabc", "abc") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Concat("abcabcabc","abc") == True
    assert check_Concat("abcab","abc") == False
    assert check_Concat("aba","ab") == False
