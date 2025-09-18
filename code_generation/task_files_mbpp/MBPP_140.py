# MBPP/140
### Completion
def extract_singly(tuple_list):
    from collections import Counter
    
    # Flatten the list of tuples into a single list
    flat_list = [item for tup in tuple_list for item in tup]
    
    # Count the occurrences of each element
    element_count = Counter(flat_list)
    
    # Extract elements that occur only once
    singly_occurring_elements = [element for element, count in element_count.items() if count == 1]
    
    return singly_occurring_elements

# Test the function with the provided assertion
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
