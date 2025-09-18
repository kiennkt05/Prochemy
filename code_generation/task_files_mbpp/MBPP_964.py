# MBPP/964
### Completion
def word_len(word):
    return len(word) % 2 == 0

# Test the function with the provided assertion
assert word_len("program") == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert word_len("program") == False
    assert word_len("solution") == True
    assert word_len("data") == True
