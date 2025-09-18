# MBPP/343
### Completion
def dig_let(s):
    letters_count = sum(c.isalpha() for c in s)
    digits_count = sum(c.isdigit() for c in s)
    return (letters_count, digits_count)

# Test the function with the provided assertion
assert dig_let("python") == (6, 0)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert dig_let("python")==(6,0)
    assert dig_let("program")==(7,0)
    assert dig_let("python3.0")==(6,2)
