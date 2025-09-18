# MBPP/897
### Completion
def is_Word_Present(sentence: str, word: str) -> bool:
    """
    Check if a specific word is present in a given sentence.

    Parameters:
    sentence (str): The sentence in which to search for the word.
    word (str): The word to search for in the sentence.

    Returns:
    bool: True if the word is present in the sentence, False otherwise.
    """
    # Check if the word is present in the sentence
    return word in sentence

# Test case
assert is_Word_Present("machine learning", "machine") == True

# Additional test cases for verification
assert is_Word_Present("machine learning", "learning") == True
assert is_Word_Present("machine learning", "AI") == False
assert is_Word_Present("Hello world", "world") == True
assert is_Word_Present("Hello world", "hello") == False  # Case-sensitive check
assert is_Word_Present("", "word") == False  # Empty sentence
assert is_Word_Present("word", "") == True  # Empty word should be considered present

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Word_Present("machine learning","machine") == True
    assert is_Word_Present("easy","fun") == False
    assert is_Word_Present("python language","code") == False
