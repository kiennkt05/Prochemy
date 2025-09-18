# MBPP/142
### Completion
def count_samepair(list1, list2, list3):
    """
    Count the number of same pairs in three given lists.
    
    A pair is considered the same if the elements at the same index in all three lists are equal.
    
    Parameters:
    list1 (list): The first list of elements.
    list2 (list): The second list of elements.
    list3 (list): The third list of elements.
    
    Returns:
    int: The count of same pairs across the three lists.
    """
    # Initialize a counter for the same pairs
    same_pair_count = 0
    
    # Iterate through the lists using the index
    for i in range(min(len(list1), len(list2), len(list3))):
        # Check if the elements at the same index are equal
        if list1[i] == list2[i] == list3[i]:
            same_pair_count += 1
            
    return same_pair_count

# Test case
assert count_samepair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
    assert count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5
