# MBPP/254
### Completion
def words_ae(input_string):
    """
    Find all words in the input string that start with 'a' or 'e'.
    
    Parameters:
    input_string (str): The string to search for words.
    
    Returns:
    list: A list of words starting with 'a' or 'e'.
    """
    # Split the input string into words
    words = input_string.split()
    
    # Initialize a list to hold words that start with 'a' or 'e'
    result = []
    
    # Check each word
    for word in words:
        # Check if the word starts with 'a' or 'e' (case insensitive)
        if word.lower().startswith(('a', 'e')):
            result.append(word)
    
    return result

# Test case
assert words_ae("python programe") == ['ame']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert words_ae("python programe")==['ame']
    assert words_ae("python programe language")==['ame','anguage']
    assert words_ae("assert statement")==['assert', 'atement']
