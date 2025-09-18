# MBPP/537
### Completion
def first_repeated_word(s: str) -> str:
    """
    Function to find the first repeated word in a given string.
    
    Parameters:
    s (str): The input string containing words.
    
    Returns:
    str: The first repeated word, or None if no word is repeated.
    """
    # Split the string into words
    words = s.split()
    seen = set()  # Set to keep track of seen words
    
    # Iterate through the words
    for word in words:
        # Check if the word has already been seen
        if word in seen:
            return word  # Return the first repeated word
        seen.add(word)  # Add the word to the set if not seen
    
    return None  # Return None if no repeated word is found

# Test case
assert first_repeated_word("ab ca bc ab") == "ab"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_repeated_word("ab ca bc ab") == "ab"
    assert first_repeated_word("ab ca bc") == 'None'
    assert first_repeated_word("ab ca bc ca ab bc") == "ca"
