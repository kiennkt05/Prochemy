# MBPP/114
### Completion
def assign_freq(tuple_list):
    # Step 1: Count occurrences of each tuple
    frequency_dict = {}
    for tup in tuple_list:
        if tup in frequency_dict:
            frequency_dict[tup] += 1
        else:
            frequency_dict[tup] = 1
    
    # Step 2: Create a new list with tuples and their frequencies
    result = []
    for tup, freq in frequency_dict.items():
        result.append(tup + (freq,))  # Extend the tuple with its frequency
    
    # Step 3: Convert the result to the required string format
    result_str = str(result)
    
    return result_str

# Test the function with the provided test case
assert assign_freq([(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9,), (2, 7)]) == '[(6, 5, 8, 3), (2, 7, 2), (9, 1)]'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert assign_freq([(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)] ) == '[(6, 5, 8, 3), (2, 7, 2), (9, 1)]'
    assert assign_freq([(4, 2, 4), (7, 1), (4, 8), (4, 2, 4), (9, 2), (7, 1)] ) == '[(4, 2, 4, 2), (7, 1, 2), (4, 8, 1), (9, 2, 1)]'
    assert assign_freq([(11, 13, 10), (17, 21), (4, 2, 3), (17, 21), (9, 2), (4, 2, 3)] ) == '[(11, 13, 10, 1), (17, 21, 2), (4, 2, 3, 2), (9, 2, 1)]'
