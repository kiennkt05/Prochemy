# MBPP/130
### Completion
from collections import Counter

def max_occurrences(lst):
    """
    Find the item with maximum frequency in the given list.

    Parameters:
    lst (list): A list of items.

    Returns:
    tuple: A tuple containing the item with maximum frequency and its count.
    """
    # Count the occurrences of each item in the list
    frequency = Counter(lst)
    
    # Find the item with the maximum frequency
    max_item, max_count = max(frequency.items(), key=lambda x: x[1])
    
    return (max_item, max_count)

# Test case
assert max_occurrences([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]) == (2, 5)

# Additional test cases can be added to further validate the function
print(max_occurrences([1, 2, 2, 3, 3, 3]))  # Expected output: (3, 3)
print(max_occurrences([4, 4, 4, 1, 1, 2, 2, 2, 2]))  # Expected output: (2, 4)
print(max_occurrences([]))  # Expected output: (None, 0) or handle empty list case as needed
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==(2, 5)
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,16,18])==(8, 2)
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==(20, 3)
