# MBPP/526
### Completion
def capitalize_first_last_letters(s):
    words = s.split()
    capitalized_words = []
    
    for word in words:
        if len(word) > 1:
            capitalized_word = word[0].upper() + word[1:-1] + word[-1].upper()
        elif len(word) == 1:
            capitalized_word = word.upper()
        else:
            capitalized_word = word  # In case of empty string
        capitalized_words.append(capitalized_word)
    
    return ' '.join(capitalized_words)

# Test the function with the provided assertion
assert capitalize_first_last_letters("python") == "PythoN"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert capitalize_first_last_letters("python") == "PythoN"
    assert capitalize_first_last_letters("bigdata") == "BigdatA"
    assert capitalize_first_last_letters("Hadoop") == "HadooP"
