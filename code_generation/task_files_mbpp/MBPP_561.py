# MBPP/561
### Completion
def assign_elements(pairs):
    result = {}
    
    # Create the mapping
    for a, b in pairs:
        if a not in result:
            result[a] = []
        if b not in result:
            result[b] = []
        result[a].append(b)
    
    # Ensure all elements are represented in the result
    for a, b in pairs:
        if b not in result:
            result[b] = []
    
    return result

# Test the function with the provided assertion
assert assign_elements([(5, 3), (7, 5), (2, 7), (3, 8), (8, 4)]) == {3: [8], 5: [3], 7: [5], 2: [7], 8: [4], 4: []}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert assign_elements([(5, 3), (7, 5), (2, 7), (3, 8), (8, 4)] ) == {3: [8], 5: [3], 7: [5], 2: [7], 8: [4], 4: []}
    assert assign_elements([(6, 4), (9, 4), (3, 8), (4, 9), (9, 5)] ) == {4: [9], 6: [4], 9: [4, 5], 8: [], 3: [8], 5: []}
    assert assign_elements([(6, 2), (6, 8), (4, 9), (4, 9), (3, 7)] ) == {2: [], 6: [2, 8], 8: [], 9: [], 4: [9, 9], 7: [], 3: [7]}
