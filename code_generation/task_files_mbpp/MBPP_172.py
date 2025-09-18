# MBPP/172
### Completion
def count_occurance(s):
    return s.count('std')

# Test the function
assert count_occurance("letstdlenstdporstd") == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_occurance("letstdlenstdporstd") == 3
    assert count_occurance("truststdsolensporsd") == 1
    assert count_occurance("makestdsostdworthit") == 2
