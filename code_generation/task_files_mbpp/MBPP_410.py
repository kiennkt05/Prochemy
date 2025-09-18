# MBPP/410
### Completion
def min_val(heterogeneous_list):
    # Filter out non-numeric values
    numeric_values = [item for item in heterogeneous_list if isinstance(item, (int, float))]
    
    # Return the minimum value if there are numeric values, otherwise return None
    return min(numeric_values) if numeric_values else None

# Test the function with the provided assertion
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20
