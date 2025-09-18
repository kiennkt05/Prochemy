# MBPP/947
### Completion
def len_log(words):
    """
    This function takes a list of words and returns the length of the shortest word.
    
    :param words: List of strings (words)
    :return: Length of the shortest word
    """
    if not words:  # Check if the list is empty
        return 0  # Return 0 if there are no words
    
    # Use the min function with key=len to find the shortest word
    shortest_word = min(words, key=len)
    
    # Return the length of the shortest word
    return len(shortest_word)

# Test case
assert len_log(["win", "lose", "great"]) == 3  # The shortest word is "win" with length 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert len_log(["win","lose","great"]) == 3
    assert len_log(["a","ab","abc"]) == 1
    assert len_log(["12","12","1234"]) == 2
