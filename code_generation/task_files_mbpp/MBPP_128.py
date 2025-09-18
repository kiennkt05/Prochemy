# MBPP/128
### Completion
def long_words(n, sentence):
    # Split the sentence into words
    words = sentence.split()
    # Filter and return words longer than n
    return [word for word in words if len(word) > n]

# Test the function with the provided assertion
assert long_words(3, "python is a programming language") == ['python', 'programming', 'language']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert long_words(3,"python is a programming language")==['python','programming','language']
    assert long_words(2,"writing a program")==['writing','program']
    assert long_words(5,"sorting list")==['sorting']
