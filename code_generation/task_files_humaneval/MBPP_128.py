# MBPP/128
### Completion
def long_words(n, sentence):
    """
    Shortlist words longer than n from the given sentence.

    Parameters:
    n (int): The length threshold for filtering words.
    sentence (str): The input sentence containing words.

    Returns:
    list: A list of words longer than n.
    """
    # Split the sentence into words
    words = sentence.split()
    
    # Filter words that are longer than n
    long_words_list = [word for word in words if len(word) > n]
    
    return long_words_list

# Test the function with the provided assertion
assert long_words(3, "python is a programming language") == ['python', 'programming', 'language']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert long_words(3,"python is a programming language")==['python','programming','language']
    assert long_words(2,"writing a program")==['writing','program']
    assert long_words(5,"sorting list")==['sorting']
