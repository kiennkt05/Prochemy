# MBPP/90
### Completion
def len_log(words):
    """
    Function to find the length of the longest word in a list of words.
    
    Parameters:
    words (list of str): A list containing words as strings.
    
    Returns:
    int: The length of the longest word.
    """
    if not words:  # Check if the list is empty
        return 0
    
    # Use max with key=len to find the longest word and return its length
    longest_word_length = len(max(words, key=len))
    return longest_word_length

# Test case
assert len_log(["python", "PHP", "bigdata"]) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert len_log(["python","PHP","bigdata"]) == 7
    assert len_log(["a","ab","abc"]) == 3
    assert len_log(["small","big","tall"]) == 5
