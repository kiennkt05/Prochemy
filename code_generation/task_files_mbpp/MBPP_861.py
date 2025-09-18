# MBPP/861
### Completion
def anagram_lambda(words, target):
    # Sort the target string to create a reference for comparison
    sorted_target = sorted(target)
    # Use a lambda function to filter the list of words
    return list(filter(lambda word: sorted(word) == sorted_target, words))

# Test the function with the provided assertion
assert anagram_lambda(["bcda", "abce", "cbda", "cbea", "adcb"], "abcd") == ['bcda', 'cbda', 'adcb']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert anagram_lambda(["bcda", "abce", "cbda", "cbea", "adcb"],"abcd")==['bcda', 'cbda', 'adcb']
    assert anagram_lambda(["recitals"," python"], "articles" )==["recitals"]
    assert anagram_lambda([" keep"," abcdef"," xyz"]," peek")==[" keep"]
