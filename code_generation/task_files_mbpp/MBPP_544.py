# MBPP/544
### Completion
def flatten_tuple(tuple_list):
    # Flatten the list of tuples and join the elements into a single string
    return ' '.join(item for tup in tuple_list for item in tup)

# Test the function with the provided assertion
assert flatten_tuple([('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]) == '1 4 6 5 8 2 9 1 10'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert flatten_tuple([('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]) == '1 4 6 5 8 2 9 1 10'
    assert flatten_tuple([('2', '3', '4'), ('6', '9'), ('3', '2'), ('2', '11')]) == '2 3 4 6 9 3 2 2 11'
    assert flatten_tuple([('14', '21', '9'), ('24', '19'), ('12', '29'), ('23', '17')]) == '14 21 9 24 19 12 29 23 17'
