# MBPP/484
### Completion
def remove_matching_tuple(list1, list2):
    """
    Remove matching tuples from the first list based on the second list.

    Parameters:
    list1 (list of tuples): The first list of tuples.
    list2 (list of tuples): The second list of tuples containing tuples to be removed from the first list.

    Returns:
    list of tuples: A new list containing tuples from the first list that are not in the second list.
    """
    # Use a list comprehension to filter out matching tuples
    return [tup for tup in list1 if tup not in list2]

# Test case
assert remove_matching_tuple([('Hello', 'dude'), ('How', 'are'), ('you', '?')], 
                             [('Hello', 'dude'), ('How', 'are')]) == [('you', '?')]

# Additional test cases for verification
assert remove_matching_tuple([('a', 1), ('b', 2), ('c', 3)], [('b', 2)]) == [('a', 1), ('c', 3)]
assert remove_matching_tuple([('x', 'y'), ('z', 'w')], [('x', 'y'), ('z', 'w')]) == []
assert remove_matching_tuple([], [('Hello', 'dude')]) == []
assert remove_matching_tuple([('Hello', 'dude')], []) == [('Hello', 'dude')]

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_matching_tuple([('Hello', 'dude'), ('How', 'are'), ('you', '?')], [('Hello', 'dude'), ('How', 'are')]) == [('you', '?')]
    assert remove_matching_tuple([('Part', 'of'), ('the', 'journey'), ('is ', 'end')], [('Journey', 'the'), ('is', 'end')]) == [('Part', 'of'), ('the', 'journey'), ('is ', 'end')]
    assert remove_matching_tuple([('Its', 'been'), ('a', 'long'), ('day', 'without')], [('a', 'long'), ('my', 'friend')]) == [('Its', 'been'), ('day', 'without')]
