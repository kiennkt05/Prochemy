# MBPP/88
### Completion
from collections import Counter

def freq_count(lst):
    """
    Count the frequency of elements in a list.

    Parameters:
    lst (list): A list of elements to count.

    Returns:
    dict: A dictionary with elements as keys and their frequencies as values.
    """
    # Use Counter to count the frequency of each element in the list
    frequency = Counter(lst)
    # Convert Counter to a dictionary and return
    return dict(frequency)

# Test case
assert freq_count([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]) == {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1}) 
    assert freq_count([1,2,3,4,3,2,4,1,3,1,4])==({1:3, 2:2,3:3,4:3}) 
    assert freq_count([5,6,7,4,9,10,4,5,6,7,9,5])==({10:1,5:3,6:2,7:2,4:2,9:2}) 
