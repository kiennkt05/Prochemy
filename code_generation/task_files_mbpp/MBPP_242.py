# MBPP/242
### Completion
def count_charac(s):
    return len(s)

# Test the function with the provided assertion
assert count_charac("python programming") == 18
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_charac("python programming")==18
    assert count_charac("language")==8
    assert count_charac("words")==5
