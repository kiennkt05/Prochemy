# MBPP/788
### Completion
def new_tuple(lst, string):
    return tuple(lst) + (string,)

# Test the function with the provided assertion
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')
    assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')
