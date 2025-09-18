# MBPP/712
### Completion
def remove_duplicate(lst):
    seen = set()
    result = []
    for sublist in lst:
        # Convert the sublist to a tuple (which is hashable) to check for duplicates
        sublist_tuple = tuple(sublist)
        if sublist_tuple not in seen:
            seen.add(sublist_tuple)
            result.append(sublist)
    return result

# Test the function with the provided assertion
assert remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]) == [[10, 20], [40], [30, 56, 25], [33]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])==[[10, 20], [30, 56, 25], [33], [40]] 
    assert remove_duplicate(["a", "b", "a", "c", "c"] )==["a", "b", "c"]
    assert remove_duplicate([1, 3, 5, 6, 3, 5, 6, 1] )==[1, 3, 5, 6]
