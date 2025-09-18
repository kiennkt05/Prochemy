# MBPP/79
### Completion
def word_len(word):
    """
    Check whether the length of the word is odd or not.

    Parameters:
    word (str): The word to check.

    Returns:
    bool: True if the length of the word is odd, False otherwise.
    """
    # Calculate the length of the word
    length = len(word)
    
    # Check if the length is odd
    return length % 2 == 1

# Test case
assert word_len("Hadoop") == False  # "Hadoop" has 6 letters, which is even
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert word_len("Hadoop") == False
    assert word_len("great") == True
    assert word_len("structure") == True
