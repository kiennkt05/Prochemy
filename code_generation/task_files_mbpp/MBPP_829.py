# MBPP/829
### Completion
from collections import Counter

def second_frequent(strings):
    # Count the frequency of each string in the list
    frequency = Counter(strings)
    
    # Get the two most common strings
    most_common = frequency.most_common(2)
    
    # Check if there are at least two different strings
    if len(most_common) < 2:
        return None  # or raise an exception if preferred
    
    # Return the second most common string
    return most_common[1][0]

# Test the function with the provided assertion
assert second_frequent(['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']) == 'bbb'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert second_frequent(['aaa','bbb','ccc','bbb','aaa','aaa']) == 'bbb'
    assert second_frequent(['abc','bcd','abc','bcd','bcd','bcd']) == 'abc'
    assert second_frequent(['cdma','gsm','hspa','gsm','cdma','cdma']) == 'gsm'
