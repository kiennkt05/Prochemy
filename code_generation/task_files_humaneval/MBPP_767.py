# MBPP/767
### Completion
from itertools import combinations

def get_Pairs_Count(arr, target_sum, pair_size):
    """
    Count the number of pairs in the array whose sum equals the target_sum.
    
    Parameters:
    arr (list): List of integers.
    target_sum (int): The target sum for the pairs.
    pair_size (int): The number of elements in each pair.
    
    Returns:
    int: The count of pairs whose sum equals target_sum.
    """
    count = 0
    
    # Generate all combinations of the specified size
    for pair in combinations(arr, pair_size):
        if sum(pair) == target_sum:
            count += 1
            
    return count

# Test case
assert get_Pairs_Count([1, 1, 1, 1], 4, 2) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Pairs_Count([1,1,1,1],4,2) == 6
    assert get_Pairs_Count([1,5,7,-1,5],5,6) == 3
    assert get_Pairs_Count([1,-2,3],3,1) == 1
