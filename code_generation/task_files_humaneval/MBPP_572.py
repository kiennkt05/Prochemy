# MBPP/572
### Completion
def two_unique_nums(lst):
    """
    Remove two duplicate numbers from the given list.
    
    Parameters:
    lst (list): A list of integers where duplicates may exist.
    
    Returns:
    list: A new list with two duplicates removed.
    """
    from collections import Counter
    
    # Count occurrences of each number in the list
    count = Counter(lst)
    
    # Create a new list to store the result
    result = []
    
    # Track how many duplicates we've removed
    duplicates_removed = 0
    
    for num in lst:
        # If the number is a duplicate and we haven't removed two yet
        if count[num] > 1 and duplicates_removed < 2:
            # Decrease the count and increment the duplicates removed
            count[num] -= 1
            duplicates_removed += 1
        else:
            # If it's not a duplicate or we've removed enough, add to result
            result.append(num)
    
    return result

# Test case
assert two_unique_nums([1, 2, 3, 2, 3, 4, 5]) == [1, 4, 5]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
    assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]
