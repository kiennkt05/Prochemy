# MBPP/564
### Completion
def count_Pairs(array, n):
    """
    Count the number of unequal element pairs in the given array.
    
    Parameters:
    array (list): The input array of integers.
    n (int): The length of the array.
    
    Returns:
    int: The count of unequal element pairs (i, j) where i < j and array[i] != array[j].
    """
    count = 0
    # Iterate through each pair of indices (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] != array[j]:
                count += 1
    return count

# Test case
assert count_Pairs([1, 2, 1], 3) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10
