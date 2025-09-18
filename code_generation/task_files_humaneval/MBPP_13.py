# MBPP/13
### Completion
from collections import Counter

def count_common(words):
    """
    Count the most common words in a list and return them as a list of tuples.
    
    Args:
    words (list): A list of words (strings).
    
    Returns:
    list: A list of tuples, each containing a word and its count, sorted by count in descending order.
    """
    # Count the occurrences of each word using Counter
    word_counts = Counter(words)
    
    # Sort the words by count in descending order and convert to a list of tuples
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_word_counts

# Test case
assert count_common(['red','green','black','pink','black','white','black','eyes','white','black',
                     'orange','pink','pink','red','red','white','orange','white',"black",
                     'pink','green','green','pink','green','pink','white','orange',"orange",
                     'red']) == [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]

# If the assertion passes, the function works as expected.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_common(['red','green','black','pink','black','white','black','eyes','white','black','orange','pink','pink','red','red','white','orange','white',"black",'pink','green','green','pink','green','pink','white','orange',"orange",'red']) == [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
    assert count_common(['one', 'two', 'three', 'four', 'five', 'one', 'two', 'one', 'three', 'one']) == [('one', 4), ('two', 2), ('three', 2), ('four', 1)]
    assert count_common(['Facebook', 'Apple', 'Amazon', 'Netflix', 'Google', 'Apple', 'Netflix', 'Amazon']) == [('Apple', 2), ('Amazon', 2), ('Netflix', 2), ('Facebook', 1)]
