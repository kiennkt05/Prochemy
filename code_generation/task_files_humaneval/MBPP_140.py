# MBPP/140
### Completion
def extract_singly(tuple_list):
    from collections import Counter
    
    # Step 1: Flatten the list of tuples into a single list
    flattened_list = [item for tup in tuple_list for item in tup]
    
    # Step 2: Count occurrences of each element
    element_count = Counter(flattened_list)
    
    # Step 3: Extract elements that occur exactly once
    singly_occurring_elements = [element for element, count in element_count.items() if count == 1]
    
    return singly_occurring_elements

# Test case
assert extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]) == [3, 7, 1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]) == [3, 4, 5, 7, 1]
    assert extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)]) == [1, 2, 3, 4, 7, 8]
    assert extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)]) == [7, 8, 9, 10, 11, 12]
