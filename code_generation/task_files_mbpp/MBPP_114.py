# MBPP/114
### Completion
def assign_freq(tuples_list):
    # Count the frequency of each tuple
    frequency = {}
    for tup in tuples_list:
        if tup in frequency:
            frequency[tup] += 1
        else:
            frequency[tup] = 1
    
    # Create a new list with tuples and their frequencies
    result = [(tup + (freq,)) for tup, freq in frequency.items()]
    
    # Return the result as a string
    return str(result)

# Test the function with the provided assertion
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
