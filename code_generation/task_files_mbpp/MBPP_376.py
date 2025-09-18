# MBPP/376
### Completion
def remove_replica(input_tuple, custom_value='MSP'):
    # Create a dictionary to count occurrences of each element
    count_dict = {}
    
    # Count occurrences of each element in the tuple
    for item in input_tuple:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    
    # Create a new tuple with duplicates replaced by the custom value
    result = tuple(custom_value if count_dict[item] > 1 else item for item in input_tuple)
    
    return result

# Test the function with the provided assertion
assert remove_replica((1, 1, 4, 4, 4, 5, 5, 6, 7, 7)) == (1, 'MSP', 4, 'MSP', 'MSP', 5, 'MSP', 6, 7, 'MSP')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_replica((1, 1, 4, 4, 4, 5, 5, 6, 7, 7)) == (1, 'MSP', 4, 'MSP', 'MSP', 5, 'MSP', 6, 7, 'MSP')
    assert remove_replica((2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9)) == (2, 3, 4, 'MSP', 5, 6, 'MSP', 7, 8, 9, 'MSP')
    assert remove_replica((2, 2, 5, 4, 5, 7, 5, 6, 7, 7)) == (2, 'MSP', 5, 4, 'MSP', 7, 'MSP', 6, 'MSP', 'MSP')
