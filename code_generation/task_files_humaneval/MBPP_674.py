# MBPP/674
### Completion
from collections import OrderedDict

def remove_duplicate(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Use OrderedDict to remove duplicates while maintaining order
    unique_words = OrderedDict.fromkeys(words)
    
    # Join the unique words back into a single string
    result = ' '.join(unique_words)
    
    return result

# Test case
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
