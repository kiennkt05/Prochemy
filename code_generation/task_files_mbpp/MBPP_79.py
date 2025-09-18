# MBPP/79
### Completion
def word_len(word):
    return len(word) % 2 != 0

# Test the function with the provided assertion
assert word_len("Hadoop") == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert word_len("Hadoop") == False
    assert word_len("great") == True
    assert word_len("structure") == True
