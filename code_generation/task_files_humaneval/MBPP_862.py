# MBPP/862
### Completion
from collections import Counter

def n_common_words(text, n):
    """
    Find the occurrences of n most common words in a given text.

    Parameters:
    text (str): The input text from which to find common words.
    n (int): The number of most common words to return.

    Returns:
    list: A list of tuples containing the n most common words and their counts.
    """
    # Normalize the text to lowercase and split into words
    words = text.lower().split()
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Get the n most common words
    most_common = word_counts.most_common(n)
    
    return most_common

# Test case
assert n_common_words("python is a programming language", 1) == [('python', 1)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert n_common_words("python is a programming language",1)==[('python', 1)]
    assert n_common_words("python is a programming language",1)==[('python', 1)]
    assert n_common_words("python is a programming language",5)==[('python', 1),('is', 1), ('a', 1), ('programming', 1), ('language', 1)]
