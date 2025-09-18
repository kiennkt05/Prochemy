# MBPP/537
### Completion
def first_repeated_word(s):
    words = s.split()
    seen = set()
    
    for word in words:
        if word in seen:
            return word
        seen.add(word)
    
    return None  # Return None if no repeated word is found

# Test the function with the provided assertion
assert first_repeated_word("ab ca bc ab") == "ab"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_repeated_word("ab ca bc ab") == "ab"
    assert first_repeated_word("ab ca bc") == 'None'
    assert first_repeated_word("ab ca bc ca ab bc") == "ca"
