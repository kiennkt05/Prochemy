# MBPP/15
### Completion
def split_lowerstring(s: str) -> list:
    """
    Splits the input string at each lowercase letter.

    Parameters:
    s (str): The input string to be split.

    Returns:
    list: A list of substrings split at lowercase letters.
    """
    result = []
    current_substring = []

    for char in s:
        if char.islower():
            # If we encounter a lowercase letter, we join the current substring
            # and add it to the result if it's not empty
            if current_substring:
                result.append(''.join(current_substring))
                current_substring = []
        current_substring.append(char)

    # Add the last substring if it exists
    if current_substring:
        result.append(''.join(current_substring))

    return result

# Test case
assert split_lowerstring("AbCd") == ['bC', 'd']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split_lowerstring("AbCd")==['bC','d']
    assert split_lowerstring("Python")==['y', 't', 'h', 'o', 'n']
    assert split_lowerstring("Programming")==['r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
