# MBPP/512
### Completion
def count_element_freq(nested_tuple):
    frequency = {}

    def count_elements(t):
        for element in t:
            if isinstance(element, tuple):
                count_elements(element)  # Recursively count elements in the nested tuple
            else:
                if element in frequency:
                    frequency[element] += 1
                else:
                    frequency[element] = 1

    count_elements(nested_tuple)
    return frequency

# Test the function with the provided assertion
assert count_element_freq((5, 6, (5, 6), 7, (8, 9), 9)) == {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_element_freq((5, 6, (5, 6), 7, (8, 9), 9) ) == {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}
    assert count_element_freq((6, 7, (6, 7), 8, (9, 10), 10) ) == {6: 2, 7: 2, 8: 1, 9: 1, 10: 2}
    assert count_element_freq((7, 8, (7, 8), 9, (10, 11), 11) ) == {7: 2, 8: 2, 9: 1, 10: 1, 11: 2}
