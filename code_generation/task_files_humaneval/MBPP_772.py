# MBPP/772
### Completion
def remove_length(input_string, k):
    """
    Remove all words of length k from the input string.

    Parameters:
    input_string (str): The string from which to remove words.
    k (int): The length of words to remove.

    Returns:
    str: The modified string with words of length k removed.
    """
    # Split the input string into words
    words = input_string.split()
    
    # Filter out words of length k
    filtered_words = [word for word in words if len(word) != k]
    
    # Join the remaining words back into a string
    result = ' '.join(filtered_words)
    
    return result

# Test case
assert remove_length('The person is most value tet', 3) == 'person is most value'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_length('The person is most value tet', 3) == 'person is most value'
    assert remove_length('If you told me about this ok', 4) == 'If you me about ok'
    assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'
