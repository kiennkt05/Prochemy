# MBPP/964
### Completion
def word_len(word):
    """
    Check if the length of the given word is even.

    Parameters:
    word (str): The word to check.

    Returns:
    bool: True if the length of the word is even, False otherwise.
    """
    # Calculate the length of the word
    length = len(word)
    
    # Check if the length is even
    return length % 2 == 0

# Test case
assert word_len("program") == False  # "program" has 7 letters, which is odd
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert word_len("program") == False
    assert word_len("solution") == True
    assert word_len("data") == True
