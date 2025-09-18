# MBPP/204
### Completion
def count(string, char):
    return string.count(char)

# Test the function with the provided assertion
assert count("abcc", "c") == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count("abcc","c") == 2
    assert count("ababca","a") == 3
    assert count("mnmm0pm","m") == 4
