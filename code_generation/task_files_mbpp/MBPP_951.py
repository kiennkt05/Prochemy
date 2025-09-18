# MBPP/951
### Completion
def max_similar_indices(list1, list2):
    # Ensure both lists are of the same length
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    # Create a new list to store the maximum tuples
    max_tuples = []
    
    # Iterate through both lists simultaneously
    for tuple1, tuple2 in zip(list1, list2):
        # Append the maximum of the two tuples to the result list
        max_tuples.append(max(tuple1, tuple2))
    
    return max_tuples

# Test the function with the provided assertion
assert max_similar_indices([(2, 4), (6, 7), (5, 1)], [(5, 4), (8, 10), (8, 14)]) == [(5, 4), (8, 10), (8, 14)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_similar_indices([(2, 4), (6, 7), (5, 1)],[(5, 4), (8, 10), (8, 14)]) == [(5, 4), (8, 10), (8, 14)]
    assert max_similar_indices([(3, 5), (7, 8), (6, 2)],[(6, 5), (9, 11), (9, 15)]) == [(6, 5), (9, 11), (9, 15)]
    assert max_similar_indices([(4, 6), (8, 9), (7, 3)],[(7, 6), (10, 12), (10, 16)]) == [(7, 6), (10, 12), (10, 16)]
