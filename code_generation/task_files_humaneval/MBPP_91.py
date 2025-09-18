# MBPP/91
### Completion
def find_substring(string_list, substring):
    """
    Check if a substring is present in any of the strings in the given list.

    Parameters:
    string_list (list of str): A list of strings to search through.
    substring (str): The substring to search for.

    Returns:
    bool: True if the substring is found in any string, False otherwise.
    """
    for string in string_list:
        if substring in string:
            return True
    return False

# Test case
assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
    assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
    assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True
