# MBPP/614
### Completion
def cumulative_sum(tuple_list):
    total = 0
    for tup in tuple_list:
        total += sum(tup)
    return total

# Test the function with the provided assertion
assert cumulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
    assert cummulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37
    assert cummulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44
