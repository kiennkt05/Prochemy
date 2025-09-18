# MBPP/946
### Completion
from collections import Counter

def most_common_elem(text, n):
    # Count the frequency of each character in the text
    counter = Counter(text)
    # Get the n most common elements
    most_common = counter.most_common(n)
    return most_common

# Test the function with the provided assertion
assert most_common_elem('lkseropewdssafsdfafkpwe', 3) == [('s', 4), ('e', 3), ('f', 3)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert most_common_elem('lkseropewdssafsdfafkpwe',3)==[('s', 4), ('e', 3), ('f', 3)] 
    assert most_common_elem('lkseropewdssafsdfafkpwe',2)==[('s', 4), ('e', 3)]
    assert most_common_elem('lkseropewdssafsdfafkpwe',7)==[('s', 4), ('e', 3), ('f', 3), ('k', 2), ('p', 2), ('w', 2), ('d', 2)]
