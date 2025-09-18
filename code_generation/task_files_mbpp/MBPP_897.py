# MBPP/897
### Completion
def is_Word_Present(sentence, word):
    # Check if the word is present in the sentence
    return word in sentence.split()

# Test the function with the provided assertion
assert is_Word_Present("machine learning", "machine") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Word_Present("machine learning","machine") == True
    assert is_Word_Present("easy","fun") == False
    assert is_Word_Present("python language","code") == False
