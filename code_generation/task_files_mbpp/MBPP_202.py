# MBPP/202
### Completion
def remove_even(s):
    return ''.join(s[i] for i in range(len(s)) if i % 2 != 0)

# Test the function with the provided assertion
assert remove_even("python") == "pto"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_even("python")==("pto")
    assert remove_even("program")==("porm")
    assert remove_even("language")==("lnug")
