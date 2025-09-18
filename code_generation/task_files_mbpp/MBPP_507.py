# MBPP/507
### Completion
def remove_words(original_list, words_to_remove):
    return [word for word in original_list if word not in words_to_remove]

# Test the function with the provided assertion
assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'], ['white', 'orange']) == ['red', 'green', 'blue', 'black']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'],['white', 'orange'])==['red', 'green', 'blue', 'black']
    assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'],['black', 'orange'])==['red', 'green', 'blue', 'white']
    assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'],['blue', 'white'])==['red', 'green', 'black', 'orange']
