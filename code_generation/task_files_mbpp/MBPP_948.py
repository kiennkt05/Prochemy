# MBPP/948
### Completion
def get_item(tup, index):
    return tup[index:index+1]

# Test the function with the provided assertion
assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 3) == ('e',)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),3)==('e')
    assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-4)==('u')
    assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-3)==('r')
