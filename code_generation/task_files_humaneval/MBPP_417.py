# MBPP/417
### Completion
def group_tuples(tuples_list):
    from collections import defaultdict
    
    # Step 1: Create a dictionary to group tuples by their first element
    grouped = defaultdict(list)
    
    for first, second in tuples_list:
        grouped[first].append(second)
    
    # Step 2: Construct the result list
    result = []
    for first, seconds in grouped.items():
        # Combine the first element with all second elements
        result.append((first, *seconds))
    
    return result

# Test case
assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]
