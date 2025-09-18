# MBPP/862
### Completion
from collections import Counter
import re

def n_common_words(text, n):
    # Normalize the text to lowercase and use regex to find words
    words = re.findall(r'\b\w+\b', text.lower())
    # Count the occurrences of each word
    word_counts = Counter(words)
    # Get the n most common words
    return word_counts.most_common(n)

# Example usage
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
