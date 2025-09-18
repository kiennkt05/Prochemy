# MBPP/674
### Completion
from collections import OrderedDict

def remove_duplicate(input_string):
    # Split the string into words
    words = input_string.split()
    # Use OrderedDict to remove duplicates while preserving order
    unique_words = list(OrderedDict.fromkeys(words))
    # Join the unique words back into a string
    return ' '.join(unique_words)

# Test the function with the provided assertion
assert remove_duplicate("Python Exercises Practice Solution Exercises") == "Python Exercises Practice Solution"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_duplicate("Python Exercises Practice Solution Exercises")==("Python Exercises Practice Solution")
    assert remove_duplicate("Python Exercises Practice Solution Python")==("Python Exercises Practice Solution")
    assert remove_duplicate("Python Exercises Practice Solution Practice")==("Python Exercises Practice Solution")
