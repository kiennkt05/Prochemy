# MBPP/741
### Completion
def all_Characters_Same(s):
    if not s:  # Check if the string is empty
        return True  # Consider empty string as having all same characters
    return all(char == s[0] for char in s)

# Test the function with the provided assertion
assert all_Characters_Same("python") == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert all_Characters_Same("python") == False
    assert all_Characters_Same("aaa") == True
    assert all_Characters_Same("data") == False
