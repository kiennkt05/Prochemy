# MBPP/294
### Completion
def max_val(heterogeneous_list):
    max_value = None
    
    for item in heterogeneous_list:
        if isinstance(item, (int, float)):  # Check if the item is a number
            if max_value is None or item > max_value:
                max_value = item
                
    return max_value

# Test the function with the provided assertion
assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
    assert max_val(['Python', 15, 20, 25])==25
    assert max_val(['Python', 30, 20, 40, 50, 'version'])==50
