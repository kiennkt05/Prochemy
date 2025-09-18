# MBPP/40
### Completion
from collections import Counter
from typing import List, Dict

def freq_element(lst: List[List[int]]) -> Dict[int, int]:
    """
    Function to find the frequency of elements in a list of lists.
    
    Parameters:
    lst (List[List[int]]): A list of lists containing integers.
    
    Returns:
    Dict[int, int]: A dictionary with elements as keys and their frequencies as values.
    """
    # Flatten the list of lists
    flat_list = [item for sublist in lst for item in sublist]
    
    # Count the frequency of each element using Counter
    frequency = Counter(flat_list)
    
    # Return the frequency as a dictionary
    return dict(frequency)

# Test case
assert freq_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]) == {2: 3, 1: 2, 5: 2, 3: 1, 4: 1, 6: 1, 7: 1, 9: 1}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert freq_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]])==({2: 3, 1: 2, 5: 2, 3: 1, 4: 1, 6: 1, 7: 1, 9: 1})
    assert freq_element([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1})
    assert freq_element([[15,20,30,40],[80,90,100,110],[30,30,80,90]])==({30: 3, 80: 2, 90: 2, 15: 1, 20: 1, 40: 1, 100: 1, 110: 1})
