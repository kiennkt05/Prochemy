# MBPP/18
### Completion
def remove_dirty_chars(s1, s2):
    return ''.join(char for char in s1 if char not in s2)

# Test the function with the provided assertion
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles' 
