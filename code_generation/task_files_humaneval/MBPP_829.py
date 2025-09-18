# MBPP/829
### Completion
from collections import Counter

def second_frequent(strings):
    # Count the frequency of each string in the list
    frequency = Counter(strings)
    
    # Sort the items based on frequency in descending order
    sorted_items = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    
    # Check if there are at least two different strings
    if len(sorted_items) < 2:
        return None  # or raise an exception based on requirements
    
    # Return the second most frequent string
    return sorted_items[1][0]

# Test case
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
