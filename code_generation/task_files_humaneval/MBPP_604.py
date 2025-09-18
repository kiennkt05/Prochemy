# MBPP/604
### Completion
def reverse_words(s: str) -> str:
    """
    Reverses the words in the given string.

    Parameters:
    s (str): The input string containing words to be reversed.

    Returns:
    str: A string with the words in reverse order.
    """
    # Split the string into words
    words = s.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list back into a string
    return ' '.join(reversed_words)

# Test case
assert reverse_words("python program") == "program python"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert reverse_words("python program")==("program python")
    assert reverse_words("java language")==("language java")
    assert reverse_words("indian man")==("man indian")
