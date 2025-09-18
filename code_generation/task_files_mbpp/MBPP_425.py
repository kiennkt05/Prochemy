# MBPP/425
### Completion
def count_element_in_list(sublists, element):
    count = 0
    for sublist in sublists:
        if element in sublist:
            count += 1
    return count

# Test the function with the provided assertion
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
    assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3
    assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1
