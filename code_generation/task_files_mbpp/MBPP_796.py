# MBPP/796
### Completion
def return_sum(input_dict):
    return sum(input_dict.values())

# Test the function with the provided assertion
assert return_sum({'a': 100, 'b': 200, 'c': 300}) == 600
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
    assert return_sum({'a': 25, 'b':18, 'c':45}) == 88
    assert return_sum({'a': 36, 'b':39, 'c':49}) == 124
