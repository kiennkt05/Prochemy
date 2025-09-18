# MBPP/561
### Completion
def assign_elements(pairs):
    # Initialize an empty dictionary to hold the results
    result = {}
    
    # Create a set to hold unique elements
    unique_elements = set()
    
    # First pass: collect unique elements
    for a, b in pairs:
        unique_elements.add(a)
        unique_elements.add(b)
    
    # Initialize the result dictionary with empty lists
    for element in unique_elements:
        result[element] = []
    
    # Second pass: populate the result dictionary
    for a, b in pairs:
        result[a].append(b)
        result[b].append(a)
    
    # Remove self-pairing (if any) to match the expected output
    for key in result:
        result[key] = [x for x in result[key] if x != key]
    
    return result

# Test the function with the provided test case
assert assign_elements([(5, 3), (7, 5), (2, 7), (3, 8), (8, 4)]) == {3: [8], 5: [3], 7: [5], 2: [7], 8: [4], 4: []}

# The function should work correctly for the provided test case.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert assign_elements([(5, 3), (7, 5), (2, 7), (3, 8), (8, 4)] ) == {3: [8], 5: [3], 7: [5], 2: [7], 8: [4], 4: []}
    assert assign_elements([(6, 4), (9, 4), (3, 8), (4, 9), (9, 5)] ) == {4: [9], 6: [4], 9: [4, 5], 8: [], 3: [8], 5: []}
    assert assign_elements([(6, 2), (6, 8), (4, 9), (4, 9), (3, 7)] ) == {2: [], 6: [2, 8], 8: [], 9: [], 4: [9, 9], 7: [], 3: [7]}
