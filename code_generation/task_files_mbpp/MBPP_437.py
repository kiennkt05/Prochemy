# MBPP/437
### Completion
def remove_odd(s):
    return ''.join(s[i] for i in range(len(s)) if i % 2 != 0)

# Test the function with the provided assertion
assert remove_odd("python") == "yhn"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_odd("python")==("yhn")
    assert remove_odd("program")==("rga")
    assert remove_odd("language")==("agae")
