# MBPP/26
### Completion
def check_k_elements(tuple_list, k):
    return all(len(tup) == k for tup in tuple_list)

# Test the function with the provided assertion
assert check_k_elements([(4, 4), (4, 4, 4), (4, 4), (4, 4, 4, 4), (4, )], 4) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_k_elements([(4, 4), (4, 4, 4), (4, 4), (4, 4, 4, 4), (4, )], 4) == True
    assert check_k_elements([(7, 7, 7), (7, 7)], 7) == True
    assert check_k_elements([(9, 9), (9, 9, 9, 9)], 7) == False
