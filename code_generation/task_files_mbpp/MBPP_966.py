# MBPP/966
### Completion
def remove_empty(tuples_list):
    return [t for t in tuples_list if t]

# Test the function with the provided assertion
assert remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]) == [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])==[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']  
    assert remove_empty([(), (), ('',), ("python"), ("program")])==[('',), ("python"), ("program")]  
    assert remove_empty([(), (), ('',), ("java")])==[('',),("java") ]  
